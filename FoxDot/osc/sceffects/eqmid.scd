SynthDef.new(\eqmid, {
	|bus, eqmid, eqmidfreq, eqmidq|
	var osc;
	osc = In.ar(bus, 2);
	osc = BPeakEQ.ar(osc, freq: eqmidfreq, rq: eqmidq.reciprocal, db: abs(eqmid).ampdb);
	ReplaceOut.ar(bus, osc)
}).add;