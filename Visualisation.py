from Extracting_musical_information import *
import pygame
import math
import colorsys
import difflib
pygame.init()

"""
instrumentUsed = instruments_used(read_mxl())
keyOfMusic = key_of_music(read_mxl())
pitchesOfChords = pitchesForChords(read_mxl())
durationOfNote = get_note_type()
measureOffset = get_measure_offset()
clefs = gettingClef()
"""
#functions here =========================================
#get max pitches (total height of image)
def maxHeight():
	noOfInst = len(instruments_used(read_mxl()))
	selected = []
	for i in allpitchesNotes():
		selected.append(getMax(i))
	maximHeight = (max(selected)/ 10) * len(instruments_used(read_mxl()))
	#print(maximHeight)

	return maximHeight

def maxLength():
	offsets = get_measure_offset()
	noteDuration = allNoteTypes()
	#print(noteDuration)
	noteSelect = []
	maxim = 0
	for i in noteDuration:
		noteSelect.append(i[-1])
	selected = []
	for i in offsets:
		selected.append(getMax(i))
	maximLength = ((max(selected)  * 5) )
	#print(noteSelect)
	#print(maximLength)
	return maximLength		
	#toArray = re.compile('\w+').findall(noteType.lower())

def getRGB(re, gr, bl, metOne, metTwo):
	red = re
	green = gr
	blue = bl
	print('red', 'green', 'blue')
	print(red, green, blue)
	RGB = []
	bpmDiff = int((round(metTwo - metOne, -1))/10)

	if float(red) == 0.0:
		myRed = 1.22
		#print(myRed)
	else:
		myRed = red
	if float(blue) == 0.0:
		myBlue = 2.15
	else:
		myBlue = blue
	if float(green) == 0.0:
		myGreen = 2.53
	else:
		myGreen = green
	print('bpmDiff')
	print(bpmDiff)
	if bpmDiff >0:
		r = int(round(float(myRed) * math.pow(1.22, abs(float(bpmDiff)))))
		g = int(round(float(myGreen) * math.pow(2.53, abs(float(bpmDiff)))))
		b = int(round(float(myBlue) * math.pow(2.15, abs(float(bpmDiff)))))
	if bpmDiff <= 0:
		r = int(round(float(myRed) / math.pow(1.22, abs(float(bpmDiff)))))
		g = int(round(float(myGreen) / math.pow(2.53, abs(float(bpmDiff)))))
		b = int(round(float(myBlue) / math.pow(2.15, abs(float(bpmDiff)))))
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255 
	RGB.append(r)
	RGB.append(g)
	RGB.append(b)

	#lightness conversion
	#print(RGB)
	return RGB

def measures():
	measures = get_measure_offset()
	measure_offset = [[] for _ in range(len(measures))]
	total_height = maxHeight() / len(instruments_used(read_mxl()))
	heightOfMeasure = total_height / len(measures)
	#print(heightOfMeasure)
	yval = total_height / 2
	#print(yval)
	for i in range(len(measures)):
		temp_array = measures[i]
		for j in temp_array:
			measure_offset[i].append(j*5)
	for a in range(len(measure_offset)):
		my_temp = measure_offset[a]
		for d in range(len(measures)):
			for c in my_temp:
				pygame.draw.rect(visualDisplay, white, [c, yval, 1, heightOfMeasure], 1)
			yval += total_height
	#print(measures)
	#print(measure_offset)
	return measure_offset

def calculatePitches():
	pitchesOfChords = allpitchesNotes()
	actualPitches = [[] for _ in range(len(pitchesOfChords))]
	for j in range(len(pitchesOfChords)):
		tempArrray = pitchesOfChords[j]
		for k in tempArrray:
			if k == 'rest':
				actualPitches[j].append(k)
				continue
			if k != 'rest':
				actualPitches[j].append(int(round((k / 10), 0)))
	#print(actualPitches)
	return actualPitches

def durationOfnote():
	durationNote = allNoteTypes()
	actualDuration = [[] for _ in range(len(durationNote))]

	for i in range(len(durationNote)):
		tempDuration = durationNote[i]
		for j in tempDuration:
			actualDuration[i].append(int(round(j * 5)))

	return actualDuration

