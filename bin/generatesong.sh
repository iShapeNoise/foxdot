#!/bin/bash
java -cp /home/bbscar/Projects/Music/FoxDot_Dev/foxdot/lib/jchordbox.jar -Djcb.song.path=$JCBSONGPATH -Djcb.style.path=$JCBSTYLEPATH org.jchordbox.process.GenerateSong $@

