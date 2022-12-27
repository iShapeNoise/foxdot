SynthDef(\noisecomb, {
	|bus=0, pan=0, atk=0.3, sus=1, rel=0.8, fmod=0, freq=440, amp=1, noiselevel=0.8, minfreq=50, decaytime=0.5, ffreq=500, rq=0.4|
	var osc, clip, env;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	osc = WhiteNoise.ar(noiselevel);
	osc = osc + ClipNoise.ar(noiselevel);
	osc = osc + AllpassC.ar(osc, 1/minfreq, 1/freq, decaytime);
	osc = RLPF.ar(osc, ffreq * [6, 4, 5, 10, 1, 1.2, 0.8, 0.4, 2, 8 ], rq, amp);
	env = EnvGen.kr(Env.linen(atk, sus, rel, curve: 'sin'), levelBias: 0.1, timeScale: 1.5, doneAction: 0);
	osc = Mix(osc * env) * amp * 0.1;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
	},
metadata: (
	credit: "grirgz",
	modified_by: "Jens Meisner",
	description: "Electric Guitar Distorted",
	category: \category,
	tags: [\tag]
	)
).add;