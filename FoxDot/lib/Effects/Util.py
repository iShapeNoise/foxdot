"""
    Filter Effects
    --------------

    Effects are added to Player objects as keywords instructions like `dur`
    or `amp` but are a little more tricky. Each effect has a "title" keyword,
    which requires a nonzero value to add the effect to a Player. Effects
    also have other attribute keywords which can be any value and may have
    a default value which is set when a Player is created.

    ::
    # Example. Reverb effect "title" is `room` and attribute is `mix`, which
    # defaults to 0.25. The following adds a reverb effect

    p1 >> pads(room=0.5)
    # This still adds the effect, but a mix of 0 doesn't actually do anything
    p1 >> pads(room=0.5, mix=0)
    # This effect is not added as the "title" keyword, room, is 0
    p1 >> pads(room=0, mix=0.5)

    Other effects are outlined below:

    *High Pass Filter* - Title keyword: `hpf`, Attribute keyword(s): `hpr`
    Only frequences **above** the value of `hpf` are kept in the final signal.
    Use `hpr` to set the resonance (usually a value between 0 and 1)

    *Low Pass Filter* - Title keyword: `lpf`, Attribute keyword(s): `lpr`
    Only frequences **below** the value of `lpf` are kept in final signal. Use
    `lpr` to set the resonance (usually a value between 0 and 1)

    *Bitcrush* - Title keyword: `bits`, Attribute keyword(s): `crush`
    The bit depth, in number of `bits`, that the signal is reduced to; this is
    a value between 1 and 24 where other values are ignored. Use `crush` to set
    the amount of reduction to the bitrate (defaults to 8)

    *Reverb* - Title keyword: `room`, Attribute keyword(s): `mix`
    The `room` argument specifies the size of the room and `mix` is the dry/wet
    mix of reverb; this should be a value between 0 and 1 (defalts to 0.25)

    *Chop* - Title keyword: `chop`, Attribute keyword(s): `sus`
    'Chops' the signal into chunks using a low frequency pulse wave over the
    sustain of a note.

    *Slide To* - Title keyword: `slide`, Attribute keyword(s):
    Slides' the frequency value of a signal to `freq * (slide+1)` over the
    duration of a note (defaults to 0)

    *Slide From* - Title keyword: `slidefrom`, Attribute keyword(s):
    Slides' the frequency value of a signal from `freq * (slidefrom)` over the
    duration of a note (defaults to 1)

    *Comb delay (echo)* - Title keyword: `echo`, Attribute keyword(s): `decay`
    Sets the decay time for any echo effect in beats, works best on
    Sample Player (defaults to 0)

    *Panning* - Title keyword: `pan`, Attribute keyword(s):
    Panning, where -1 is far left, 1 is far right (defaults to 0)

    *Vibrato* - Title keyword: `vib`, Attribute keyword(s):
    Vibrato (defaults to 0)

    Undocumented: Spin, Shape, Formant, BandPassFilter, Echo

"""

from __future__ import absolute_import, division, print_function
import os.path
from ..Settings import EFFECTS_DIR, SC3_PLUGINS
from ..ServerManager import Server


