SynthDef.new(\eqhigh, {
	|bus, eqhigh, eqhighfreq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BHiShelf.ar(osc, freq: eqhighfreq, db: abs(eqhigh).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;