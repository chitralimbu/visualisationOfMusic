from music21 import *
import random
import re
import math
def read_mxl():
	mxl_file = converter.parse(r'C:\Users\Niku\Dropbox\\University\final_year_projet\The_legend_of_korra.mxl')
	#mxl_file.show('text')
	return mxl_file

def instruments_used(mxl_file):
	inst_used = []

	for i in mxl_file.parts:
		inst_used.append(i.id)
	#print(inst_used)
	return inst_used

def key_of_music(mxl_file):
	key = mxl_file.analyze('key').name
	#print(key)
	return key

def insertionSort(aList):
	allOffsets = allOffsetNotes()
	myReturn = aList
	#print(allOffsets[0])
	#print('\n')
	#print(myReturn[0])
	#print('\n')
	for i in range(len(allOffsets)):
			sortListOffset = allOffsets[i]
			toReturn = myReturn[i]
			for index in range(1, len(sortListOffset)):

				currentvalue = sortListOffset[index]
				returnValue = toReturn[index]
				position = index

				while position > 0 and sortListOffset[position-1] > currentvalue:
					sortListOffset[position] = sortListOffset[position -1]
					toReturn[position] = toReturn[position -1]
					position = position-1

				sortListOffset[position] = currentvalue
				toReturn[position] = returnValue
			myReturn[i] = toReturn
	#print('this is the sorted one')
	#print(allOffsets[0])
	#print(myReturn[0])
	return myReturn

def all_chords_used(mxl_file):
	instruments = instruments_used(mxl_file)
	chords = [[] for _ in range(len(instruments))]
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('Note'):
			chords[i].append(j.name)
		for k in inst.flat.getElementsByClass('Rest'):
			chords[i].append(k.name)
		for l in inst.flat.getElementsByClass('Chord'):
			for m in l.pitches:
				chords[i].append(note.Note(m).name)
	#print(len(chords[0]))
	#print(chords[0])

	"""
	print(chords[0])
	print('\n')
	print(len(chords[0]))
	print(chords[1])
	print('\n')
	print(len(chords[1]))
	print('\n')
	print(chords[2])
	print('\n')
	print(len(chords[2]))
	"""
	return chords

def allOffsetNotes():
	instruments = instruments_used(read_mxl())
	offset = [[] for _ in range(len(instruments))]
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('Note'):
			offset[i].append(int(j.offset))
		for k in inst.flat.getElementsByClass('Rest'):
			offset[i].append(int(k.offset))
		for l in inst.flat.getElementsByClass('Chord'):
			for m in l.pitches:
				offset[i].append(int(l.offset))
	#print(len(offset[0]))
	#print(offset[0])
	
	return offset

def sortedOffset():
	offsets = allOffsetNotes()
	newOffset = insertionSort(offsets)

	return newOffset

def allpitchesNotes():
	instruments = instruments_used(read_mxl())
	pitch = [[] for _ in range(len(instruments))]
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('Note'):
			pitch[i].append(int(j.pitch.frequency))
		for k in inst.flat.getElementsByClass('Rest'):
			pitch[i].append(k.name)
		for l in inst.flat.getElementsByClass('Chord'):
			for m in l.pitches:
				pitch[i].append(int(m.frequency))

	#print(len(pitch[0]))
	#print(pitch[0])
	newPitch = insertionSort(pitch)
	#print(len(newPitch[0]))
	#print(newPitch)
	return newPitch

def allNoteTypes():
	instruments = instruments_used(read_mxl())
	noteType = [[] for _ in range(len(instruments))]
	toNumber = [[] for _ in range(len(noteType))]

	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('Note'):
			noteType[i].append(float(j.duration.quarterLength))
		for k in inst.flat.getElementsByClass('Rest'):
			noteType[i].append(float(k.duration.quarterLength))
		for l in inst.flat.getElementsByClass('Chord'):
			for m in l.pitches:
				noteType[i].append(float(l.duration.quarterLength))
	#print(noteType)
	
	"""for i in range(len(noteType)):
		myinput = noteType[i]
		for j in range(len(myinput)):
			print(myinput[j])
			toNumber[i].append(calculateDots(myinput[j]))
	"""
	#print(toNumber)
	#print(len(offset[0]))
	#print(offset[0])
	#print(toNumber[0])
	newNoteType = insertionSort(noteType)
	#print(newNoteType)
	return newNoteType
