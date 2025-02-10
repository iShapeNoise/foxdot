from __future__ import absolute_import, print_function

from .MidiFactory import createMidi
import os
from math import ceil


def extendScale(scale, times):
    scaleAux = scale[:]
    for i in range(1, times):
        for note in scaleAux:
            scale.append(note+12*i)
    return scale


def matchListsSize(rhythm, melody):
    n_rhythm = len(rhythm)
    n_melody = len(melody)
    if n_rhythm < n_melody:
        rhythm = (rhythm*int(ceil(n_melody/float(n_rhythm))))[:n_melody]
    elif n_rhythm != n_melody:
        melody = (melody*int(ceil(n_rhythm/float(n_melody))))[:n_rhythm]
    return rhythm, melody


def toList(rhythm, melody, scale):
    scale = extendScale(scale, 2)
    scaleSize = len(scale)
    volume = 100
    baseNote = 60
    rhythm, melody = matchListsSize(rhythm, melody)
    composition = []
    time = 0
    for i in range(len(rhythm)):
        dur = rhythm[i]
        note = scale[melody[i] % scaleSize] + baseNote
        composition.append((note, dur, volume, time))
        time += dur
    return composition


def compose(notes, durations, scale, new_midi_path, new_musicxml_path):
    print('notes: ', notes)
    print('durations: ', durations)
    print('scale: ', scale)
    composition = toList(durations, notes, scale)
    print("Composition: ", composition)
    createMidi(new_midi_path, composition)
    # uses MuseCore to onvert midi file to musicXML file
    from sys import platform
    # linux
    if platform == "linux" or platform == "linux2":
        os.system("musescore " + new_midi_path + " -o " + new_musicxml_path)
    # OS X
    elif platform == "darwin":
        os.system("/Applications/MuseScore\ 3.app/Contents/MacOS/mscore " + new_midi_path + " -o " + new_musicxml_path)
    # Windows...
    elif platform == "win32":
        os.system("musescore " + new_midi_path + " -o " + new_musicxml_path)
