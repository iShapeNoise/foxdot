# -*- coding: latin-1 -*-
import math
import sys


def generateVoiceSpecification(lyrics, tempo, inputMusicXMLPath, outputMusicXMLPath):
	with open(inputMusicXMLPath, 'r') as c:
		content = [x.strip() for x in c.readlines()]
		with open(outputMusicXMLPath, 'w') as f:
			f.write(addVoiceTags(tempo, lyrics, content))


def addVoiceTags(tempo, text, content):
	output = ""
	tempo_xml = '<direction>\n<sound tempo="{}"/>\n</direction>'.format(tempo)
	lyrics_xml = '<voice>1</voice>\n<lyric>\n<text>{}</text>\n</lyric>'
	i = 0
	ignoreThisNote = False
	for line in content:
		if "<rest/>" in line:
			ignoreThisNote = True
		# for multiple notes connected by a tie, we don't want to start
		# a new word during the continuous note
		if "<tie type=\"stop\"/>" in line:
			ignoreThisNote = True
		if "</note" in line:
			if not ignoreThisNote:
				output += lyrics_xml.format(text[i%len(text)])
				i+=1
			else:
				ignoreThisNote = False
		output += line
		if tempo != -1 and "<measure" in line:
			output += tempo_xml
	return output