def allClefs():
	instruments = instruments_used(read_mxl())
	mySelection = [[] for _ in range(len(instruments))]
	signLines = [[] for _ in range(2)]

	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('Clef'):
			signLines[0].append(j.sign)
			signLines[1].append(j.line)
	#print(signLines[0])
	return signLines


def keyOfInstrument(mxl_file):
	instruments = instruments_used(mxl_file)
	key = []
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		key.append(inst.analyze('key').name)
	#print('\n')
	#print(key)
	return key

def getMax(arr):
	temp = 0
	for i in arr:
		if i == 'rest':
			continue
		if i > temp:
			temp = i
	return temp

def getMin(arr):
	temp = arr[0]
	for i in arr:
		temp = i
		if i == 'rest':
			continue
		if i < temp:
			temp = i
	return temp

def get_measure_offset():
	instruments = instruments_used(read_mxl())
	measure_offset = [[] for _ in range(len(instruments))]

	for i in range(len(instruments)):
	 	inst = read_mxl().getElementById(instruments[i])
	 	for j in inst.measures(1,None):
	 		measure_offset[i].append(j.offset)
	#print('\n')
	"""
	print(measure_offset[0])
	print('\n')
	print(len(measure_offset[0]))
	print(measure_offset[1])
	print('\n')
	print(len(measure_offset[1]))
	print('\n')
	"""	
	#print('measure offset')
	#print(measure_offset[0])
	#print('\n')
	#print(len(measure_offset[0]))

	return measure_offset

def metronomeMark():
	instruments = instruments_used(read_mxl())
	metAsString = []
	metOffset = []
	metBPM = []
	storeAll = [[] for _ in range(2)]
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.getElementsByClass('MetronomeMark'):
			metAsString.append(str(j))
			temp = j.offset
			metOffset.append(int(round(temp)))

	for i in metAsString:
		mySplit = i.split("=", 1)
		splitAgain = mySplit[-1].split(">",1)
		toInt = int(float(splitAgain[0]))
		metBPM.append(toInt)
	storeAll[0] = metBPM
	storeAll[1] = metOffset

	#print(storeAll)
	#print(metAsString)
	return storeAll
	#print(instruments)

def formulaDots(noteType, typeDot):
	finalDuration = noteType * (2- (1/(math.pow(2, typeDot))))
	#print(finalDuration)
	return finalDuration

def calculateDots(noteType):
	durationNumber = [4.0,2.0,1.0,0.5,0.25,0.125, 0.0625, 0.03125]
	duration_type = ['whole','half','quarter','eighth','16th','32nd','64th', '128th']
	dotType = ['none','dotted','double','triple']
	toArray = re.compile('\w+').findall(noteType.lower())
	
	if len(toArray) > 1:
		for i in range(len(duration_type)):
			if toArray[-1] == duration_type[i]:
				toNumber = durationNumber[i]
		for i in range(len(dotType)):
			if toArray[0] == dotType[i]:
				typeDot = i
		finalNumber = formulaDots(int(toNumber), int(typeDot))
	if len(toArray) == 1:
		for i in range(len(duration_type)):
			if toArray[-1] == duration_type[i]:
				toNumber = durationNumber[i]
				print(toNumber)
		finalNumber = toNumber
	return finalNumber



##########===================OF NO MORE USE=========================#######
def pitchesForChords(mxl_file):
	instruments = instruments_used(mxl_file)
	allChords = all_chords_used(mxl_file)
	pitches = [[] for _ in range(len(instruments))]
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.notesAndRests:
			if j.name == 'rest' or j.name == 'Rest':
				pitches[i].append(j.name)
				continue
			else:
				pitches[i].append(int(j.pitch.frequency))
			"""
	print('\n')
	print(pitches[0])
	print('\n')
	print(len(pitches[0]))
	print(pitches[1])
	print('\n')
	print(len(pitches[1]))
	"""
	#print('chords and pitches')
	"""
	print('\n')
	print(allChords[0])
	print('\n')
	print(len(allChords[0]))
	print('\n')
	print(pitches[0])
	print('\n')
	print(len(pitches[0]))
	print('\n')
	print(getMin(pitches[0]))
	"""
	return pitches		