class Effect:
    server = Server

    def __init__(self, foxdot_name, synthdef, args={}, control=False):

        self.name = foxdot_name
        self.synthdef = synthdef
        self.filename = EFFECTS_DIR + "/{}.scd".format(self.synthdef)
        self.args = args.keys()
        self.vars = ["osc"]
        self.defaults = args
        self.effects = []
        self.control = control
        self.suffix = "kr" if self.control else "ar"
        self.channels = 1 if self.control else 2
        self.input = "osc = In.{}(bus, {});\n".format(self.suffix,
                                                      self.channels)
        self.output = "ReplaceOut.{}".format(self.suffix)

    @classmethod
    def set_server(cls, server):
        cls.server = server

    def __repr__(self):
        # return "<Fx '{}' -- args: {}>".format(self.synthdef, ", ".join(self.args))
        other_args = ['{}'.format(arg) for arg in self.args if arg != self.name]
        other_args = ", other args={}".format(other_args) if other_args else ""
        return "<'{}': keyword='{}'{}>".format(self.synthdef,
                                               self.name,
                                               other_args)

    def __str__(self):
        s = "SynthDef.new(\{},\n".format(self.synthdef)
        s += "{" + "|bus, {}|\n".format(", ".join(self.args))
        s += "var {};\n".format(",".join(self.vars))
        s += self.input
        s += self.list_effects()
        s += self.output
        s += "(bus, osc)}).add;"
        return s

    def add(self, string):
        self.effects.append(string)
        return

    def doc(self, string):
        """ Set a docstring for the effects"""
        return

    def list_effects(self):
        s = ""
        for p in self.effects:
            s += p + ";\n"
        return s

    def add_var(self, name):
        if name not in self.vars:
            self.vars.append(name)
        return

    def load(self):
        ''' writes to file and sends to server '''

        # 1. See if the file exists
        if os.path.isfile(self.filename):
            with open(self.filename) as f:
                contents = f.read()
        else:
            contents = ""

        # 2. If it does, check contents
        this_string = self.__str__()
        if contents != this_string:
            try:
                with open(self.filename, 'w') as f:
                    f.write(this_string)
            except IOError:
                print("IOError: Unable to update '{}' effect.".format(self.synthdef))

        # 3. Send to server
        self.load()

    def load(self):
        """ Load the Effect """
        if self.server is not None:
            self.server.loadSynthDef(self.filename)
        return


class In(Effect):
    def __init__(self):
        Effect.__init__(self, 'startSound', 'startSound')
        self.load()

    def __str__(self):
        s = "SynthDef.new(\startSound,\n"
        s += "{ arg bus, rate=1, sus; var osc;\n"
        s += "	ReplaceOut.kr(bus, rate)}).add;\n"
        return s


class Out(Effect):
    def __init__(self):
        self.max_duration = 8
        Effect.__init__(self, 'makeSound', 'makeSound')
        self.load()

    def __str__(self):
        s = "SynthDef.new(\makeSound,\n"
        s += "{ arg bus, sus; var osc;\n"
        s += "	osc = In.ar(bus, 2);\n"
        s += "  osc = EnvGen.ar(Env([1,1,0],[sus * {}, 0.1]), doneAction: 14) * osc;\n".format(self.max_duration)
        s += "	DetectSilence.ar(osc, amp:0.0001, time: 0.1, doneAction: 14);\n"
        # s += "	Out.ar(0, osc);\n"
        s += "OffsetOut.ar(0, osc[0]);\n"
        s += "OffsetOut.ar(1, osc[1]);\n"
        s += " }).add;\n"
        return s


class EffectManager(dict):

    def __init__(self):
        dict.__init__(self)
        self.kw = []
        self.all_kw = []
        self.defaults = {}
        self.order = {N: [] for N in range(3)}

    def __repr__(self):
        return "\n".join([repr(value) for value in self.values()])

    def values(self):
        return [self[key] for key in self.sort_by("synthdef")]

    def sort_by(self, attr):
        """ Returns the keys sorted by attribute name"""
        return sorted(self.keys(),
                      key=lambda effect: getattr(self[effect],
                      attr))

    def new(self, foxdot_arg_name, synthdef, args, order=2):
        self[foxdot_arg_name] = Effect(foxdot_arg_name,
                                       synthdef, args,
                                       order == 0)

        if order in self.order:
            self.order[order].append(foxdot_arg_name)
        else:
            self.order[order] = [foxdot_arg_name]

        # Store the main keywords together
        self.kw.append(foxdot_arg_name)

        # Store other sub-keys
        for arg in args:
            if arg not in self.all_kw:
                self.all_kw.append(arg)
            # Store the default value
            self.defaults[arg] = args[arg]

        return self[foxdot_arg_name]

    def kwargs(self):
        """ Returns the title keywords for each effect """
        return tuple(self.kw)

    def all_kwargs(self):
        """ Returns *all* keywords for all effects """
        return tuple(self.all_kw)

    def __iter__(self):
        for key in self.kw:
            yield key, self[key]

    def reload(self):
        """ Re-sends each effect to SC """
        for kw, effect in self:
            effect.load()
        In()
        Out()
        return


