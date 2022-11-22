SynthDef.new(\ring, {
	|bus, ring, ringl, ringh|
	var osc, mod;
	osc = In.ar(bus, 2);
	mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000));
	osc = ring1(osc, mod);
	ReplaceOut.ar(bus, osc)
}).add;