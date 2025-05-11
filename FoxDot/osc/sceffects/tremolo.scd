SynthDef.new(\tremolo, {
	|bus, tremolo, tremolomix, beat_dur|
	var osc;
	osc = In.ar(bus, 2);
	osc = LinXFade2.ar(osc * SinOsc.ar(tremolo / beat_dur, mul: 0.5, add: 0.5), osc, 1-tremolomix);
	ReplaceOut.ar(bus, osc)
}).add;