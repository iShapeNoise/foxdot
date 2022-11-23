SynthDef.new(\resonz, {
	|bus, resonz, rfreq|
	var osc;
	osc = In.ar(bus, 2);
	osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
	ReplaceOut.ar(bus, osc)
}).add;