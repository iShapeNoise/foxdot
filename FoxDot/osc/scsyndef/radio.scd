SynthDef.new(\radio, {
	|bus=0, freq=440, gate=1, amp=0.5, pan=0, fmod=0, atk=0.1, sus=1, rel=0.8, rate=1, sweep_min=20, sweep_max=11000|
	var env, hum, tuning, osc, numHarms;
	numHarms = 7;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	hum = Array.fill(numHarms, {|i| SinOsc.ar( (i+1) * freq, 0, 1/numHarms)});
	hum = hum.sum;
	osc = Dust.ar(LFNoise1.ar(1).range(1000, 8000), 0.2);
	osc = hum * osc * LFNoise1.ar(freq).range(0.5, 2);
	tuning = SinOsc.ar(10000).ring4(SinOsc.ar(LFNoise2.ar(1).range(sweep_min, sweep_max), mul:0.2)) * LFNoise2.ar(1.1).range(0.05, 0.1);
	env = EnvGen.ar(Env.asr(atk, sus, rel), gate, doneAction: 0);
	osc = osc + tuning;
	osc = Mix(osc) * amp * env * 0.5;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "CrashServer, jnarveson",
	modified_by: "Jens Meisner",
	description: "Radio tuning, frequency based noise, sine sweeping",
	category: \ambient,
	tags: [\tag]
	)
).add;