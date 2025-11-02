FoxDot - Live Coding with Python v0.9
=====================================


This branch of the original FoxDot is called PitchGlitch.
It is an attempt to continue to develop FoxDot ever more for Live Coding
and composing music.

---

FoxDot is a Python programming environment that provides a fast and user-friendly abstraction to SuperCollider. It also comes with its own IDE, which means it can be used straight out of the box; all you need is Python and SuperCollider and you're ready to go!

## Important

There is momentarily no pip package for this branch, so you will need to install
it via setup.py


### v0.9.13 branch "PitchGlitch"

New features:

- New editor based on [ttkBootstrap](https://ttkbootstrap.readthedocs.io/en/latest/) module
- Preferences section with theme editor
- Searchbar
- Treeview opens python scripts
- Midibar to show changing values according to LiveCoding rules
- MidiMapper (Maps Midi devices)
- SampleChart app now with progressbar

#### New functions:

- New MidiIn() functionality

For more info, please check Tutorial 16_midi_in_basics.py under Menu >> Help


### v0.8.12 branch "PitchGlitch"

Credits to CrashServer, KittyClock,  and others who provided many synths, fxs and other functions for this branch of FoxDot.

#### **SynthDefs:**

['loop', 'stretch', 'play1', 'play2', 'abass', 'acidbass', 'alva', 'ambi', 'angel', 'angst', 'arpy', 'audioin', 'bass', 'bassguitar', 'bbass', 'bchaos', 'bell', 'bellmod', 'benoit', 'birdy', 'blip', 'blips', 'bnoise', 'borgan', 'bounce', 'bphase', 'brass', 'brown', 'bug', 'charm', 'chimebell', 'chipsy', 'cicada', 'click', 'clip', 'cluster', 'combs', 'creep', 'cricket', 'crunch', 'cs80lead', 'dab', 'dafbass', 'dbass', 'dblbass', 'dirt', 'donk', 'donk1', 'donk2', 'donkysub', 'donorgan', 'dopple', 'drone', 'dub', 'dust', 'dustv', 'ebass', 'ecello', 'eeri', 'eoboe', 'epiano', 'faim', 'faim2', 'fbass', 'feel', 'filthysaw', 'flute', 'fm', 'fmbass', 'fmrhodes', 'four', 'fuzz', 'garfield', 'glass', 'glitchbass', 'glitcher', 'gong', 'grat', 'gray', 'growl', 'harp', 'hnoise', 'hoover', 'hydra', 'jbass', 'kalimba', 'karp', 'keys', 'klank', 'ladder', 'lapin', 'laserbeam', 'latoo', 'lazer', 'lfnoise', 'linesaw', 'longsaw', 'marimba', 'mhpad', 'mhping', 'moogbass', 'moogpluck', 'moogpluck2', 'noise', 'noisecomb', 'noisynth', 'noquarter', 'nylon', 'organ', 'organ2', 'orient', 'pads', 'pasha', 'pbass', 'phazer', 'piano', 'pianovel', 'pink', 'pluck', 'pmcrotal', 'ppad', 'prayerbell', 'prof', 'prophet', 'pulse', 'quin', 'radio', 'rave', 'razz', 'rhodes', 'rhpiano', 'ripple', 'risseto', 'rissetobell', 'rlead', 'rsaw', 'rsin', 'saw', 'sawbass', 'scatter', 'scrap', 'scratch', 'shore', 'sillyvoice', 'sine', 'sinepad', 'siren', 'sitar', 'snick', 'soft', 'soprano', 'sos', 'sosbell', 'space', 'spacesaw', 'spark', 'spick', 'sputter', 'square', 'squish', 'ssaw', 'star', 'steeldrum', 'strings', 'subbass', 'subbass2', 'supersaw', 'swell', 'tb303', 'total', 'tremsynth', 'tribell', 'tritri', 'triwave', 'tubularbell', 'twang', 'tworgan', 'tworgan2', 'tworgan3', 'tworgan4', 'varicelle', 'varsaw', 'vibass', 'video', 'vinsine', 'viola', 'virus', 'waves', 'windmaker', 'wobble', 'wobblebass', 'wsaw', 'wsawbass', 'xylophone', 'zap']

- - - - - -

#### **SynthDefs: Extra attributes**

| SynthDef |  Xtra Attributes   |
| ------------ | ------------ |
| acidbass  |  lagtime=0.12, frange=6 (filter range), width=0.51, rq=0.4   |
|  angel  | rq=0.5, cnoise=0.001 (clip noise), offnote=1.01  |
| benoit   | semione=12, semitwo=24, trackmul=2, width=0.17   |
|  blips | nharm=20, offnote=1.001   |
|  borgan | spread=0.8, lagtime=0.1   |
| bounce  | para1=2, para2=2.5, rel=0.09, nharm=3   |
|  bphase | pmindex=2   |
| chimebell  | rel=0.02, t60=8, offnote=1.001  |
|  chipsy | offnote=0.75, rel=0.009   |
| cicada  | trig_freq=0.2  |
| click  | mult=4, ptime=0.2  |
| cluster  |  para1=7, mult=4, pstep=0.75 |
| combs  |  rate=2, depth=0.8, regen= -3, sweep=8, rq=0.9, nharm=2 |
| cs60lead   | fatk=0.75, fdec=0.5, fsus=0.8, frel=1.0, cutoff=200, dtune=0.002, vibspeed=4, vibdepth=0.015, ratio=0.8, glide=0.15  |
| dafbass |  ffmod=1 (do not 0), level=0.8, peak=1, offnote=1.01 |
| dblbass  |  freqdev=4, op1mul=0.1, op2mul=0.1, op3mul=0.1, sprd=0.5, subAmp=0.1 |
| donkysub  | frate  |
|  donorgan | rel=0.5, lforate=9, lfowidth=0.01, cutoff=100, rq=0.5  |
|  dustv |  everbtime=3, roomdepth=8 |
| ebass  | pick=0.414, rq=0.5, cutoff=250  |
|  eoboe | range=0, vibrate=6, width=1, decimate=22040, decibits=2, offnote=1.005  |
|  feel |  offnote=1.005 |
|  filthysaw |  cf=100, t_bd=0, t_sd=0, pw=0.4 |
| flute  | ipress=0.9, ibreath=0.09, ifeedbk1=0.4, ifeedbk2=0.4  |
|  fmbass | atkfract=0.05, relfract= 0.7, modindex = 80, modratio = 1.51, subamp = 0.99, modfb = 1 fmrhodes >> vel = 0.8, modindex = 0.2, oscmix = 0.2, lfospeed = 0.4, lfodepth = 0.1  |
| garfield | phase=0, smooth=0.5, mult=3, vibrato=1, rq=1  |
| grat  | rlpf=4000 |
|  glitcher | len =20, henA=2, henB=0.4, t=1 |
| harp  | decaytime=7, coef=0.04, blend=0.7  |
| hoover  | rel=0.09, offnote=0.5  |
| kalimba  | oscmix=0.4, relMin=2.5, relMax=3.5  |
|  linesaw | lforate1 = 5, lfodepth1 = 0.25, phasecenter1 = 0.35, lforate2 = 2.7, lfodepth2 = 0.5, phasecenter2 = 0.5, pswitch = 0 (0 or 1), fdelay1 = 0.00025, fdelay2 = 0.00015  |
| mhpad  | vibrate = 4, vibdepth = 0.02, trem=3, tremdepth = 0.5  |
| mhping  |  depth=0.02|
| moogbass  |  cutoff = 1200, gain = 1.2, lagamount = 0.01, width=0.6 |
| moogpluck  | pluckfilter=4, pluckcoef=0.8, pluckmix=0.8  |
| moogpluck2  | level=0.8, legato=1, para1=0.5  |
|  pmcrotal | mod=5, atone=2, btone=4  |
| prayerbell  | decayscale=0.6, singswitch=0, lag=3  |
|  rhodes | rate=4.85, phase=0.5, cutoff=2000, rq=0.5  |
| rhpiano  | modindex=0.2, mix=0.2, lfospeed=0.4, lfodepth=0.1  |
| rlead  | bps=2, seqnote1=3, seqnote2=1, seqnote3=2  |
|  rsaw | lofreq = 800, hifreq = 4000 scatter >> level=0.8, offnote1=2, offnote2=1|
| shore  | noiselevel=0.1, density=100    |
|  sillyvoice | level=0.5, sinefb=0.2  |
|  sine | level=0.5, sinefb=0.2  |
| sosbell  |  ringamp=1, ringrel=0.9, wobbledepth=0.9, wobblemin=0.3, wobblemax=3.8, strikeamp=1, strikedec=0.05, strikerel=0.09, strikedepth=0.058, strikeharm=4, humamp=0.7|
| spacesaw |   filterlow=100, filterhigh=2000, rq=0.3, sidepreamp=2, midpreamp=1, lfofreq=0.1, lfodepth=0.015, balance=0.5 (0 to 1), monoswitch=0 (0 or 1) |
| sputter  |  pw = 0.5, noisedepth = 0.05, pwmrate = 12, pwmdepth = 0.15, rstartf = 2000, rlf = 500, rrf = 5000, ratk = 0.5, method = 0 (0 to 4), gateSwitch = 1 (0 to 1), gateThresh = 0.5 (0 to 1), stereoWidth = 0.75 (0 to 1) |
| squish  | xlatk=0.1, xlsus=0.01, xldur=1, xlmul=0.2, pulserate=4, pulsewidth=0.5 |
| steeldrum  | fharm=6, offnote=2.015  |
| strings  | freqlag = 0.9, rq = 0.012, combharm = 4, sawharm = 1.5  |
| subbass  | plpf=2400, plpr=1.0  |
|  subbass2 | plpf=2400, plpr=1.0  |
| supersaw | noiserate=0.5  |
| tb303  |  wave=0, ctf=100, res=0.2, top=1000 |
| tremsynth  | modfreq=3  |
| tribell  | lforate = 8, lfowidth = 0.02, cutoff = 80, rq = 0.05  |
|  triwave | lforate=3, lfowidth=0.0, cutoff=400, rq=0.7  |
| tubularbell   | exciterRel=0.05  |
| tworgan  |  qnt=1, fndmtl=1, nazard=1, bflute=1, trc=1, lrigot=1, sflute=1, vrate=3, vdepth=0.008, vdelay=0.1, vonset=0, vratevar=0.1, vdepthvar=0.1 |
| tworgan2  |  vibrate=6.0, vibharm=1.017, fharm=5.04, rq=1, blend=0.83 |
| tworgan3  | vrate=6, vdepth=0.02, vdelay=0.1, vonset=0, vratevar=0.1, vdepthvar=0.1, fharm=5.04, rq=1, blend=0.83  |
| tworgan4  | lforate=4.85, lfodepth=0.006, cutoff=5000, rq=0.5, parfreq=400, parrq=1, pardb=3, blend=0.6  |
|  varcell | cutoff=4800, noisemix=0.5, noiserate=12, xvib=2  |
| varsaw  | offnote=1.005  |
| vibass  |  vibrate=9 |
| vinsine  |  noiseamp=0.02, mainsdepth=0.35, mainshz = 50, vrate = 2, vdepth = 0.005, sineclip = 0.825 |
| windmaker  | cutoff=100, rq=0.1  |
| wobble  |modfreq=4, width=0.4   |
| wobblebass  | modfreqlo=1, modfreqhi=6, gate=1, wfmax=8500, reso=0.4, iphase=0.0, offnote1=0.98, offnote2=1.025  |
|  wsaw | iphase1=0.4, iphase2=0.5, iphase3=0.0, offnote1=1, offnote2=0.99, offnote3=1.005   |
| wsawbass   | slidetime = 0.08, cutoff = 1100, width = 0.15, detune = 1.002, preamp = 4  |
| xylophone |  t60=2 virus >> prate1=1, prate2=2, len=2 |

----

#### **SynthDefs: New functionalities**

<br>

- ***print(Player.get_fxs())*** >> Lists all filters and effects available for each SynthDef instrument.

  Example:

  ``` python
  print(Player.get_fxs())
  ```

  Output:

  ``` python
  ('bend', 'sus', 'benddelay', 'bpf', 'bpr', 'bpnoise', 'chop', 'chop2', 'chopmix', 'chopwave', 'chopi', 'chorus', 'chorusrate', 'coarse', 'comp', 'comp_down', 'comp_up', 'cut', 'dfm', 'dfmr', 'dfmd', 'dist2', 'dist2mix', 'dist2shape', 'djf', 'djfq', 'drive', 'drivemix', 'drop', 'dropof', 'a', 's', 'r', 'ac', 'rc', 'ehpf', 'ehpr', 'ehpa', 'ehps', 'ehpc', 'elpf', 'elpr', 'elpa', 'elps', 'elpc', 'eqlow', 'eqlowfreq', 'eqmid', 'eqmidfreq', 'eqmidq', 'eqhigh', 'eqhighfreq', 'echo', 'echomix', 'beat_dur', 'echotime', 'fdist', 'fdisfreq', 'fdistc', 'fdistcfreq1', 'fdistcfreq2', 'fdistcfreq3', 'fdistcfreq4', 'fdistcm1', 'fdistcm2', 'fdistcm3', 'fdistcm4', 'fdistcp1', 'fdistcp2', 'fdistcp3', 'fdistcp4', 'flanger', 'fdecay', 'flangermix', 'formant', 'formantmix', 'glide', 'glidedur', 'hpf', 'hpr', 'krush', 'kutoff', 'leg', 'lofi', 'lofiwow', 'lofiamp', 'minWowRate', 'maxDepth', 'lpf', 'lpr', 'mpf', 'mpr', 'octafuz', 'octamix', 'octer', 'octersub', 'octersubsub', 'output', 'phaser', 'phaserdepth', 'pong', 'pongtime', 'resonz', 'rfreq', 'pshift', 'ring', 'ringl', 'ringh', 'ringzfreq', 'ringz', 'room', 'mix', 'room2', 'mix2', 'damp2', 'revatk', 'revsus', 'sample_atk', 'sample_sus', 'shape', 'shapemix', 'shift', 'shiftsize', 'slide', 'slidedelay', 'slidefrom', 'spf', 'spr', 'spfslide', 'spfend', 'spin', 'squiz', 'striate', 'buf', 'rate', 'swell', 'tanh', 'tremolo', 'temolomix', 'trim', 'triode', 'vib', 'vibdepth', 'vol', 'bits', 'amp', 'crush', 'dist')
  ```

- ***print(Player(NAME_OF_SYNTH).get_extra_attributes)*** >> Lists all extra attributes of a particular SynthDef instrument.

  Example:

  ``` python
  print(Player('wobblebass').get_extra_attributes())
  ```

  Output:

  ``` python
  {'modfreqlo': '1', 'modfreqhi': '6', 'gate': '1', 'wfmax': '8500', 'reso': '0.4', 'iphase': '0.0', 'offnote1': '0.98', 'offnote2': '1.
  ```

----

#### ***Sample Player: sdb*** >> New attribute for a sample player SynthDef to easy switch between entire sample data bases.

<br>

  Example:

  ``` python
  b1 >> play(Z, dur=4, sample1, sdb=1, amplify=1/8)
  ```

  ***Hint: You can set your default number for a sample database in menu option Open Config File***

----

#### ***Midi: MidiIn+++*** >> Additional functionalities to MidiIn()

<br>

- Call MidiIn()

  ``` python
  midi = MidiIn()
  ```

- Check all available devices

  ``` python
  midi.device.get_ports()
  ```

- Enable midi message print

  ``` python
  midi.print_message(True)
  ```

- Select midi device

  ``` python
  midi = MidiIn(PORT)
  ```

- Get played midi note from keyboard

  ``` python
  midi.get_note()
  ```

- Get velocity of keyboard key or pad

  ``` python
  midi.get_velocity()
  ```

- Get value from controller like knobs

  ``` python
  midi.get_ctrl(MIDI_CHANNEL)
  ```

----

#### ***Midi: TempoTapper*** >> Implemented functionality for project TempoTapper

<br>

[Project: TempoTapper](https://jensmeisner.net/tempotapper/ "Project:")


- Check for TempoTapper device

  ```python
  midi = MidiIn()
  midi.device.get_ports()
  ```

- Setup TempoTapper device

  ``` python
  tempotap = MidiIn(PORT)
  tempotap.tempo_tapper(True)
  ```

- Update tempo clock with TempoTapper

  ``` python
  def updateBPM():
    Clock.bpm = tempotap.tempo_tapper_bpm()
    Clock.future(1, updateBPM)

  updateBPM()
  ```


----

  #### ***Help: Sample Charts App*** >> Sample Chart App in Menu > Help&Support

Sample Charts:

- Generates buttons for each sample in a chosen data base
- Plays the sound on press
- Shows a basic code example to copy/paste it into the FoxDot IDE


----


### v0.8 Updates

- Added `stretch` synth for timestretching samples, similar to `loop` but better and only plays the whole file. Stretches the audio's duration to the `sus` attribute without affecting pitch and does not require the tempo to be known.

```python
# Stretches the audio to 4 beats without affecting pitch
p1 >> stretch("Basic_Rock_135", dur=4)
```

---

## Installation and startup

#### Prerequisites
- [Python 2 or 3](https://www.python.org/) - add Python to your path and install "pip" when prompted during the install.
- [SuperCollider 3.8 and above](http://supercollider.github.io/download)
- [Tkinter](https://tkdocs.com/tutorial/install.html) - Usually packaged with Python but Linux and MacOS users may need to install using:
```bash
$ sudo apt-get install python3-tk (Linux)
$ sudo port install py-tkinter (MacOS)
```
#### Recommended
- [sc3 plugins](http://sc3-plugins.sourceforge.net/)

#### Installing FoxDot

- Open up a command prompt and type `pip install --user FoxDot`. This will download and install the latest stable version of FoxDot from the Python Package Index if you have properly configured Python.
- You can update FoxDot to the latest version if it's already installed by adding `-U` or `--upgrade` flag to this command.
- Alternatively, you can build from source from directly from this repository:
``` bash
$ git clone https://gitlab.com/iShapeNoise/FoxDot.git
$ cd FoxDot
$ python3 setup.py install
```
- Open SuperCollder and install the FoxDot Quark and its dependencies (this allows FoxDot to communicate with SuperCollider) by entering the following and pressing `Ctrl+Return` (Note: this requires [Git to be installed](http://git-scm.com/) on your machine if it is not already):
```supercollider
Quarks.install("FoxDot")
```
- Recompile the SuperCollider class library by going to `Language -> Recompile Class Library` or pressing `Ctrl+Shift+L`

#### Startup

1. Open SuperCollider and type in `FoxDot.start` and evaluate this line. SuperCollider is now listening for messages from FoxDot.
2. Start FoxDot by entering `FoxDot` at the command line. If that doesn't work, try `python -m FoxDot`.
3. If you have installed the SC3 Plugins, use the "Code" drop-down menu to select "Use SC3 Plugins". Restart FoxDot and you'll have access to classes found in the SC3 Plugins.
4. Keep up to date with the latest verion of FoxDot by running `pip install FoxDot --upgrade` every few weeks.
5. Check out the [YouTube tutorials](https://www.youtube.com/channel/UCRyrNX07lFcfRSymZEWwl6w) for some in-depth tutorial videos on getting to grips with FoxDot

#### Installing with SuperCollider 3.7 or earlier

If you are having trouble installing the FoxDot Quark in SuperCollider, it is usually because the version of SuperCollider you are installing doesn’t have the functionality for installing Quarks or it doesn’t work properly. If this is the case, you can download the contents of the following SuperCollider script: [foxdot.scd](http://foxdot.org/wp-content/uploads/foxdot.scd). Once downloaded, open the file in SuperCollider and press Ctrl+Return to run it. This will make SuperCollider start listening for messages from FoxDot.

#### Frequently Asked Questions

You can find answers to many frequently asked questions on the [FAQ post on the FoxDot discussion forum](http://foxdot.org/forum/?view=thread&id=1).

## Basics

### Executing Code

A 'block' of code in FoxDot is made up of consecutive lines of code with no empty lines. Pressing `Ctrl+Return` (or `Cmd+Return` on a Mac) will execute the block of code that the cursor is currently in. Try `print(1 + 1)` to see what happens!

### Player Objects

Python supports many different programming paradigms, including procedural and functional, but FoxDot implements a traditional object orientated approach with a little bit of cheating to make it easier to live code. A player object is what FoxDot uses to make music by assigning it a synth (the 'instrument' it will play) and some instructions, such as note pitches. All one and two character variable names are reserved for player objects at startup so, by default, the variables `a`, `bd`, and `p1` are 'empty' player objects. If you use one of these variables to store something else but want to use it as a player object again, or you  want to use a variable with more than two characters, you just have to reserve it by creating a `Player` and assigning it like so:

``` python
p1 = Player("p1") # The string name is optional
```

To stop a Player, use the `stop` method e.g. `p1.stop()`. If you want to stop all players, you can use the command `Clock.clear()` or the keyboard short-cut `Ctrl+.`, which executes this command.

Assigning synths and instructions to a player object is done using the double-arrow operator `>>`. So if you wanted to assign a synth to `p1` called 'pads' (execute `print(SynthDefs)` to see all available synths) you would use the following code:

``` python
p1 >> pads([0,1,2,3])
```

The empty player object, `p1` is now assigned a the 'pads' synth and some playback instructions. `p1` will play the first four notes of the default scale using a SuperCollider `SynthDef` with the name `\pads`. By default, each note lasts for 1 beat at 120 bpm. These defaults can be changed by specifying keyword arguments:

```python
p1 >> pads([0,1,2,3], dur=[1/4,3/4], sus=1, vib=4, scale=Scale.minor)
```

The keyword arguments `dur`, `oct`, and `scale` apply to all player objects - any others, such as `vib` in the above example, refer to keyword arguments in the corresponding `SynthDef`. The first argument, `degree`, does not have to be stated explicitly. Notes can be grouped together so that they are played simultaneously using round brackets, `()`. The sequence `[(0,2,4),1,2,3]` will play the the the first harmonic triad of the default scale followed by the next three notes.

### 'Sample Player' Objects

In FoxDot, sound files can be played through using a specific SynthDef called `play`. A player object that uses this SynthDef is referred to as a Sample Player object. Instead of specifying a list of numbers to generate notes, the Sample Player takes a string of characters (known as a "PlayString") as its first argument. To see a list of what samples are associated to what characters, use `print(Samples)`. To create a basic drum beat, you can execute the following line of code:

``` python
d1 >> play("x-o-")
```

To have samples play simultaneously, you can create a new 'Sample Player' object for some more complex patterns.

``` python
bd >> play("x( x)  ")
hh >> play("---[--]")
sn >> play("  o ")
```

Alternatively, you can do this in one line using `<>` arrows to separate patterns you want to play together like so:

```python
d1 >> play("<x( x)  ><---[--]><  o >")
```

Or you can use `PZip`, the `zip` method, or the `&` sign to create one pattern that does this. This can be useful if you want to perform some function on individual layers later on:

``` python
d1 >> play(P["x( x)  "].palindrome().zip("---[--]").zip(P["  o "].amen()))  

# The first item must be a P[] pattern, not a string.

d1 >> play(P["x( x)  "].palindrome() & "---[--]" & P["  o "].amen())
```

Grouping characters in round brackets laces the pattern so that on each play through of the sequence of samples, the next character in the group's sample is played. The sequence `(xo)---` would be played back as if it were entered `x---o---`. Using square brackets will force the enclosed samples to played in the same time span as a single character e.g. `--[--]` will play two hi-hat hits at a half beat then two at a quarter beat. You can play a random sample from a selection by using curly braces in your Play String like so:

``` python
d1 >> play("x-o{-[--]o[-o]}")
```

There is now the functionality to specify the sample number for an individual sample when using the `play` SynthDef. This can be done from the play string itself by using the bar character in the form `|<char><sample>|`. These can also be patterns created using brackets:

```python
# Plays the kick drum with sample 2 but the rest with sample 0
p1 >> play("|x2|-o-")

# You can use square brackets to play multiple samples
p1 >> play("|x[12]| o ")

# Round brackets alternate which sample is used on each loop through the sequence
p1 >> play("|x(12)| o ")

# Curly braces will pick a sample at random
p1 >> play("|x{0123}| o ")
```

## Scheduling Player methods

You can perform actions like shuffle, mirror, and rotate on Player Objects just by calling the appropriate method.

```python
bd >> play("x o  xo ")

# Shuffle the contents of bd
bd.shuffle()
```

You can schedule these methods by calling the `every` method, which takes a list of durations (in beats), the name of the method as a string, and any other arguments. The following syntax mirrors the string of sample characters after 6 beats, then again 2 beats  later and also shuffles it every 8 beats.

```python
bd >> play("x-o-[xx]-o(-[oo])").every([6,2], 'mirror').every(8, 'shuffle')
```

## Documentation

[Link to documentation website](https://foxdot.org/docs/) (still in progress)


## Running Python files with FoxDot code

You can import `FoxDot` into your own Python programs as you would any other module. If you are not writing an interactive program, i.e. only containing FoxDot code, then you need to call a function `Go()` at the end of your program to get playback otherwise the program will terminate immediately. For example your program, `my_file.py`, should look something like this:

```python
from FoxDot import *
p1 >> pads([0, 1, 2, 3])
d1 >> play("x-o-")
Go()
```

Then just run like any other Python program: `python my_file.py`

## Thanks

- The SuperCollider development community and, of course, James McCartney, its original developer
- PyOSC, Artem Baguinski et al
- Members of the Live Coding community who have contributed to the project in one way or another including, but not limited to, Alex McLean, Sean Cotterill, and Dan Hett.
- Big thanks to those who have used, tested, and submitted bugs, which have all helped improve FoxDot
- Thank you to those who have found solutions for SuperCollider related issues, such as DavidS48

### Samples

FoxDot's audio files have been obtained from a number of sources but I've lost record of which files are attributed to which original author. Here's a list of thanks for the unknowing creators of FoxDot's sample archive.

- [FoxDot_SampleDB_PitchGlitch](https://gitlab.com/iShapeNoise/foxdot_sampledb_pitchglitch)
- [Legowelt Sample Kits](https://awolfe.home.xs4all.nl/samples.html)
- [Game Boy Drum Kit](http://bedroomproducersblog.com/2015/04/08/game-boy-drum-kit/)
- A number of sounds courtesy of Mike Hodnick's live coded album, [Expedition](https://github.com/kindohm/expedition)
- Many samples have been obtained from http://freesound.org and have been placed in the public domain via the Creative Commons 0 License: http://creativecommons.org/publicdomain/zero/1.0/ - thank you to the original creators
- Other samples have come from the [Dirt Sample Engine](https://github.com/tidalcycles/Dirt-Samples/tree/c2db9a0dc4ffb911febc613cdb9726cae5175223) which is part of the TidalCycles live coding language created by Yaxu - another huge amount of thanks.

If you feel I've used a sample where I shouldn't have, please get in touch!


[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/iShapeNoise/foxdot)