def keysAndColour(theKey):
	overAll = theKey
	instKeys = keyOfInstrument(read_mxl())
	keys = ['C major','G Major','E major','F# major','G- major','F major','E- major','A- major','D- major','C minor','G minor','D minor','F# minor','B- minor']
	colours = ['white','green','orange','red','blue','brown','skyblue','mauve','purple','gray','silver','sand_colour','light_red','black']
	toReturn = [[] for _ in range(2)]
	greatest = 0
	for j in range(len(keys)):
		a = overAll
		b = keys[j]
		seq = difflib.SequenceMatcher(a=a.lower(), b = b.lower())
		ratio = seq.ratio()
		#print(b)
		#print('ratio')
		#print(ratio)
		if ratio >= greatest:
			greatest = ratio
			index = j
	chosen = keys[index]
	
	#print('chosen')
	#print(chosen)
	
	chosenColor = colours[index]
	
	#print('chosenColor')
	#print(chosenColor)
	#print('greatest')
	#print(greatest)
	
	if int(greatest) == 1.0:
		toReturn[0].append(chosenColor)
		toReturn[1].append(0)

	if int(greatest) < 1.0:
		actualChar = overAll[1]
		selectChar = chosen[1]
		if actualChar == '-' and selectChar == '-':
			toReturn[0].append(chosenColor)
			toReturn[1].append(0)
		if actualChar == '#' and selectChar == '#':
			toReturn[0].append(chosenColor)
			toReturn[1].append(0)
		if actualChar == ' ' and selectChar == ' ':
			toReturn[0].append(chosenColor)
			toReturn[1].append(0)
		if actualChar == ' ' and selectChar == '#':
			toReturn[0].append(chosenColor)
			toReturn[1].append(1)
		if actualChar == ' ' and selectChar == '-':
			toReturn[0].append(chosenColor)
			toReturn[1].append(-1)
		if actualChar == '-' and selectChar == '#':
			toReturn[0].append(chosenColor)
			toReturn[1].append(2)
		if actualChar == '#' and selectChar == '-':
			toReturn[0].append(chosenColor)
			toReturn[1].append(-2)
		if actualChar == '#' and selectChar == ' ':
			toReturn[0].append(chosenColor)
			toReturn[1].append(-1)
		if actualChar == '-' and selectChar == ' ':
			toReturn[0].append(chosenColor)
			toReturn[1].append(1)

	#print(len(colours))
	#print(len(keys))
	#print(index)
	#print('toReturn')
	#print(toReturn)
	return toReturn

def colourOfKey():
	colour = ['white','green','orange','red','blue','brown','skyblue','mauve','purple','gray','silver','sand_colour','light_red','black']
	red = ['255','0','255','255','0','165','135','204','128','128','192','194','255','0'] 
	green = ['255','255','165','0','0','42','206','153','0','128','192','178','77','0']
	blue = ['255','0','0','0','255','42','235','255','128','128','192','128','77','0']
	RGB = []
	instKeys = keyOfInstrument(read_mxl())
	#print(instKeys)
	toAverage = [[] for _ in range(3)]
	"""
	getKey = keysAndColour(instKeys[0])
	print(getKey)
	select = getKey[0]
	print(select[0])

	print(select[0] == colour[13])
	"""
	total_red = 0
	total_green = 0
	total_blue = 0
	final_red = 0
	final_green = 0
	final_blue = 0
	#print(instKeys)
	for i in range(len(instKeys)):
		getKey = keysAndColour(instKeys[i])
		#print('getKey')
		#print(getKey)
		select = getKey[0]
		#print('select')
		#print(select)
		color = select[0]
		toMul = getKey[1]
		multiply = toMul[0]
		#print(color)
		for j in range(len(colour)):
			if color == colour[j]:
				r = int(red[j])
				g = int(green[j])
				b = int(blue[j])

				if multiply == 0:
					r = r
					g = g
					b = b
				if multiply == 1:
					r = r / 0.61
					g = g / 0.99
					b = b / 2.17
				if multiply == -1:
					r = r * 0.61
					g = g * 0.99
					b = b * 2.17
				if multiply == 2:
					r = r / math.pow(0.61, 2)
					g = g / math.pow(0.99, 2)
					b = b / math.pow(2.17, 2)
				if multiply == -2:
					r = r * math.pow(0.61, 2)
					g = g * math.pow(0.99, 2)
					b = b * math.pow(2.17, 2)
				
				if r > 255:
					r = 255
				if g > 255:
					g = 255
				if b > 255:
					b = 255
				toAverage[0].append(int(round(r)))
				toAverage[1].append(int(round(g)))
				toAverage[2].append(int(round(b)))
	
	#print(toAverage)
	"""
				total_red = total_red + r
				total_green = total_green + g
				total_blue = total_blue + b

	total_red = int((round(total_red / len(instKeys))))
	total_green = int((round(total_green / len(instKeys))))
	total_blue = int((round(total_blue / len(instKeys))))

	print(len(instKeys))
	if total_red > 255:
		total_red = 255
	if total_green > 255:
		total_green = 255
	if total_blue > 255:
		total_blue = 255

	RGB.append(total_red)
	RGB.append(total_green)
	RGB.append(total_blue)
	"""
	return toAverage
					
