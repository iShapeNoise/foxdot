SynthDef.new(\chop2, {
	|bus, chop2, sus, chopmix, chopwave, chopi|
	var osc;
	osc = In.ar(bus, 2);
	osc = LinXFade2.ar(osc * SelectX.kr(chopwave, [LFPulse.kr(chop2 / sus, iphase:chopi, add: 0.01), LFTri.kr(chop2 / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop2 / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop2 / sus, iphase:chopi, add: 0.01), LFPar.kr(chop2 / sus, iphase:chopi, add: 0.01)]), osc, 1-chopmix);
	ReplaceOut.ar(bus, osc)
}).add;