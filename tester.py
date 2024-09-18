# https://stackoverflow.com/questions/67524067/how-to-play-multiple-sound-files-at-the-same-milisecond-in-pygame
# sound library from https://github.com/fuhton/piano-mp3
# need to install pygame:  pip install pygame
# if Python 3.11, there is a bug, need to do:  pip install pygame --pre
# "pip list" to check 

import pygame as pg
import time
from random import random

pg.init()
pg.mixer.set_num_channels(50)

note_names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
note_names_dict = {"C": 0, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}

class Note:
    def __init__(self, position):
        i = int(position / 12)
        n = note_names[position % 12]
        self.name = n + str(i)
        self.note = pg.mixer.Sound(f"mp3/{self.name}.mp3")

    def __str__(self):
        return self.name

    def play(self, channel, duration = 0):
        pg.mixer.Channel(channel).play(self.note)
        if duration > 0: time.sleep(duration)


class Notes:
    def __init__(self, type, position, distances):
        self.type = type
        self.notes = [Note(position)] 
        self.name = f"{self.notes[0].name} {type}"
        for pos in distances:
            self.notes.append(Note(position + pos))

    def __str__(self):
        self.name

    def play(self, start_channel, duration = 0):
        for i in range(len(self.notes)):
            self.notes[i].play(start_channel + i)
        if duration > 0: time.sleep(duration)
        

def get_pos_from_name(name):
    i = int(name[-1])
    n = name[:-1]
    return i * 12 + note_names_dict[n]

def get_name_from_pos(pos):
    i = int(pos / 12)
    n = note_names[pos % 12]
    return n + str(i)


def random_pos(start, end):
    low = get_pos_from_name(start)
    high = get_pos_from_name(end)
    return int(random() * (high - low)) + low

def get_chord_distances(type):
    if type.lower() == "major":
        return [4,7]
    elif type.lower() == "minor":
        return [3,7]
    else:
        return [3,6]

# Valid notes range from 12 to 95
def get_random_note(start = "C1", end = "A7"):
    return Note(random_pos(start, end))


def get_random_chord(start = "C1", end = "A7"):

    choice = int(3 * random())
    type = ""
    if choice == 0:
        type = "Major"
    elif choice == 1:
        type = "Minor"
    elif choice == 2:
        type = "Diminished"

    pos = random_pos(start, end)

    return Notes(type, pos, get_chord_distances(type))

while(True):
    print("===================================================")
    print("\nPlaying chord.")
    chord = get_random_chord("C4", "F5")
    chord.play(0, 2)
    print("What type was that?\n")

    repeat = True
    while repeat:
        answer = input().lower()
        repeat = False
        
        if answer == "exit":
            print("\nExiting.\n")
            exit()
        elif answer == "repeat":
            repeat = True
            print("\nRepeating chord.")
            chord.play(0,2)
            print("What type was that?\n")
        elif answer == "":
            print(f"\n{chord.name}\nPress enter to continue...")
        elif answer == chord.type.lower():
            print(f"\nCorrect! Chord was {chord.name}.\nPress enter to continue...")
        else:
            print(f"\nIncorrect. Chord was {chord.name}.\nPress enter to continue...")

    repeat = True
    while repeat:
        instruction = input().lower()
        if instruction == "exit":
            print("\nExiting.\n")
            exit()
        elif instruction == "repeat":
            print("\nRepeating chord.\nPress enter to continue...")
            chord.play(0,2)
        elif instruction == "other":
            if chord.type == "Major":
                print("\nChord is Major, there is no 'other' chord.\nPress enter to continue...")
            else:
                type = ""
                pos = get_pos_from_name(chord.notes[0].name)
                if chord.type == "Minor":
                    type = "Diminished"
                else:
                    type = "Minor"
                distances = get_chord_distances(type)
                chord = Notes(type, pos, distances)
                    
                print(f"\nPlaying {chord.name}.")
                chord.play(0,2)
                print("Press enter to continue...")
        elif instruction == "major":
            type = "Major"
            pos = get_pos_from_name(chord.notes[0].name)
            distances = get_chord_distances(type)

            chord = Notes(type, pos, distances)
            
            print(f"\nPlaying {chord.name}.")
            chord.play(0,2)
            print("Press enter to continue...")
        elif instruction == "minor":
            type = "Minor"
            pos = get_pos_from_name(chord.notes[0].name)
            distances = get_chord_distances(type)

            chord = Notes(type, pos, distances)
            
            print(f"\nPlaying {chord.name}.")
            chord.play(0,2)
            print("Press enter to continue...")
        elif instruction == "diminished":
            type = "Diminished"
            pos = get_pos_from_name(chord.notes[0].name)
            distances = get_chord_distances(type)

            chord = Notes(type, pos, distances)
            
            print(f"\nPlaying {chord.name}.")
            chord.play(0,2)
            print("Press enter to continue...")
        elif instruction == "":
            repeat = False
        else:
            print("\nPress enter to continue...")