def get_note_type():
	instruments = instruments_used(read_mxl())
	note_type = [[] for _ in range(len(instruments))]
	toNumber = [[] for _ in range(len(note_type))]

	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst.flat.notesAndRests:
			note_type[i].append(j.duration.fullName)
	#convert to number
	for i in range(len(note_type)):
		myinput = note_type[i]
		for j in range(len(myinput)):
			#print(myinput[j])
			toNumber[i].append(calculateDots(myinput[j]))
	"""
	print('\n')
	print(note_type[0])
	print('\n')
	print(len(note_type[0]))
	print(note_type[1])
	print('\n')
	print(len(note_type[1]))
	print('\n')
	"""
	"""
	print('note_type_number')
	print(toNumber[0])
	print('\n')
	print(len(toNumber[0]))
	print('note_type')
	print(note_type[0])
	print('\n')
	print(len(note_type[0]))
	"""
	return toNumber

def gettingClef():
	clefs = ['TrebleClef','BassClef','AltoClef','Bass8vaClef','Bass8vbClef','CBaritoneClef','CClef','FBaritoneClef','FClef','FrenchViolinClef','GClef','GSopranoClef','MezzoSopranoClef','NoClef','PercussionClef','PitchClef','SopranoClef','SubBassClef','TabClef','TenorClef','Treble8vaClef','Treble8vbClef']
	music21Clef = ['<music21.clef.TrebleClef>','<music21.clef.BassClef>','<music21.clef.AltoClef>','<music21.clef.Bass8vaClef>','<music21.clef.Bass8vbClef>','<music21.clef.CBaritoneClef>','<music21.clef.CClef>','<music21.clef.FBaritoneClef>','<music21.clef.FClef>','<music21.clef.FrenchViolinClef>','<music21.clef.GClef>','<music21.clef.GSopranoClef>','<music21.clef.MezzoSopranoClef>','<music21.clef.NoClef>','<music21.clef.PercussionClef>','<music21.clef.PitchClef>','<music21.clef.SopranoClef>','<music21.clef.SubBassClef>','<music21.clef.TabClef>','<music21.clef.TenorClef>','<music21.clef.Treble8vaClef>','<music21.clef.Treble8vbClef>']
	instruments = instruments_used(read_mxl())

	mySelection = [[] for _ in range(len(instruments))]

	clefsOfInst = []

	signLines = [[] for _ in range(2)]
	
	for i in range(len(instruments)):
		inst = read_mxl().getElementById(instruments[i])
		for j in inst[1]:
			mypick = j
			k = str(mypick)
			mySelection[i].append(k)
	for i in mySelection:
		for j in range(len(i)):
			for k in range(len(music21Clef)):
				if i[j] == music21Clef[k]:
					clefsOfInst.append(clefs[k])
	signs = []
	lines = []
	for i in clefsOfInst:
		myattr = getattr(clef, i)()
		signs.append(myattr.sign)
		if i.find('8va') != -1:
			higherPitch = myattr.line
			lines.append(higherPitch - 1)
		if i.find('8vb') != -1:
			lowerPitch = myattr.line
			lines.append(lowerPitch +1)
		else:
			lines.append(myattr.line)

	signLines[0] = signs
	signLines[1] = lines

	#print(clefsOfInst)
	#print(signs)

	#print(lines)
	
	#print(signLines)
	return signLines
####################==========OF NO MORE USE ==================#########

#key_of_music(read_mxl())
#all_chords_used(read_mxl())
#instruments_used(read_mxl())
#keyOfInstrument(read_mxl())
#pitchesForChords(read_mxl())
#get_note_type()
#get_measure_offset())
#gettingClef()
#metronomeMark()
#all_chords_used(read_mxl())
#allOffsetNotes()
allpitchesNotes()
#allClefs()
#allNoteTypes()
#insertionSort(allNoteTypes())