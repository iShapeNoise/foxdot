SynthDef.new(\easr, {
	|bus, a, s, r, ac, rc|
	var osc, env;
	osc = In.ar(bus, 2);
	env = EnvGen.ar(Env.new(levels: [0,1,1,0], times:[a*s, max((a*s + r*s), s - (a*s + r*s)), r*s], curve:[ac, 0, rc]));
	osc = osc * env;
	ReplaceOut.ar(bus, osc)
}).add;