# -- TODO

# Have ordered effects e.g.
# 0. Process frequency / playback rate
# 1. Before envelope
# 2. Adding the envelope
# 3. After envelope

FxList = EffectManager()

Effects = FxList  # Alias - to become default

# Frequency Effects, Signal Effects, Post-envelope Effects
# Credits to CrashSever team

fx = FxList.new("bend",
                "bend",
                {"bend": 0, "sus": 1, "benddelay": 0},
                order=0)
fx.add("osc = osc * EnvGen.ar(Env([1, 1, 1 + bend, 1], [sus * benddelay, (sus*(1-benddelay)/2), (sus*(1-benddelay)/2)]))")
fx.load()

fx = FxList.new("bpf",
                "bpf",
                {"bpf": 0, "bpr": 1, "bpnoise": 0, "sus": 1},
                order=2)
fx.add("bpnoise = bpnoise / sus")
fx.add("bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2)")
fx.add("bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2)")
fx.add("osc = BPF.ar(osc, bpf, bpr)")
fx.load()

fx = FxList.new('chop', 'chop', {'chop': 0,
                                 'sus': 1,
                                 'chopmix': 1,
                                 'chopwave': 0,
                                 'chopi': 0}, order=2)
fx.add("osc = LinXFade2.ar(osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)]), osc, 1-chopmix)")
fx.load()

fx = FxList.new('chorus',
                'chorus',
                {'chorus': 0, 'chorusrate': 0.5, 'numDelays': 4},
                order=2)
fx.doc("Derek Kwan chorus")
fx.add_var("lfos")
fx.add_var("chrate")
fx.add_var("maxDelayTime")
fx.add_var("minDelayTime")
fx.add("chrate = Select.kr(chorusrate > 0.5, [LinExp.kr(chorusrate, 0.0, 0.5, 0.025, 0.125), LinExp.kr(chorusrate, 0.5, 1.0, 0.125, 2)])")
fx.add("maxDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.016, 0.052)")
fx.add("minDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.012, 0.022)")
fx.add("osc = osc * numDelays.reciprocal;")
fx.add("lfos = Array.fill(numDelays, {|i| LFPar.kr(chrate * {rrand(0.95, 1.05)}, 0.9 * i,(maxDelayTime - minDelayTime) * 0.5,(maxDelayTime + minDelayTime) * 0.5,)})")
fx.add("osc = DelayC.ar(osc, (maxDelayTime * 2), lfos).sum")
fx.add("osc = Mix(osc)")
fx.load()

fx = FxList.new("coarse", "coarse", {"coarse": 0, "sus": 1}, order=0)
fx.add("osc = osc * LFPulse.ar(coarse / sus)")
fx.load()

fx = FxList.new("comp", "comp", {"comp": 0,
                                 "comp_down": 1,
                                 "comp_up": 0.8}, order=2)
fx.add("osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1)")
fx.load()

fx = FxList.new("cut", "cut", {"cut": 0, "sus": 1}, order=2)
fx.add("osc = osc * EnvGen.ar(Env(levels: [1,1,0.01], curve: 'step', times: [sus * cut, 0.01]))")
fx.load()

fx = FxList.new('dfm', 'dfm', {'dfm': 1000, 'dfmr': 0.1, 'dfmd': 1}, order=2)
fx.doc("DFM1 low pass filter")
fx.add('osc = DFM1.ar(osc, dfm, dfmr, dfmd,0.0)')
fx.load()

fx = FxList.new("dist2", "dist2", {"dist2": 0,
                                   "dist2mix": 1,
                                   "dist2shape": 0.1}, order=2)
fx.add_var("tmp")
fx.add("tmp = Fold.ar(osc, -1*dist2shape, dist2shape)")
fx.add("tmp = (tmp * 16.dbamp * dist2).tanh")
fx.add("tmp = BHiShelf.ar(tmp, 9000, 0.8, -12)")
fx.add("tmp = LPF.ar(tmp, 9000)")
fx.add("osc = LinXFade2.ar(tmp, osc, 1-dist2mix)")
fx.load()

