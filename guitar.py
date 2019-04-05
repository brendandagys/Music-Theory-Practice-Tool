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

class Menu:

    '''Display a menu and respond to choices when run.'''
    def __init__(self):

        self.choices = {"1": choice_1,
                        "2": 'get_notes_scale',
                        "3": 'interval_practice',
                        "4": choice_4,
                        "5": choice_5
                        }

    def display_menu(self):
        print("""
Practice Menu

1) Look up/play a chord
2) Look up/play a scale
3) Interval practice
4) Generate random scales
5) Generate random chords
6) QUIT
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = str(input("Enter an option: "))
            if choice == '1':
                choice_1.run()
            if choice == '4':
                choice_4.run()
            if choice == '5':
                choice_5.run()

            # action = self.choices.get(choice)
            # if action:
            # action.run()
            # else:
            #     print("\n{0} is not a valid choice.".format(choice))

class Note:
    def __init__(self, type, prefix = ''):
        self.path = pwd + '/' + prefix + str(type) + '.wav'

class Player:
    def play(self, notes_list):
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

        # REMOVE THIS
        print(note_count)

        audio1 = AudioSegment.from_wav(note_1.path)
        audio2 = AudioSegment.from_wav(note_2.path)
        audio3 = AudioSegment.from_wav(note_3.path)
        if note_count > 3:
            audio4 = AudioSegment.from_wav(note_4.path)
        if note_count > 4:
            audio5 = AudioSegment.from_wav(note_5.path)
        if note_count > 5:
            audio6 = AudioSegment.from_wav(note_6.path)
        if note_count > 6:
            audio7 = AudioSegment.from_wav(note_7.path)

        # For the chords
        audio1_long = AudioSegment.from_wav(note_1_long.path)
        audio2_long = AudioSegment.from_wav(note_2_long.path)
        audio3_long = AudioSegment.from_wav(note_3_long.path)
        if note_count > 3:
            audio4_long = AudioSegment.from_wav(note_4_long.path)
        if note_count > 4:
            audio5_long = AudioSegment.from_wav(note_5_long.path)
        if note_count > 5:
            audio6_long = AudioSegment.from_wav(note_6_long.path)
        if note_count > 6:
            audio7_long = AudioSegment.from_wav(note_7_long.path)

        mixed1 = audio1_long.overlay(audio2_long)          #combine , superimpose audio files
        mixed2 = mixed1.overlay(audio3_long)          #Further combine , superimpose audio files
        if note_count > 3:
            mixed3 = mixed2.overlay(audio4_long)
        if note_count > 4:
            mixed4 = mixed3.overlay(audio5_long)
        if note_count > 5:
            mixed5 = mixed4.overlay(audio6_long)
        if note_count > 6:
            mixed6 = mixed5.overlay(audio7_long)

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
Major Harmony:
Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian

Melodic Minor Harmony:
Melodic Minor, Phrygian N6, Lydian Augmented, Lydian Dominant, Mixolydian b6, Locrian #2, Altered

Haronic Minor Harmony:
Harmonic Minor, Locrian 6, Ionian #5, Dorian #4, Phrygian Dominant, Lydian #2, Super Locrian bb7

Others:
Major Pentatonic, Minor Pentatonic, Major Blues, Minor Blues
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


    chord_list = ['Maj', 'min', 'aug', 'Maj7', 'Maj7(#5)', '7', '7(b5)', '7(#5)', 'min7', 'min7(b5)', 'min/Maj7',
                  'Maj9', '9', 'min9', 'Maj6', 'min6', '7(#9)', '7(b9)', 'sus(b9)', '7sus4', '13', 'dim']

    chord_structures = {'Maj':[0,4,7], 'min':[0,3,7], 'aug':[0,4,8], 'Maj7':[0,4,7,11], 'Maj7(#5)':[0,4,8,11],
                        '7':[0,4,7,10], '7(b5)':[0,4,6,10], '7(#5)':[0,4,8,10], 'min7':[0,3,7,10], 'min7(b5)':[0,3,6,10],
                        'min/Maj7':[0,3,7,11], 'Maj9':[0,4,7,11,2], '9':[0,4,7,10,2], 'min9':[0,3,7,10,2], 'Maj6':[0,4,7,9],
                        'min6':[0,3,7,9], '7(#9)':[0,4,7,10,3], '7(b9)':[0,4,7,10,2], 'sus(b9)':[0,5,7,10,1],
                        '7sus4':[0,5,7,10], '13':[0,4,7,10,9], 'dim':[0,3,6,9]}

    chord_additions =  {'Maj':[4,7], 'min':[3,7], 'aug':[4,8], 'Maj7':[4,7,11], 'Maj7(#5)':[4,8,11],
                        '7':[4,7,10], '7(b5)':[4,6,10], '7(#5)':[4,8,10], 'min7':[3,7,10], 'min7(b5)':[3,6,10],
                        'min/Maj7':[3,7,11], 'Maj9':[4,7,11,14], '9':[4,7,10,14], 'min9':[3,7,10,14], 'Maj6':[4,7,9],
                        'min6':[3,7,9], '7(#9)':[4,7,10,15], '7(b9)':[4,7,10,14], 'sus(b9)':[5,7,10,13],
                        '7sus4':[5,7,10], '13':[4,7,10,21], 'dim':[3,6,9]}

    chromatic_scales = {'A':     ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab'],
                        'A#':    ['A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A'],
                        'Bb':    ['A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A'],
                        'B':     ['B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb'],
                        'C':     ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'],
                        'C#':    ['C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C'],
                        'Db':    ['C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C'],
                        'D':     ['D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db'],
                        'D#':    ['D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D'],
                        'Eb':    ['D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D'],
                        'E':     ['E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb'],
                        'F':     ['F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E'],
                        'F#':    ['F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F'],
                        'Gb':    ['F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F'],
                        'G':     ['G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb'],
                        'G#':    ['G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G'],
                        'Ab':    ['G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G']
                        }

    notes = ['a', 'a#', 'bb', 'b', 'c', 'c#', 'db', 'd', 'd#', 'eb', 'e', 'f', 'f#', 'gb', 'g', 'g#', 'ab', 'a#/bb',
             'c#/db', 'd#/eb', 'f#/gb', 'g#/ab']

    notes_lookup = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    notes_dict = {'a':1, 'a#':2, 'bb':2, 'b':3, 'c':4, 'c#':5, 'db':5, 'd':6, 'd#':7, 'eb':7, 'e':8, 'f':9, 'f#':10,
                  'gb':10, 'g':11, 'g#':12, 'ab':12, 'a#/bb':2, 'c#/db':5, 'd#/eb':7, 'f#/gb':10, 'g#/ab':12}

    def prompt(self):
        print('''
Triads:
Maj, min, aug

Seventh Chords:
Maj7, Maj7(#5), 7, 7(b5), 7(#5), min7, min7(b5), min/Maj7

Ninth Chords:
Maj9, 9, min9

Other Chords:
Maj6, min6, 7(#9), 7(b9), sus(b9), 7sus4, 13, dim
''')

    def notes_in_chord(self):

        got_root = 0
        chord = input('\nPlease enter the root or the full chord: ')

        if ((len(chord) == 1) and (chord.lower() in self.notes)):
            text_root = chord.upper()
            root = self.notes_dict[chord[0].lower()]
            got_root = 1

        elif (((chord[1].lower() == 'b') or chord[1] == '#') and (len(chord) > 1) and (len(chord) < 6)):
            text_root = chord[0:2]
            root = self.notes_dict[chord[0:2].lower()]
            got_root = 1

        if got_root == 1:
            chord_type = input('\nPlease specify the type of chord: ')
            full_chord = text_root + chord_type
            if (chord_type in self.chord_list):
                chord_structure = self.chord_structures[chord_type]
                chord_addition = self.chord_additions[chord_type]

                notes_list = [root]
                for number in chord_addition:
                    notes_list.append(notes_list[0] + number)

                text_notes_list = []
                for degree in chord_structure:
                    text_notes_list.append(self.chromatic_scales[text_root][degree])
                print('\nThe notes in ' + full_chord + ' are: ' + str(text_notes_list) + '\n')

                print(notes_list)

                ask_to_play = input('Press \'p\' to hear the chord. Press any other key to try another chord: ')
                if ask_to_play.lower() == 'p':
                    player.play(notes_list)

                self.notes_in_chord()

            else:
                print('\nPLEASE USE A VALID CHORD TYPE.')


        # elif ((len(chord) > 1) and (chord[0].lower() in self.notes)):
        #     root = chord[0].upper()
        #     chord_type = chord[1:]
        #     full_chord = root + chord_type
        #     if ((chord_type in self.chord_list) or (chord_type.lower() in self.chord_list)):
        #         structure = self.chord_structures[chord_type]
        #
        #         notes_list = []
        #         for degree in structure:
        #             notes_list.append(self.chromatic_scales[root][degree])
        #         print('\nThe notes in ' + full_chord + ' are: ' + str(notes_list) + '\n')
        #
        #         ask_to_play = input('Press \'p\' to hear the chord. Press any other key to try another chord: ')
        #         if ask_to_play.lower() == 'p':
        #             player.play(notes_list)
        #
        #         self.notes_in_chord()

        elif chord[0].lower() == 'q':
            Menu().run()

        else:
            print('\nPLEASE USE A ROOT FROM A - G.\n')
            self.notes_in_chord()


    # def get_notes_chord():
    #     for iteration in range(1000):
    #         type, notes = notes_of_chord()
    #         chord = Chord(type, notes)
    #         chord.print_type()
    #         chord.print_notes()

class RandomScale:

    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    scales = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian',
              'Melodic Minor', 'Phrygian N6', 'Lydian Augmented', 'Lydian Dominant',
              'Mixolydian b6', 'Locrian #2', 'Altered', 'Harmonic Minor', 'Locrian 6',
              'Ionian #5', 'Dorian #4', 'Phrygian Dominant', 'Lydian #2', 'Super Locrian bb7',
              'Major Pentatonic', 'Minor Pentatonic', 'Major Blues', 'Minor Blues']

    def run(self):

        display_count = int(input('\nPlease enter the number of scales you\'d like displayed: '))
        time_delay = int(input('\nPlease enter the delay in seconds between each scale: '))

        temporary = []

        if (display_count > 0 and time_delay > 0):

            for count in range(0, display_count):
                note = random.randint(0, 11)
                scale = random.randint(0, 24)

                if scale in temporary:
                    count = count - 1
                    continue
                else:
                    temporary.append(scale)

                if len(temporary) == 21:
                    temporary = []
                    # print ('\n--------------------------------------------------------------------------------')

                print ('\n' + self.notes[note] + ' ' + self.scales[scale])

                time.sleep(time_delay)

        else:
            print('\nPLEASE ENSURE NUMBERS ARE GREATER THAN 0.')



class RandomChord:

    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

    chord_list = ['Maj', 'min', 'aug', 'Maj7', 'Maj7(#5)', '7', '7(b5)', '7(#5)', 'min7', 'min7(b5)', 'min/Maj7',
                  'Maj9', '9', 'min9', 'Maj6', 'min6', '7(#9)', '7(b9)', 'sus(b9)', '7sus4', '13', 'dim']

    def run(self):

        display_count = int(input('\nPlease enter the number of chords you\'d like displayed: '))
        time_delay = int(input('\nPlease enter the delay between each chord: '))

        temporary = []

        if (display_count > 0 and time_delay > 0):

            for count in range(0, display_count):
                note = random.randint(0, 11)
                chord = random.randint(0, 21)

                if chord in temporary:
                    count = count - 1
                    continue
                else:
                    temporary.append(chord)

                if len(temporary) == 21:
                    temporary = []
                    # print ('\n--------------------------------------------------------------------------------')

                print ('\n' + self.notes[note] + self.chord_list[chord])

                time.sleep(time_delay)

        else:
            print('\nPLEASE ENSURE NUMBERS ARE GREATER THAN 0.')

        # Menu().Run()

if __name__ == "__main__":
    choice_1 = GetNotesChord()
    choice_4 = RandomScale()
    choice_5 = RandomChord()
    player = Player()
    Menu().run()