def overallColour(toAverage):
	myRGB = toAverage
	instKeys = keyOfInstrument(read_mxl())

	finalSum = []
	sumRed = sum(myRGB[0]) / len(instKeys)
	sumGreen = sum(myRGB[1]) / len(instKeys)
	sumBlue = sum(myRGB[2]) / len(instKeys)

	if sumRed > 255:
		sumRed = 255
	if sumGreen > 255:
		sumGreen = 255
	if sumBlue > 255:
		sumBlue = 255
	finalSum.append(int(round(sumRed)))
	finalSum.append(int(round(sumGreen)))
	finalSum.append(int(round(sumBlue)))

	#print(finalSum)
	return finalSum

def rectangle(xval, yval, instPart, color, shapeW, lineSize):

	pygame.draw.rect(visualDisplay, color, [xval, (0 + instPart +yval), shapeW, shapeW], lineSize)

def circle(color, xval, yval, instPart, theRad, lineSize):
	pygame.draw.circle(visualDisplay, color, [xval, (0 + instPart) + yval], theRad, lineSize)

def diamond(color, xval, yval, instPart, theSize, lineSize):
	#(a,b), (c,d), (e,f) (g,h)
	polyp = (xval + (theSize / 2) , yval + instPart - (theSize/ 2)), (xval  + theSize, yval + instPart), (xval + (theSize/2), yval + instPart+(theSize/2)),(xval , yval + instPart) 
	
	pygame.draw.polygon(visualDisplay, color, polyp, lineSize)