fx = FxList.new('djf', 'djf', {'djf': 0, 'djfq': 0.3}, order=2)
fx.doc("DJ Filter")
fx.add_var('lpfCutoffFreq')
fx.add_var('hpfCutoffFreq')
fx.add('lpfCutoffFreq = djf.linexp(0, 0.5, 50, 15000)')
fx.add('hpfCutoffFreq = djf.linexp(0.5, 1, 50, 15000)')
fx.add('osc = RHPF.ar(RLPF.ar(osc,lpfCutoffFreq, djfq),hpfCutoffFreq, djfq)')
fx.load()

fx = FxList.new("drive", "drive", {"drive": 0, "drivemix": 1}, order=2)
fx.add("osc = LinXFade2.ar((osc * (drive * 50)).clip(0,0.2).fold2(2), osc, 1-drivemix)")
fx.load()

fx = FxList.new("drop", "drop", {"drop": 0, "dropof": 100}, order=2)
fx.doc("Tidal Effect: Waveloss disto")
fx.add("osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2)")
fx.load()

fx = FxList.new("easr", "easr", {"a": 0,
                                 "s": 1,
                                 "r": 1,
                                 "ac": 0,
                                 "rc": 0}, order=2)
fx.doc("Envelope: Attack/Sustain/Release with ac and rc as curve arguments")
fx.add_var("env")
fx.add("env = EnvGen.ar(Env.new(levels: [0,1,1,0], times:[a*sus, max((a*sus + r*sus), sus - (a*sus + r*sus)), r*sus], curve:[ac,0,rc]))")
fx.add("osc = osc * env")
fx.load()

fx = FxList.new('ehpf', 'ehpf', {'ehpf': 0,
                                 'ehpr': 0.7,
                                 'ehpa': 0.001,
                                 'ehps': 0.01,
                                 'ehpc': -3,
                                 'sus': 1}, order=2)
fx.doc("Envelope: High pass filter")
fx.add_var("env")
fx.add('env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc))')
fx.add('osc = RHPF.ar(osc, ehpf, ehpr, mul: env)')
fx.load()

fx = FxList.new('elpf', 'elpf', {'elpf': 0,
                                 'elpr': 0.7,
                                 'elpa': 0.001,
                                 'elps': 0.01,
                                 'elpc': -3,
                                 'sus': 1}, order=2)
fx.doc("Envelope: Low pass filter")
fx.add_var("env")
fx.add('env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0)')
fx.add('osc = RLPF.ar(osc, LinLin.ar(env, 0, 1, 0, elpf)+10, elpr, mul: 1)')
fx.load()

fx = FxList.new('eqlow', 'eqlow', {'eqlow': 1, 'eqlowfreq': 80}, order=2)
fx.doc("Low shelf Equalizer")
fx.add('osc = BLowShelf.ar(osc, freq: eqlowfreq, db: abs(eqlow).ampdb)')
fx.load()

fx = FxList.new('eqmid', 'eqmid', {'eqmid': 1,
                                   'eqmidfreq': 1000,
                                   'eqmidq': 1}, order=2)
fx.doc("Middle boost Equalizer")
fx.add('osc = BPeakEQ.ar(osc, freq: eqmidfreq, rq: eqmidq.reciprocal, db: abs(eqmid).ampdb)')
fx.load()

fx = FxList.new('eqhigh', 'eqhigh', {'eqhigh': 1, 'eqhighfreq': 8000}, order=2)
fx.doc("High shelf Equalizer")
fx.add('osc = BHiShelf.ar(osc, freq: eqhighfreq, db: abs(eqhigh).ampdb)')
fx.load()

fx = FxList.new('echo', 'echo', {'echo': 0,
                                 'echomix': 1,
                                 'beat_dur': 1,
                                 'echotime': 1}, order=2)
fx.add('osc = LinXFade2.ar(osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur), osc, 1-echomix)')
fx.load()

fx = FxList.new('fdist', 'fdist', {'fdist': 0, 'fdisfreq': 1600}, order=1)
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.1 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.1 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 1.4 * fdist).tanh")
fx.add("osc = LPF.ar(osc, fdistfreq)")
fx.add("osc = (osc * 2 * fdist).tanh")
fx.add("osc = osc * 0.2")
fx.load()

