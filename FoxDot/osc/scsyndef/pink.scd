SynthDef.new(\pink, {
	|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0, width=0.5, noise=0.4|
	var osc, env;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	osc = PinkNoise.ar(noise) + PulseDPW.ar(freq, width, mul: 0.2);
	env = EnvGen.ar(Env.new([1, 1], [1, 1]), doneAction: 0);
	osc = (osc * env * amp);
	osc = Mix(osc) * 0.4;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
	},
metadata: (
	credit: "CrashServer",
	modified_by: "Jens Meisner",
	description: "",
	category: \category,
	tags: [\tag]
	)
).add;
