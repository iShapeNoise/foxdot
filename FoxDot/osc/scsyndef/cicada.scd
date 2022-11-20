SynthDef.new(\cicada, {
	|amp=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, atk=0.01, dec=0.01, sus=1, rel=0.01, trig_freq=0.2|
	var osc, trig, demand, seq, vals, env;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	trig = Impulse.kr(trig_freq);
	vals = [[0.5, 128], [8, 6], [30, 3]];
	freq = TChoose.kr(trig, vals);
	osc = WhiteNoise.ar;
	osc = (osc - OnePole.ar(osc, exp(-2pi * (8000 * SampleDur.ir))));
	osc = (osc - OnePole.ar(osc, exp(-2pi * (8000 * SampleDur.ir))));
	osc = OnePole.ar(osc, exp(-2pi * (10000 * SampleDur.ir)));
	osc = OnePole.ar(osc, exp(-2pi * (10000 * SampleDur.ir)));
	osc = osc * 5;
	osc = BPF.ar(osc, [7500, 5500], 40.reciprocal).sum * SinOsc.ar(500);
	osc = osc * (1 / (SinOsc.ar(freq[0], 0, freq[1]).squared + 1));
	osc = (osc - OnePole.ar(osc, exp(-2pi * (4000 * SampleDur.ir)))) * 4.dup;
	osc = osc * amp;
	osc = Mix(osc) * 1;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "",
	modified_by: "",
	description: "",
	category: [],
	tags: []
)).add;