fx = FxList.new('fdistc', 'fdistc', {'fdistc': 0,
                                     'fdistcfreq1': 0,
                                     'fdistcfreq2': 0,
                                     'fdistcfreq3': 0,
                                     'fdistcfreq4': 0,
                                     'fdistcm1': 0,
                                     'fdistcm2': 0,
                                     'fdistcm3': 0,
                                     'fdistcm4': 0,
                                     'fdistcp1': 0,
                                     'fdistcp2': 0,
                                     'fdistcp3': 0,
                                     'fdistcp4': 0
                                     }, order=1)
fx.add("osc = RLPF.ar(osc, fdistcfreq1, fdistcq1)")
fx.add("osc = (osc * fdistcm1 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq2, fdistcq2)")
fx.add("osc = (osc * fdistcm2 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq3, fdistcq3)")
fx.add("osc = (osc * fdistcm3 * fdistc).tanh")
fx.add("osc = RLPF.ar(osc, fdistcfreq4, fdistcq4)")
fx.add("osc = (osc * fdistcm4 * fdistc).tanh")
fx.load()

fx = FxList.new('flanger', 'flanger', {'flanger': 0,
                                       'fdecay': 0,
                                       'flangermix': 1}, order=2)
fx.add("osc = LinXFade2.ar(CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1),  osc, 1-flangermix)")
fx.load()

fx = FxList.new("formant", "formant", {"formant": 0,
                                       "formantmix": 1}, order=2)
fx.add("formant = (formant % 8) + 1")
fx.add("osc = LinXFade2.ar(Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh, osc, 1-formantmix)")
fx.load()

fx = FxList.new("glide", "glide", {"glide": 0, "glidedur": 0.05}, order=0)
fx.doc("Glide mode")
fx.add("osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur)")
fx.load()

fx = FxList.new('hpf', 'hpf', {'hpf': 0, 'hpr': 1}, order=2)
fx.doc("Highpass filter")
fx.add('osc = RHPF.ar(osc, hpf, hpr)')
fx.load()

fx = FxList.new('krush', 'krush', {'krush': 0, 'kutoff': 15000}, order=2)
fx.doc("Tidal Effect: Distortion")
fx.add_var("signal")
fx.add_var("freq")
fx.add("freq = Select.kr(kutoff > 0, [DC.kr(4000), kutoff])")
fx.add("signal = (osc.squared + (krush * osc)) / (osc.squared + (osc.abs * (krush - 1.0)) + 1.0)")
fx.add("signal = RLPF.ar(signal, clip(freq, 20, 10000), 1)")
fx.add("osc = SelectX.ar(krush * 2.0, [osc, signal])")
fx.load()

fx = FxList.new('leg', 'leg', {'leg': 0, 'sus': 1}, order=0)
fx.doc("Legato slide")
fx.add("osc = osc * XLine.ar(Rand(0.5,1.5)*leg,1,0.05*sus)")
fx.load()

fx = FxList.new('lofi', 'lofi', {'lofi': 0,
                                 'lofiwow': 1,
                                 'lofiamp': 0,
                                 'minWowRate': 0.5,
                                 'maxDepth': 35}, order=2)
