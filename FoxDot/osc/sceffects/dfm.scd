SynthDef.new(\dfm, {
	|bus, dfm, dfmr, dfmd|
	var osc;
	osc = In.kr(bus, 1);
	osc = DFM1.ar(osc, dfm, dfmr, dfmd, 0.0);
	ReplaceOut.kr(bus, osc)
}).add;