import random
from musthe import *
import numpy

def setCondition(state):
    if state == 'R':
        return [1, 0, 0]
    elif state == 'C':
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def mChain(currentState, transitionMatrix):

    newState = numpy.dot(currentState, transitionMatrix)
    # defines the new state vector by multiplying the current state vector with the transition matrix

    return random.choices(['R', 'C', 'N'], weights=(list(newState)), k=1)
    # returns a state of either R, C, or N, based on the probabilities given by the new state vector

transitionMatrix = [[0.3,0.7,0],[0.2,0.3,0.5],[1,0,0]] #defines the transition matrix

state = "R"

chord = Scale(Note('C'), 'major')
tonalCenter = Scale(Note('C'), 'major')

scales = [str(chord)]
states = [state]
notes = [random.choices(list(chord[i] for i in range(len(chord))))[0]]

for i in range(20):
    
    currentState = states[i]
    
    if currentState == 'R': 
        chord = tonalCenter  # whatever the current chord is, change it to whatever the current tonal center is
    elif currentState == 'C':
        chord = Scale(chord.root + random.choices([Interval('P4'), Interval('P5')], weights=(50, 50), k=1)[0], 'major')
        # for our purposes, we made the "change" state change the chord to either the fourth (IV) or fifth (V) of the chord
        # with equal probability
    else: # case 'N'
        tonalCenter = chord # update the tonal center to be what the current chord is

    for j in range(4):

        #n = random.choices(list((s[i]) for i in range(len(s))))
        n = notes[4 * i + j - 1]
        
        tempScale = chord

        tempScale.root.octave = n.octave - 1
        noteList = list((tempScale[i]) for i in range(len(tempScale)))
        tempScale.root.octave = n.octave
        noteList += ((tempScale[i]) for i in range(len(tempScale)))
        
        if n in noteList:
            index = noteList.index(n)
        elif (n + Interval('m2')) in noteList:
            index = noteList.index(n + Interval('m2'))
        elif (n + Interval('M2')) in noteList:
            index = noteList.index(n + Interval('M2'))
        else:
            print('error lol')

        n = noteList[(index + random.choices([-2, -1, 0, 1, 2], weights=(5, 30, 30, 30, 5), k=1)[0]) % 14]

        notes += [n]
   
    states += mChain(setCondition(currentState), transitionMatrix)
    scales += [str(chord)]

print(states)
print("\n")
print(scales)
print("\n")
#print(s)
notestr = ""
for note in notes:
    notestr += str(note) + str(note.octave) + " "

print(notestr)
print("\n")