fx.add_var("wowRate")
fx.add_var("maxLfoDepth")
fx.add_var("depth")
fx.add_var("depthLfoAmount")
fx.add_var("wowMul")
fx.add_var("maxDelay")
fx.add_var("ratio")
fx.add_var("threshold")
fx.add_var("gain")
fx.add("osc = HPF.ar(osc, 25)")
fx.add("ratio = LinExp.kr(lofiamp, 0, 1, 0.15, 0.01)")
fx.add("threshold = LinLin.kr(lofiamp, 0, 1, 0.8, 0.33)")
fx.add("gain = 1/(((1.0-threshold) * ratio) + threshold)")
fx.add("osc = Limiter.ar(Compander.ar(osc, osc, threshold, 1.0, ratio, 0.1, 1, gain), dur: 0.0008)")
fx.add("wowRate = LinExp.kr(lofiwow, 0, 1, minWowRate, 4)")
fx.add("maxLfoDepth = 5")
fx.add("depth = LinExp.kr(lofiwow, 0, 1, 1, maxDepth - maxLfoDepth)")
fx.add("depthLfoAmount = LinLin.kr(lofiwow, 0, 1, 1, maxLfoDepth).floor")
fx.add("depth = LFPar.kr(depthLfoAmount * 0.1, mul: depthLfoAmount, add: depth)")
fx.add("wowMul = ((2 ** (depth * 1200.reciprocal)) - 1)/(4 * wowRate)")
fx.add("maxDelay = (((2 ** (maxDepth * 1200.reciprocal)) - 1)/(4 * minWowRate)) * 2.5")
fx.add("osc = DelayC.ar(osc, maxDelay, SinOsc.ar(wowRate, 2, wowMul, wowMul + ControlRate.ir.reciprocal))")
fx.add("osc = ((osc * LinExp.kr(lofiamp, 0, 1, 1, 2.5))).tanh")
fx.add("osc = LPF.ar(osc, LinExp.kr(lofi, 0, 1, 2500, 10000))")
fx.add("osc = HPF.ar(osc, LinExp.kr(lofi, 0, 1, 40, 1690))")
fx.add("osc = MoogFF.ar(osc, LinExp.kr(lofi, 0, 1, 1000, 10000), 0)")
fx.load()

fx = FxList.new('lpf', 'lpf', {'lpf': 0, 'lpr': 1}, order=2)
fx.add('osc = RLPF.ar(osc, lpf, lpr)')
fx.load()

fx = FxList.new('mpf', 'mpf', {'mpf': 0, 'mpr': 0}, order=2)
fx.add("osc = MoogFF.ar(osc, mpf, mpr, 0, 1)")
fx.load()

fx = FxList.new('octafuz', 'octafuz', {'octafuz': 0, 'octamix': 1}, order=2)
fx.doc("Octafuz Distortion")
fx.add_var("dis")
fx.add_var("osc_base")
fx.add("osc_base = osc")
fx.add("dis = [1,1.01,2,2.02,4.5,6.01,7.501]")
fx.add("dis = dis ++ (dis*6)")
fx.add("osc = ((osc * dis*octafuz).sum.distort)")
fx.add("osc = (osc * 1/16)!2")
fx.add("osc = LinXFade2.ar(osc_base, osc, octamix)")
fx.load()

fx = FxList.new("octer", "octer", {"octer": 0,
                                   "octersub": 0,
                                   "octersubsub": 0
                                   }, order=1)
fx.add_var("oct1")
fx.add_var("oct2")
fx.add_var("oct3")
fx.add_var("sub")
fx.add("oct1 = 2.0 * LeakDC.ar(abs(osc))")
fx.add("sub = LPF.ar(osc, 440)")
fx.add("oct2 = ToggleFF.ar(sub)")
fx.add("oct3 = ToggleFF.ar(oct2)")
fx.add("osc = SelectX.ar(octer, [osc, octer*oct1, DC.ar(0)])")
fx.add("osc = osc + (octersub * oct2 * sub) + (octersubsub * oct3 * sub)")
fx.load()

fx = FxList.new('output', 'output', {'output': 0}, order=2)
fx.doc("Output select Bus")
fx.add("Out.ar(output, osc)")
fx.load()

fx = FxList.new('phaser', 'phaser', {'phaser': 0, 'phaserdepth': 1}, order=2)
fx.add_var("delayedSignal")
fx.add("delayedSignal = osc")
fx.add("for(1, 4, {|i| delayedSignal = AllpassL.ar(delayedSignal, 0.01 * 4.reciprocal, LFPar.kr(LinExp.kr(phaser, 0, 1, 0.275, 16), i + 0.5.rand, LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5), LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5)), 0)})")
fx.add("osc = osc + delayedSignal")
fx.load()

