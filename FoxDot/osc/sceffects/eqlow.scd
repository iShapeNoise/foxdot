SynthDef.new(\eqlow, {
	|bus, eqlow, eqlowfreq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BLowShelf.ar(osc, freq: eqlowfreq, db: abs(eqlow).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;