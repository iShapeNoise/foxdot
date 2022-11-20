SynthDef.new(\cricket, {
	|amp=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, atk=0.01, dec=0.01, sus=1, rel=0.01|
	var osc1, osc2, osc3, osc, osc4, osc5, trig, demand, seq, env;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	osc1 = LFSaw.ar(1.43, 1, 0.5, 0.5);
    osc2 = (osc1 * 40.6 * 2pi).cos.squared;
	osc3 = osc1 * 3147 + freq;
	osc3 = (osc3 * 2pi).cos + ((osc3 * 2 * 2pi).cos * 0.3);
	osc = ((Wrap.ar(osc1.min(0.1714) * 5.84) - 0.5).squared * (-4) + 1) * (osc2 * osc3);
	trig = Impulse.kr(58.82);
	seq = Dseq(Array.fill(41, {|i| if(i<7, {(i+2)/9},{0}) }),inf);
	demand = Demand.kr(trig, 0, seq);
	env = EnvGen.ar(Env.new([0, 1, 0], [4/44100, 0]), trig, doneAction: 0) * demand;
	osc5 = OnePole.ar(env, exp(-2pi * (1000 * SampleDur.ir)));
	osc5 = (BPF.ar(osc5, 4500 + ((0..2)*50), 300.reciprocal, 100)).sum
		+ BPF.ar(osc5, 9000, 500.reciprocal, 42);
	osc5 = ((osc5 - OnePole.ar(osc5, exp(-2pi * (4000 * SampleDur.ir)))) * 0.5)!2;
	osc = (osc + osc5);
	osc = Mix(osc) * amp * 0.15;
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