fx = FxList.new('pong', 'pong', {'pong': 0, 'beat_dur': 1, 'pongtime': 1}, order=2)
fx.doc("Ping pong delay")
fx.add_var("left")
fx.add_var("right")
fx.add("left = CombN.ar(osc, delaytime: pong * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur)")
fx.add("left = left*2.distort.tanh")
fx.add("left = LPF.ar(left, 12000)")
fx.add("left = HPF.ar(left, 300)")
fx.add("right = CombN.ar(osc, delaytime: pong * beat_dur + pong * beat_dur*0.5, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur)")
fx.add("right = right*2.distort.tanh")
fx.add("right = LPF.ar(right,12000)")
fx.add("right = HPF.ar(right,300)")
fx.add("osc = osc + [left, right]")
fx.load()

fx = FxList.new('resonz', 'resonz', {'rfreq': 50, 'resonz': 0.1}, order=2)
fx.doc("Resonz")
fx.add('osc = Resonz.ar(osc, freq: rfreq, bwr: resonz)')
fx.load()

fx = FxList.new("pshift", "pshift", {"pshift": 0}, order=0)
fx.add("osc = osc * (1.059463**pshift)")
fx.load()

fx = FxList.new("ring", "ring", {"ring": 0,
                                 "ringl": 500,
                                 "ringh": 1500}, order=0)
fx.doc("Ring Modulator")
fx.add_var("mod")
fx.add("mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000))")
fx.add("osc = ring1(osc, mod)")
fx.load()

fx = FxList.new('ringz', 'ringz', {'ringzfreq': 0, 'ringz': 0}, order=2)
fx.doc("Z of Ringmodulation")
fx.add("Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05)")
fx.load()

fx = FxList.new('room', 'room', {'room': 0, 'mix': 0.1}, order=2)
fx.add("osc = FreeVerb.ar(osc, mix, room)")
fx.load()

fx = FxList.new('room2', 'room2', {'room2': 0,
                                   'mix2': 0.2,
                                   'damp2': 0.8,
                                   'revatk': 0,
                                   'revsus': 1}, order=2)
fx.add_var("dry")
fx.add("dry = osc")
fx.add("osc = HPF.ar(osc, 100)")
fx.add("osc = LPF.ar(osc, 10000)")
fx.add("osc = FreeVerb2.ar(osc[0], osc[1], 1, room2, damp2)")
fx.add("osc = osc * EnvGen.ar(Env([0,1,0], [revatk,revsus], curve: 'welch'))")
fx.add("osc = SelectX.ar(mix2, [dry, osc])")
fx.load()

fx = FxList.new('sample_atk', 'sample_atk', {'sample_atk': 0,
                                             'sample_sus': 1}, order=2)
fx.add_var("env")
fx.add("env = EnvGen.ar(Env.new(levels: [0,1,0], times:[sample_atk, sample_sus], curve: 'lin'))")
fx.add("osc = osc*env")
fx.load()

fx = FxList.new("shape", "shape", {"shape": 0, "shapemix": 1}, order=2)
fx.add("osc = LinXFade2.ar((osc * (shape * 50)).fold2(1).distort / 5, osc, 1-shapemix)")
fx.load()

fx = FxList.new("shift", "shift", {"shift": 0, "shiftsize": 0.1}, order=1)
fx.doc("Pitch Shifter")
fx.add("osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01)")
fx.load()

fx = FxList.new("slide", "slide", {"slide": 0,
                                   "sus": 1,
                                   "slidedelay": 0}, order=0)
fx.add("osc = osc * EnvGen.ar(Env([1, 1, slide + 1], [sus*slidedelay, sus*(1-slidedelay)]))")
fx.load()

fx = FxList.new("slidefrom", "slidefrom", {"slidefrom": 0,
                                           "sus": 1,
                                           "slidedelay": 0}, order=0)
fx.add("osc = osc * EnvGen.ar(Env([slidefrom + 1, slidefrom + 1, 1], [sus*slidedelay, sus*(1-slidedelay)]))")
fx.load()

fx = FxList.new('spf', 'spf', {'spf': 0,
                               'spr': 1,
                               'spfslide': 1,
                               'spfend': 15000}, order=2)
fx.doc("Lpf slide")
fx.add_var("spfenv")
fx.add("spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]))")
fx.add("osc = RLPF.ar(osc, spfenv, spr)")
fx.load()

