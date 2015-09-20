s.reboot;
ServerOptions.outDevices
Server.default.options.outDevice_("Built-in Output");

s.options.memSize;

(
var osc = {SinOsc.ar(0, 0, 0.2)}.play;
x = OSCFunc( { | msg, time, addr, port |
	var pyFreq;
	pyFreq = msg[1].asFloat;
	osc.release;

	// (msg[2]-5).postln;
	(pyFreq).postln;
   osc = { BPF.ar([WhiteNoise.ar(1,0), WhiteNoise.ar(1,0)],pyFreq,0.2,4,0) }.play;
}, '/print' );
)

"SC_JACK_DEFAULT_INPUTS".setenv("system:capture_1");
"SC_JACK_DEFAULT_OUTPUTS".setenv("system");

{SinOsc.ar(440,0,1,0)}.play;

SpectrogramWindow;


(

var osc = {SinOsc.ar(0, 0, 0.2)}.play;

x = OSCFunc( { | msg, time, addr, port |

	{
		var trig, note, son, sweep, mult = 1;
		var pyFreq;

		var x = MouseX.kr(40, 20000, 1);
		var roll_right = msg[1].asFloat;
	    var right_clench = msg[2].asFloat;
		var roll_left = msg[3].asFloat;

		(roll_right).postln;
		(right_clench).postln;
		(roll_left).postln;

		pyFreq = msg[1].asFloat;
		//pyFreq = 1000;

		trig = CoinGate.kr(0.5, Impulse.kr(2));
		//note = Demand.kr(trig, 0, Dseq((22,24..44).midicps.scramble, inf));
		sweep = LFPulse.ar(roll_right,0,0.5,5).exprange(40, 5000);
		son = LFSaw.ar(XLine.kr(x, x,0.11,1,0,2) * [0.99, 1, 1.01])+SinOsc.ar(XLine.kr(x, x,0.11,1,0,2)/4,0,1,0);
		//(pyFreq).postln;
		//son = LPF.ar(son, sweep);
		son = Normalizer.ar(son);
		son = son + BPF.ar(son, 2000, 2);
		//////// special flavours:
		// hi manster
		son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, 1000) * 4]);
		// sweep manster
		son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, sweep) * 4]);
		// decimate
		son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, son.round(0.1)]);
		son = (son * 5).tanh;
		son = son + GVerb.ar(son, 10, 0.1, 0.7, mul: 0.3);
		son = RLPF.ar(son,roll_left,9,right_clench,0);

	}.play;

}, '/print' )
)
​

{

var osc = {SinOsc.ar(0, 0, 0.2)}.play;
x = OSCFunc( { | msg, time, addr, port |
	var pyFreq;
	pyFreq = msg[1].asFloat;
	(pyFreq).postln;

	osc.release;

	var trig, note, son, sweep;
	     var x = MouseX.kr(40, 20000, 1);
	//var y = 100;
	// var y = MouseY.kr(60,1000, 1);
	    var roll_left = msg[1].asFloat;
	    var right_clench = msg[2].asFloat;
	    var roll_right = msg[3].asFloat;
	    (roll_right).postln;
        trig = CoinGate.kr(0.5, Impulse.kr(2));
        //note = Demand.kr(trig, 0, Dseq((22,24..44).midicps.scramble, inf));
        sweep = LFPulse.ar(roll_right,0,0.5,5).exprange(40, 5000);
	son = LFSaw.ar(x * [0.99, 1, 1.01])+SinOsc.ar(x/4,0,1,0);
        son = LPF.ar(son, sweep);
        son = Normalizer.ar(son);
        son = son + BPF.ar(son, 2000, 2);
        //////// special flavours:
        // hi manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, 1000) * 4]);
        // sweep manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, sweep) * 4]);
        // decimate
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, son.round(0.1)]);
        son = (son * 5).tanh;
        son = son + GVerb.ar(son, 10, 0.1, 0.7, mul: 0.3);
		osc = {RLPF.ar(son,roll_left,9,1,0)}.play;

		// osc = {BPF.ar([WhiteNoise.ar(1,0), WhiteNoise.ar(1,0)],pyFreq,0.2,4,0)}.play;
}, '/print' );
}