def drawShapes():
	 duration = durationOfnote()
	 allColourKyes = colourOfKey()
	 pitches = calculatePitches()
	 instKeys = keyOfInstrument(read_mxl())
	 total_height = int(maxHeight() / len(instruments_used(read_mxl())))
	 clefsSignsAndLines = allClefs()
	 clefsOnly = clefsSignsAndLines[0]
	 #print('clefs Only')
	 #print(clefsOnly)
	 linesOnly = clefsSignsAndLines[1]
	 instPart = 0
	 myColour = 'green'
	 anotherColour = 'mauve'
	 anoColour = 'indigo'
	 myMetronome = metronomeMark()
	 myBPM = myMetronome[0]
	 myMetOffset = []
	 for i in myMetronome[1]:
	 	myMetOffset.append(i * 5)
	 #print('my met offset')
	 #print(len(myMetOffset))
	 #print(myMetOffset)


	 #print(pitches[-1])
	 #print('\n')
	 #print(pitches[0])
	 r = 0
	 g = 0
	 b = 0
	 for i in range(len(pitches)):
	 	tempDuration = duration[i]
	 	tempPitches = pitches[i]
	 	currentClef = clefsOnly[i]
	 	totDuration = 0
	 	if len(myMetOffset) == 1:
	 		myCounter = 0
	 	else:
	 		myCounter = 1
	 	for j in range(len(tempDuration)):
	 		if tempDuration[j] == 20 or tempDuration[j] == 10:
	 			line = 1
	 		else:
	 			line = 0
	 		if tempPitches[j] != 'rest':
	 			myRed = allColourKyes[0]
	 			myGreen = allColourKyes[1]
	 			myBlue = allColourKyes[2]
	 			print('myMetOffset')
	 			print(myMetOffset)
	 			for i in range(len(instKeys)):
	 				if instPart == (total_height * i):
	 					r = myRed[i]
	 					g = myGreen[i]
	 					b = myBlue[i]
	 			if currentClef == 'G':
	 				bpmOffset = myMetOffset[myCounter]
	 				
	 				print('myCounter')
	 				print(myCounter)
	 				print('bpmOffset')
	 				print(bpmOffset)
	 				print('myBPM[myCounter -1]')
	 				print(myBPM[myCounter -1])
	 				print('myBPM[myCounter]')
	 				print(myBPM[myCounter])
	 				
	 				gettingColor = getRGB(r,g,b, myBPM[myCounter -1], myBPM[myCounter])
	 				color = (gettingColor[0], gettingColor[1], gettingColor[2])
	 				rectangle(totDuration, tempPitches[j],instPart, color, tempDuration[j],line)

	 				if totDuration >= bpmOffset and myCounter < (len(myBPM) -1):
	 					myCounter+=1
	 				totDuration+=tempDuration[j]

	 			if currentClef == 'F':
	 				bpmOffset = myMetOffset[myCounter]
	 				gettingColor = getRGB(r,g,b, myBPM[myCounter -1], myBPM[myCounter])
	 				color = (gettingColor[0], gettingColor[1], gettingColor[2])
	 				circle(color, totDuration, tempPitches[j],instPart,tempDuration[j],line)
	 				if totDuration >= bpmOffset and myCounter < (len(myBPM) -1):
	 					myCounter+=1
	 				totDuration+=tempDuration[j]
	 			"""
	 			diamond(color, xval, yval, instPart, theSize, lineSize):
				polyp = (1 + theSize + xval + 50, 0 + theSize + yval + instPart),(2+ theSize   + xval + 50,1+ theSize  + yval + instPart),(1+ theSize   + xval + 50,2+ theSize  + yval + instPart),(0+ theSize   + xval + 50,1+ theSize  + yval + instPart)
	 			"""

	 			if currentClef == 'C':
	 				bpmOffset = myMetOffset[myCounter]
	 				gettingColor = getRGB(r,g,b, myBPM[myCounter -1], myBPM[myCounter])
	 				color = (gettingColor[0], gettingColor[1], gettingColor[2])
	 				diamond(color, totDuration, tempPitches[j], instPart, tempDuration[j],line)
	 				if totDuration >= bpmOffset and myCounter < (len(myBPM) -1):
	 					myCounter+=1
	 				totDuration+=tempDuration[j]
	 		if tempPitches[j] == 'rest':
	 			totDuration+=tempDuration[i]
	 			continue
	 		#########end colour instrument key loop
	 	#print(gettingColor)
	 	instPart +=total_height

#getRGB('black', 26,50)
#metronomeMark()
#drawShapes()
#durationOfnote()
#measures()
#maxLength()
#def circle():
#keysAndColour()
#colourOfKey()
#overallColour(colourOfKey())
#def diamond():

white = (255,255,255)
black = (0,0,0)

keyColour = overallColour(colourOfKey())

finalKeyColour = (keyColour[0], keyColour[1], keyColour[2])

display_height = int(maxHeight())
display_width = int(maxLength())

visualDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('visualisation')
clock = pygame.time.Clock()

def mainKey(thingh, color):
	pygame.draw.rect(visualDisplay, color, [0, 0, display_width, thingh],0)
measures()

#end funcitons here ======================================
visualDisplay.fill(white)
	#code to create objects here========================================
mainKey(maxHeight(), finalKeyColour)
drawShapes()

pygame.image.save(visualDisplay, "screenshot.jpeg")
	#end code to create objects here ====================================
pygame.display.update()

clock.tick(30)