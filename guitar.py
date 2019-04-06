import sys
import datetime
import random
import time
from random import randint
from pydub import AudioSegment
from pydub.playback import play
import ffmpeg

import os
pwd = os.getcwd()

def get_count(type):
    display_count = input('\nPlease enter the number of ' + type + 's' + ' you\'d like displayed: ')
    try:
        int(display_count)
        if display_count[0] == '-':
            print('\nPlease enter a positive integer!')
            get_count(type)
        return int(display_count)
    except:
        print('\nPlease enter a positive integer!')
        get_count(type)

def get_delay(type):
    time_delay = input('\nPlease enter the delay between each ' + type + ': ')
    try:
        float(time_delay)
        if time_delay[0] == '-':
            print('\nPlease enter a positive number!')
            get_delay(type)
        return float(time_delay)
    except:
        print('\nPlease enter a positive number!')
        get_delay(type)

class Menu:

    '''Display a menu and respond to choices when run.'''
    def __init__(self):

        self.choices = {"1": choice_1,
                        # "2": choice_2,
                        "3": choice_3,
                        "4": choice_4,
                        "5": choice_5
                        }

    def display_menu(self):
        print("""
=========================
PRACTICE MENU

1) Look up/play a chord
2) Look up/play a scale
3) Interval practice
4) Generate random scales
5) Generate random chords
6) QUIT
=========================
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = str(input("Enter the number of the desired exercise: "))
            if choice == '1':
                choice_1.run()
            if choice == '2':
                choice_2.run()
            if choice == '3':
                choice_3.run()
            if choice == '4':
                choice_4.run()
            if choice == '5':
                choice_5.run()


class Note:
    def __init__(self, type, prefix = ''):
        self.path = pwd + '/audio_files/' + prefix + str(type) + '.wav'

class Player:
    def play(self, notes_list):
        # Generate Note objects from the passed-in notes list
        note_count = 3
        note_1 = Note(notes_list[0]); note_1_long = Note(notes_list[0], 'l')
        note_2 = Note(notes_list[1]); note_2_long = Note(notes_list[1], 'l')
        note_3 = Note(notes_list[2]); note_3_long = Note(notes_list[2], 'l')
        try:
            note_4 = Note(notes_list[3]); note_4_long = Note(notes_list[3], 'l')
            note_count+=1
        except:
            pass
        try:
            note_5 = Note(notes_list[4]); note_5_long = Note(notes_list[4], 'l')
            note_count+=1
        except:
            pass
        try:
            note_6 = Note(notes_list[5]); note_6_long = Note(notes_list[5], 'l')
            note_count+=1
        except:
            pass
        try:
            note_7 = Note(notes_list[6]); note_7_long = Note(notes_list[6], 'l')
            note_count+=1
        except:
            pass

        # Set up the AudioSegment objects (short and long)
        audio1 = AudioSegment.from_wav(note_1.path); audio1_long = AudioSegment.from_wav(note_1_long.path)
        audio2 = AudioSegment.from_wav(note_2.path); audio2_long = AudioSegment.from_wav(note_2_long.path)
        audio3 = AudioSegment.from_wav(note_3.path); audio3_long = AudioSegment.from_wav(note_3_long.path)

        mixed1 = audio1_long.overlay(audio2_long)
        mixed2 = mixed1.overlay(audio3_long)

        if note_count > 3:
            audio4 = AudioSegment.from_wav(note_4.path); audio4_long = AudioSegment.from_wav(note_4_long.path)
            mixed3 = mixed2.overlay(audio4_long)
        if note_count > 4:
            audio5 = AudioSegment.from_wav(note_5.path); audio5_long = AudioSegment.from_wav(note_5_long.path)
            mixed4 = mixed3.overlay(audio5_long)
        if note_count > 5:
            audio6 = AudioSegment.from_wav(note_6.path); audio6_long = AudioSegment.from_wav(note_6_long.path)
            mixed5 = mixed4.overlay(audio6_long)
        if note_count > 6:
            audio7 = AudioSegment.from_wav(note_7.path); audio7_long = AudioSegment.from_wav(note_7_long.path)
            mixed6 = mixed5.overlay(audio7_long)

        # PLAY!
        play(audio1)
        play(audio2)
        play(audio3)
        if note_count > 3:
            play(audio4)
        if note_count > 4:
            play(audio5)
        if note_count > 5:
            play(audio6)
        if note_count > 6:
            play(audio7)

        time.sleep(0.5)

        # PLAY CHORD!
        if note_count == 4:
            play(mixed3)
        elif note_count == 5:
            play(mixed4)
        elif note_count == 6:
            play(mixed5)
        elif note_count == 7:
            play(mixed6)
        else:
            play(mixed2)


class GetNotesScale:

    chromatic_scales = {'A':     ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab'],
                        'A#/Bb': ['A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A'],
                        'B':     ['B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb'],
                        'C':     ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'],
                        'C#/Db': ['C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C'],
                        'D':     ['D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db'],
                        'D#/Eb': ['D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D'],
                        'E':     ['E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb'],
                        'F':     ['F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E'],
                        'F#/Gb': ['F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F'],
                        'G':     ['G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb'],
                        'G#/Ab': ['G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G']
                        }

    def prompt(self):
        print('''
-------------------------------------------------------------------------------------------------
Major Harmony:
Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian

Melodic Minor Harmony:
Melodic Minor, Phrygian N6, Lydian Augmented, Lydian Dominant, Mixolydian b6, Locrian #2, Altered

Haronic Minor Harmony:
Harmonic Minor, Locrian 6, Ionian #5, Dorian #4, Phrygian Dominant, Lydian #2, Super Locrian bb7

Others:
Major Pentatonic, Minor Pentatonic, Major Blues, Minor Blues
-------------------------------------------------------------------------------------------------
''')

    scale_structures = {'Ionian':[0,2,4,5,7,9,11], 'Dorian':[0,2,3,5,7,9,10], 'Phrygian':[0,1,3,5,7,8,10], 'Lydian':[0,2,4,6,7,9,11],
                        'Mixolydian':[0,2,4,5,7,9,10], 'Aeolian':[0,2,3,5,7,8,10], 'Locrian':[0,1,3,5,6,8,10],
                        'Melodic Minor':[0,2,3,5,7,9,11],
                        'Phrygian N6': [0,1,3,5,7,8,10], 'Lydian Augmented':[], 'Lydian Dominant':[0,2,4,6,7,9,10],
                        'Mixolydian b6':[], 'Locrian #2':[], 'Altered':[], 'Harmonic Minor':[], 'Locrian 6':[],
                        'Ionian #5':[], 'Dorian #4':[], 'Phrygian Dominant':[], 'Lydian #2':[], 'Super Locrian bb7':[],
                        'Major Pentatonic':[], 'Minor Pentatonic':[], 'Major Blues':[], 'Minor Blues':[]}

class GetNotesChord:

    def run(self):
        while True:
            self.prompt()
            self.notes_in_chord()

    notes = ['a', 'a#', 'bb', 'b', 'c', 'c#', 'db', 'd', 'd#', 'eb', 'e', 'f', 'f#', 'gb', 'g', 'g#', 'ab', 'a#/bb',
             'c#/db', 'd#/eb', 'f#/gb', 'g#/ab']

    chord_list = ['maj', 'min', 'aug', 'maj7', 'maj7(#5)', '7', '7(b5)', '7(#5)', 'min7', 'min7(b5)', 'min/maj7', 'maj9',
                  '9', 'min9', 'maj6', 'min6', '7(#9)', '7(b9)', 'sus(b9)', '7sus4', '13', 'dim']

    notes_dict = {'a':10, 'a#':11, 'bb':11, 'b':12, 'c':1, 'c#':2, 'db':2, 'd':3, 'd#':4, 'eb':4, 'e':5, 'f':6, 'f#':7,
                  'gb':7, 'g':8, 'g#':9, 'ab':9, 'a#/bb':11, 'c#/db':2, 'd#/eb':4, 'f#/gb':7, 'g#/ab':9}

    chord_additions =  {'maj':[4,7], 'min':[3,7], 'aug':[4,8], 'maj7':[4,7,11], 'maj7(#5)':[4,8,11],
                        '7':[4,7,10], '7(b5)':[4,6,10], '7(#5)':[4,8,10], 'min7':[3,7,10], 'min7(b5)':[3,6,10],
                        'min/maj7':[3,7,11], 'maj9':[4,7,11,14], '9':[4,7,10,14], 'min9':[3,7,10,14], 'maj6':[4,7,9],
                        'min6':[3,7,9], '7(#9)':[4,7,10,15], '7(b9)':[4,7,10,14], 'sus(b9)':[5,7,10,13],
                        '7sus4':[5,7,10], '13':[4,7,10,21], 'dim':[3,6,9]}

    chromatic_scale = [None, 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B',
                       'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B',
                       'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

    def prompt(self):
        print('''
---------------------------------------------------------
Triads:
Maj, min, aug

Seventh Chords:
Maj7, Maj7(#5), 7, 7(b5), 7(#5), min7, min7(b5), min/Maj7

Ninth Chords:
Maj9, 9, min9

Other Chords:
Maj6, min6, 7(#9), 7(b9), sus(b9), 7sus4, 13, dim

Q: RETURN TO MAIN MENU
---------------------------------------------------------
''')

    def notes_in_chord(self):

        chord = input('\nPlease enter the root or the full chord: ')

        # If they provide a valid root only...
        if chord.lower() in self.notes:
            if len(chord) == 1:
                text_root = chord.upper()
                root = self.notes_dict[chord.lower()]
            elif len(chord) == 2:
                text_root = chord[0].upper() + chord[1].lower()
                root = self.notes_dict[chord.lower()]
            elif len(chord) == 5:
                text_root = chord[0:4].upper() + chord[4].lower()
                root = self.notes_dict[chord.lower()]

            chord_type = input('\nPlease specify the type of chord: ')

        # If they provide the full chord and the root is valid...
        elif chord[0].lower() in self.notes:
            try:
                if chord[4].lower() == 'b':
                    text_root = chord[0:4].upper() + chord[4].lower()
                    root = self.notes_dict[text_root.lower()]
                    chord_type = chord[5:].strip()

                elif chord[1].lower() == 'b' or chord[1] == '#':
                    text_root = chord[0].upper() + chord[1].lower()
                    root = self.notes_dict[text_root.lower()]
                    chord_type = chord[2:].strip()

                elif chord[0].lower() in self.notes:
                    text_root = chord[0].upper()
                    root = self.notes_dict[text_root.lower()]
                    chord_type = chord[1:].strip()
            except:
                pass

        elif chord[0].upper() == 'Q':
            Menu().run()

        else:
            print('\nPLEASE USE A ROOT FROM A - G#.\n')
            self.notes_in_chord()

        full_chord = text_root + chord_type

        if chord_type.lower() in self.chord_list:
            chord_addition = self.chord_additions[chord_type.lower()]

            try:
                notes_list = [root]
                for number in chord_addition:
                    notes_list.append(notes_list[0] + number)
                text_notes_list = [self.chromatic_scale[note] for note in notes_list]

                print('\nThe notes in ' + full_chord + ' are: ' + str(text_notes_list) + '\n')

                ask_to_play = input('Press \'p\' to hear the chord. Press any other key to try another chord: ')

                if ask_to_play.lower() == 'p':
                    player.play(notes_list)

                self.notes_in_chord()

            except:
                print('PLEASE USE A VALID CHORD TYPE.')

        else:
            print('\nPLEASE USE A VALID CHORD TYPE.')
            self.notes_in_chord()


class RandomInterval:

    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    interval_list = ['Minor 2nd', 'Major 2nd', 'Minor 3rd', 'Major 3rd', 'Perfect 4th', 'Tritone',
                 'Perfect 5th', 'Minor 6th', 'Major 6th', 'Minor 7th', 'Major 7th']

    def run(self):
        cycle_count = get_count('12-interval cycle')
        desired_delay = get_delay('interval')
        self.print_intervals(cycle_count, desired_delay)

    def print_intervals(self, cycle_count, desired_delay):
        temporary_notes = []
        count = 0

        while count < cycle_count:
            count+=1

            if len(temporary_notes) == 12:
                temporary_notes = []

            note = random.randint(0, 11)

            if note in temporary_notes:
                count-=1
                continue
            else:
                temporary_notes.append(note)

            print('\n----------------------------------------------------------------\n' +
            self.notes[note] + '\n----------------------------------------------------------------')

            temporary_intervals = []
            count_2 = 0

            while count_2 < 11:
                count_2+=1

                interval = random.randint(0,10)

                if interval in temporary_intervals:
                    count_2-=1
                    continue
                else:
                    temporary_intervals.append(interval)
                    print('\n' + self.interval_list[interval])
                    time.sleep(desired_delay)


class RandomScale:

    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    scale_list = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian',
              'Melodic Minor', 'Phrygian N6', 'Lydian Augmented', 'Lydian Dominant',
              'Mixolydian b6', 'Locrian #2', 'Altered', 'Harmonic Minor', 'Locrian 6',
              'Ionian #5', 'Dorian #4', 'Phrygian Dominant', 'Lydian #2', 'Super Locrian bb7',
              'Major Pentatonic', 'Minor Pentatonic', 'Major Blues', 'Minor Blues']

    def run(self):
        scale_count = get_count('scale')
        desired_delay = get_delay('scale')
        self.print_scales(scale_count, desired_delay)

    def print_scales(self, scale_count, desired_delay):
        temporary = []
        count = 0

        while count < scale_count:
            count+=1

            if len(temporary) == 25:
                temporary = []

            note = random.randint(0, 11)
            scale = random.randint(0, 24)

            if scale in temporary:
                count-=1
                continue
            else:
                temporary.append(scale)

            print ('\n' + self.notes[note] + ' ' + self.scale_list[scale])
            time.sleep(desired_delay)

        Menu().run()


class RandomChord:

    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    chord_list = ['Maj', 'min', 'aug', 'Maj7', 'Maj7(#5)', '7', '7(b5)', '7(#5)', 'min7', 'min7(b5)', 'min/Maj7',
                  'Maj9', '9', 'min9', 'Maj6', 'min6', '7(#9)', '7(b9)', 'sus(b9)', '7sus4', '13', 'dim']

    def run(self):
        chord_count = get_count('chord')
        desired_delay = get_delay('chord')
        self.print_chords(chord_count, desired_delay)

    def print_chords(self, chord_count, desired_delay):
        temporary = []
        count = 0

        while count < chord_count:
            count+=1

            if len(temporary) == 22:
                temporary = []

            note = random.randint(0, 11)
            chord = random.randint(0, 21)

            if chord in temporary:
                count-=1
                continue
            else:
                temporary.append(chord)

            print ('\n' + self.notes[note] + self.chord_list[chord])
            time.sleep(desired_delay)

        Menu().run()

if __name__ == "__main__":
    choice_1 = GetNotesChord()
    # choice_2 = GetNotesScale()
    choice_3 = RandomInterval()
    choice_4 = RandomScale()
    choice_5 = RandomChord()
    player = Player()
    Menu().run()