(
{
        var trig, note, son, sweep, mult = 1;
	     var x = MouseX.kr(40, 20000, 1);
	//var y = 100;
        var y = MouseY.kr(60,1000, 1);
        trig = CoinGate.kr(0.5, Impulse.kr(2));
        //note = Demand.kr(trig, 0, Dseq((22,24..44).midicps.scramble, inf));
        sweep = LFPulse.ar(2.33333,0,0.5,5).exprange(40, 5000);
	son = LFSaw.ar(y * [0.99, 1, 1.01])+SinOsc.ar(y/4,0,1,0);
        son = LPF.ar(son, sweep);
        son = Normalizer.ar(son);
        son = son + BPF.ar(son, 2000, 2);
        //////// special flavours:
        // hi manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, 1000) * 4]);
        // sweep manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, sweep) * 4]);
        // decimate
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, son.round(0.1)]);
        son = (son * 5).tanh;
        son = son + GVerb.ar(son, 10, 0.1, 0.7, mul: 0.3);
	    son = RLPF.ar(son,x,9,mult,0);
        son.dup
}.play
)



(
var osc = {SinOsc.ar(0, 0, 0.2)}.play;
x = OSCFunc( { | msg, time, addr, port |
	var pyFreq, trig, note, son, sweep;
	pyFreq = msg[1].asFloat;
	osc.release;
	// (msg[2]-5).postln;
	(pyFreq).postln;
	trig = CoinGate.kr(0.5, Impulse.kr(2));
	sweep = LFPulse.ar(2.33333,0,0.5,5).exprange(40, 5000);
	osc = {LFSaw.ar(XLine.kr(pyFreq, pyFreq,0.1,1,0,2),0,0.1)+SinOsc.ar(pyFreq/4,0,1,0,sweep)}.play;
	son = Normalizer.ar(son);
	//osc= {son+BPF.ar(son,2000,2)}.play;



	/*play({ SinOsc.ar(XLine.kr(pyFreq, pyFreq,0.1,1,0,2),0,0.1) });
	*/
	// osc = { BPF.ar([WhiteNoise.ar(1,0), WhiteNoise.ar(1,0)],pyFreq,0.2,4,0) }.play;
}, '/print' );
)


(
var osc = {SinOsc.ar(0, 0, 0.2)}.play;
x = OSCFunc( { | msg, time, addr, port |
    var pyFreq, trig, note, son, sweep, mult =1;
    pyFreq = 1000;
    osc.release;
    // (msg[2]-5).postln;
    (pyFreq).postln;
	 trig = CoinGate.kr(0.5, Impulse.kr(2));
    sweep = LFPulse.ar(2.33333,0,0.5,5).exprange(40, 5000);
    son = LFSaw.ar(1000 * [0.99, 1, 1.01])+SinOsc.ar(1000/4,0,1,0);
    (pyFreq).postln;
    son = LPF.ar(son, sweep);
    son = Normalizer.ar(son);
    son = son + BPF.ar(son, 2000, 2);
    //////// special flavours:
    // hi manster
    son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, 1000) * 4]);
    // sweep manster
    son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, sweep) * 4]);
    // decimate
    son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, son.round(0.1)]);
    son = (son * 5).tanh;
    osc = son + GVerb.ar(son, 10, 0.1, 0.7, mul: 0.3);
    //osc = {RLPF.ar(son,pyFreq-100,9,1,0)}.play;
    //osc = { BPF.ar([WhiteNoise.ar(1,0), WhiteNoise.ar(1,0)],pyFreq,0.2,4,0) }.play;
}, '/print' );
)



/*{
        var trig, note, son, sweep, mult = 1;
	     var x = MouseX.kr(40, 20000, 1);
	//var y = 100;
        var y = MouseY.kr(60,1000, 1);
        trig = CoinGate.kr(0.5, Impulse.kr(2));
        //note = Demand.kr(trig, 0, Dseq((22,24..44).midicps.scramble, inf));
        sweep = LFPulse.ar(2.33333,0,0.5,5).exprange(40, 5000);
	son = LFSaw.ar(y * [0.99, 1, 1.01])+SinOsc.ar(y/4,0,1,0);
        son = LPF.ar(son, sweep);
        son = Normalizer.ar(son);
        son = son + BPF.ar(son, 2000, 2);
        //////// special flavours:
        // hi manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, 1000) * 4]);
        // sweep manster
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, HPF.ar(son, sweep) * 4]);
        // decimate
        son = Select.ar(TRand.kr(trig: trig) < 0.05, [son, son.round(0.1)]);
        son = (son * 5).tanh;
        son = son + GVerb.ar(son, 10, 0.1, 0.7, mul: 0.3);
	    son = RLPF.ar(son,x,9,mult,0);
        son.dup
}.play*/




