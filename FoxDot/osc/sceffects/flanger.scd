SynthDef.new(\flanger, {
	|bus, flanger, fdecay, flangemix|
	var osc;
	osc = In.ar(bus, 2);
	osc = LinXFade2.ar(CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1),  osc, 1-flangermix);
	osc = osc + [left, right];
	ReplaceOut.ar(bus, osc)
}).add;