fx = FxList.new('spin', 'spin', {'spin': 0, 'sus': 1}, order=2)
fx.add('osc = osc * [FSinOsc.ar(spin / 2, iphase: 1, mul: 0.5, add: 0.5), FSinOsc.ar(spin / 2, iphase: 3, mul: 0.5, add: 0.5)]')
fx.load()

fx = FxList.new('squiz', 'squiz', {'squiz': 0}, order=2)
fx.doc("Tidal Effect: Squiz Disto")
fx.add("osc = Squiz.ar(osc, squiz)")
fx.load()

fx = FxList.new("striate", "striate", {"striate": 0,
                                       "sus": 1,
                                       "buf": 0,
                                       "rate": 1}, order=0)
fx.add("rate = (BufDur.kr(buf) / sus)")
fx.add("rate = Select.kr(rate > 1, [1, rate])")
fx.add("osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate")
fx.load()

fx = FxList.new('swell', 'swell', {'swell': 0, 'sus': 1, 'hpr': 1}, order=2)
fx.add_var("env")
fx.add("env = EnvGen.kr(Env([0,1,0], times:[(sus*0.25), (sus*0.25)], curve:\\sin))")
fx.add('osc = RHPF.ar(osc, env * swell * 2000, hpr)')
fx.load()

fx = FxList.new('tanh', 'tanh', {'tanh': 0}, order=2)
fx.add("osc = osc + (osc*tanh).tanh.sqrt()")
fx.load()

fx = FxList.new('tremolo', 'tremolo', {'tremolo': 0,
                                       'beat_dur': 1,
                                       'temolomix': 1}, order=2)
fx.add("osc = LinXFade2.ar(osc * SinOsc.ar(tremolo / beat_dur, mul: 0.5, add: 0.5), osc, 1-tremolomix)")
fx.load()

fx = FxList.new('trim', 'trim', {'trim': 0, 'sus': 1}, order=2)
fx.doc("Trimmer of sound from trim as position (old position) and sustain")
fx.add("osc = osc * EnvGen.ar(Env(levels: [0,0,1], curve: 'step', times: [sus * trim, 0]))")
fx.load()

fx = FxList.new('triode', 'triode', {'triode': 0}, order=2)
fx.doc("Tidal Effect: Triode Disto")
fx.add_var("sc")
fx.add("sc = triode * 10 + 1e-3")
fx.add("osc = (osc * (osc > 0)) + (tanh(osc * sc) / sc * (osc < 0))")
fx.add("osc = LeakDC.ar(osc) * 1.2")
fx.load()

fx = FxList.new("vib", "vibrato", {"vib": 0, "vibdepth": 0.02}, order=0)
fx.add("osc = Vibrato.ar(osc, vib, depth: vibdepth)")
fx.load()

fx = FxList.new('vol', 'vol', {'vol': 1}, order=2)
fx.doc("Simple Volume Control")
fx.add("osc = osc * vol")
fx.load()

if SC3_PLUGINS:
    fx = FxList.new('crush', 'crush', {'bits': 8,
                                       'sus': 1,
                                       'amp': 1,
                                       'crush': 0}, order=1)
    fx.add("osc = Decimator.ar(osc, rate: 44100/crush, bits: bits)")
    fx.add("osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2)")
    fx.load()

    fx = FxList.new('dist', 'dist', {'dist': 0, 'tmp': 0}, order=1)
    fx.add("tmp = osc")
    fx.add("osc = CrossoverDistortion.ar(osc, amp:0.2, smooth:0.01)")
    fx.add("osc = osc + (0.1 * dist * DynKlank.ar(`[[60,61,240,3000 + SinOsc.ar(62,mul:100)],nil,[0.1, 0.1, 0.05, 0.01]], osc))")
    fx.add("osc = (osc.cubed * 8).softclip * 0.5")
    fx.add("osc = SelectX.ar(dist, [tmp, osc])")
    fx.load()

In()
Out()
Effect.server.setFx(FxList)

''' New Effect template
fx = FxList.new('', '', {'': 0, '': 0}, order=2)
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.add("")
fx.load()
'''
