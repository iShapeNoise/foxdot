SynthDef.new(\resonz, {
	|bus, resonz, rfreq|
	var osc;
	osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
	ReplaceOut.ar(bus, osc)
}).add;