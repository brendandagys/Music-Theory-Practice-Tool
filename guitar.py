# SUPPRESS OUTPUT AND FIX FULL CHORD + FULL SCALE ENTRY???: 'SOME ERROR'

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
    # Make sure that an integer is provided and deal with negative values if passed
    try:
        if display_count[0] == '-':
            display_count = display_count[1:]
        return int(display_count)
    except:
        print('\nPlease enter a positive integer!')
        return get_count(type)

def get_delay(type):
    time_delay = input('\nPlease enter the delay between each ' + type + ': ')
    # Make sure that an integer is provided and deal with negative values if passed
    try:
        if time_delay[0] == '-':
            time_delay = time_delay[1:]
        return float(time_delay)
    except:
        print('\nPlease enter a positive number!')
        return get_delay(type)

class Menu:
    '''Display a menu of options to choose.'''
    def __init__(self):

        self.choices = {"1": choice_1,
                        "2": choice_2,
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
            choice = input("Please enter a number from 1 - 6: ")
            if choice == '1':
                choice_1.run()
            elif choice == '2':
                choice_2.run()
            elif choice == '3':
                choice_3.run()
            elif choice == '4':
                choice_4.run()
            elif choice == '5':
                choice_5.run()
            elif choice == '6':
                print()
                sys.exit()


class Note:
    '''Create a note object whose only attribute is the path to the relevant note sound file.'''
    def __init__(self, type, prefix = ''):
        self.path = pwd + '/audio_files/' + prefix + str(type) + '.wav'

class Player:
    '''Will play sound files based on a list of notes that is passed in.'''
    def play(self, notes_list, chord = False):
        '''Generate Note objects from the passed-in notes list.'''
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
        try:
            note_8 = Note(notes_list[7]); note_8_long = Note(notes_list[7], 'l')
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
        if note_count > 7:
            audio8 = AudioSegment.from_wav(note_8.path); audio7_long = AudioSegment.from_wav(note_8_long.path)

        print()

        # sys.stdout = open(os.devnull, "w")
        # PLAY!
        play(audio1); play(audio2); play(audio3)
        if note_count > 3:
            play(audio4)
        if note_count > 4:
            play(audio5)
        if note_count > 5:
            play(audio6)
        if note_count > 6:
            play(audio7)
        if note_count > 7:
            play(audio8)

        time.sleep(0.5)

        if chord == True:
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
        # sys.stdout = sys.__stdout__
        print()


class GetNotesScale:
    '''Get input from user and determine the root/scale. Display the notes in the scale and possibly play it.'''
    def run(self):
        while True:
            self.prompt()
            self.notes_in_scale()

    notes_dict = {'a':10, 'a#':11, 'bb':11, 'b':12, 'c':1, 'c#':2, 'db':2, 'd':3, 'd#':4, 'eb':4, 'e':5, 'f':6, 'f#':7,
                  'gb':7, 'g':8, 'g#':9, 'ab':9, 'a#/bb':11, 'c#/db':2, 'd#/eb':4, 'f#/gb':7, 'g#/ab':9}

    scale_additions = {'ionian':[2,4,5,7,9,11], 'dorian':[2,3,5,7,9,10], 'phrygian':[1,3,5,7,8,10], 'lydian':[2,4,6,7,9,11],
                       'mixolydian':[2,4,5,7,9,10], 'aeolian':[2,3,5,7,8,10], 'locrian':[1,3,5,6,8,10],
                       'melodic minor':[2,3,5,7,9,11], 'phrygian n6': [1,3,5,7,8,10], 'lydian augmented':[2,4,6,8,9,11],
                       'lydian dominant':[2,4,6,7,9,10], 'mixolydian b6':[2,4,5,7,8,10], 'locrian #2':[2,3,5,6,8,10],
                       'altered':[1,3,4,6,8,10], 'harmonic minor':[2,3,5,7,8,11], 'locrian n6':[1,3,5,6,9,10],
                       'ionian #5':[2,4,5,8,9,11], 'dorian #4':[2,3,6,7,9,10], 'phrygian dominant':[1,4,5,7,9,10],
                       'lydian #2':[3,4,6,7,9,11], 'super locrian bb7':[1,3,4,6,8,9], 'major pentatonic':[2,4,7,9],
                       'minor pentatonic':[3,5,7,10], 'major blues':[2,3,4,7,9], 'minor blues':[3,5,6,7,10]}

    chromatic_scale = [None, 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B',
                             'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb']

    def prompt(self):
        print('''
-------------------------------------------------------------------------------------------------
Major Harmony:
Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian

Melodic Minor Harmony:
Melodic Minor, Phrygian N6, Lydian Augmented, Lydian Dominant, Mixolydian b6, Locrian #2, Altered

Haronic Minor Harmony:
Harmonic Minor, Locrian N6, Ionian #5, Dorian #4, Phrygian Dominant, Lydian #2, Super Locrian bb7

Others:
Major Pentatonic, Minor Pentatonic, Major Blues, Minor Blues
-------------------------------------------------------------------------------------------------
''')

    def notes_in_scale(self):

        scale = input('Please enter the root or the root with scale: ')

        # If they provide a valid root only...
        if scale.lower() in list(self.notes_dict.keys()):
            if len(scale) == 1:
                text_root = scale.upper()
                root = self.notes_dict[scale.lower()]
            elif len(scale) == 2:
                text_root = scale[0].upper() + scale[1].lower()
                root = self.notes_dict[scale.lower()]
            elif len(scale) == 5:
                text_root = scale[0:4].upper() + scale[4].lower()
                root = self.notes_dict[scale.lower()]
            # With the root, now ask for the chord type
            scale_type = input('\nPlease specify the type of scale: ')

        # If they provide the full scale and the root is valid...
        elif scale[0].lower() in list(self.notes_dict.keys()):
            try:
                if scale[4].lower() == 'b':
                    text_root = scale[0:4].upper() + scale[4].lower()
                    root = self.notes_dict[text_root.lower()]
                    scale_type = scale[5:].strip()
            except:
                pass

            try:
                if scale[1].lower() == 'b' or scale[1] == '#':
                    text_root = scale[0].upper() + scale[1].lower()
                    root = self.notes_dict[text_root.lower()]
                    scale_type = scale[2:].strip()
            except:
                pass

            try:
                text_root = scale[0].upper()
                root = self.notes_dict[text_root.lower()]
                scale_type = scale[1:].strip()
            except:
                pass

        # To quit this exercise
        elif scale[0].upper() == 'Q':
                Menu().run()

        else:
            print('\nPLEASE USE A ROOT FROM A - G#.\n')
            self.notes_in_scale()

        # Create the full scale string
        full_scale = text_root + ' ' + scale_type
        # Get the scale formula, if the scale type is valid
        if scale_type.lower() in list(self.scale_additions.keys()):
            scale_addition = self.scale_additions[scale_type.lower()]

            # Construct both note lists
            try:
                notes_list = [root]
                # For the Player object to play
                for number in scale_addition:
                    notes_list.append(notes_list[0] + number)
                notes_list.append(root + 12)

                # To display the scale notes on the screen
                text_notes_list = [self.chromatic_scale[note] for note in notes_list]
                print('\nThe notes in ' + full_scale + ' are: ' + str(text_notes_list) + '\n')
                # Ask whether or not to play the scale
                ask_to_play = input('Press \'p\' to hear the scale. Press any other key to try another scale: ')

                if ask_to_play.lower() == 'p':
                    player.play(notes_list)
                print()
                self.notes_in_scale()

            except:
                print('\nSOME ERROR.') # Unknown error

        else:
            print('\nPLEASE USE A VALID SCALE TYPE.\n')
            self.notes_in_scale()


class GetNotesChord:
    '''Get input from user and determine the chord. Display the notes in the chord and possibly play the arpeggio/chord.'''
    def run(self):
        while True:
            self.prompt()
            self.notes_in_chord()

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

        chord = input('Please enter the root or the full chord: ')

        # If they provide a valid root only...
        if chord.lower() in list(self.notes_dict.keys()):
            if len(chord) == 1:
                text_root = chord.upper()
                root = self.notes_dict[chord.lower()]
            elif len(chord) == 2:
                text_root = chord[0].upper() + chord[1].lower()
                root = self.notes_dict[chord.lower()]
            elif len(chord) == 5:
                text_root = chord[0:4].upper() + chord[4].lower()
                root = self.notes_dict[chord.lower()]
            # With the root, now ask for the chord type
            chord_type = input('\nPlease specify the type of chord: ')

        # If they provide the full chord and the root is valid...
        elif chord[0].lower() in list(self.notes_dict.keys()):
            try:
                if chord[4].lower() == 'b':
                    text_root = chord[0:4].upper() + chord[4].lower()
                    root = self.notes_dict[text_root.lower()]
                    chord_type = chord[5:].strip()
            except:
                pass

            try:
                if chord[1].lower() == 'b' or chord[1] == '#':
                    text_root = chord[0].upper() + chord[1].lower()
                    root = self.notes_dict[text_root.lower()]
                    chord_type = chord[2:].strip()
            except:
                pass

            try:
                text_root = chord[0].upper()
                root = self.notes_dict[text_root.lower()]
                chord_type = chord[1:].strip()
            except:
                pass

        # To quit this exercise
        elif chord[0].upper() == 'Q':
            Menu().run()

        else:
            print('\nPLEASE USE A ROOT FROM A - G#.\n')
            self.notes_in_chord()

        # Create the full chord string
        full_chord = text_root + chord_type
        # Get the chord formula, if the chord type is valid
        if chord_type.lower() in list(self.chord_additions.keys()):
            chord_addition = self.chord_additions[chord_type.lower()]

            # Construct both note lists
            try:
                notes_list = [root]
                # For the Player object to play
                for number in chord_addition:
                    notes_list.append(notes_list[0] + number)
                # To display the chord notes on the screen
                text_notes_list = [self.chromatic_scale[note] for note in notes_list]
                print('\nThe notes in ' + full_chord + ' are: ' + str(text_notes_list) + '\n')
                # Ask whether or not to play the arpeggio + chord
                ask_to_play = input('Press \'p\' to hear the chord. Press any other key to try another chord: ')

                if ask_to_play.lower() == 'p':
                    player.play(notes_list, chord = True)
                print()
                self.notes_in_chord()

            except:
                print('SOME ERROR.') # Unknown error

        else:
            print('\nPLEASE USE A VALID CHORD TYPE.\n')
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
        temporary_notes = [] # To hold used notes
        count = 0

        while count < cycle_count:
            count+=1
            # If all notes have been used, reset
            if len(temporary_notes) == 12:
                temporary_notes = []

            note = random.randint(0, 11)
            # Do not reuse notes until all have been displayed
            if note in temporary_notes:
                count-=1
                continue
            else:
                temporary_notes.append(note)

            print('\n----------------------------------------------------------------\n' +
            self.notes[note] + '\n----------------------------------------------------------------')

            temporary_intervals = [] # To hold used intervals
            count_2 = 0

            while count_2 < 11:
                count_2+=1

                interval = random.randint(0,10)
                # Do not reuse intervals until all have been displayed
                if interval in temporary_intervals:
                    count_2-=1
                    continue
                else:
                    temporary_intervals.append(interval)
                    print('\n' + self.interval_list[interval])
                    time.sleep(desired_delay)

        Menu.run()

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
        temporary = [] # To hold used scales
        count = 0

        while count < scale_count:
            count+=1
            # If all scales have been used, reset
            if len(temporary) == 25:
                temporary = []

            note = random.randint(0, 11)
            scale = random.randint(0, 24)
            # Do not reuse scales until all have been displayed
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
        temporary = [] # To hold used chords
        count = 0

        while count < chord_count:
            count+=1
            # If all chords have been used, reset
            if len(temporary) == 22:
                temporary = []

            note = random.randint(0, 11)
            chord = random.randint(0, 21)
            # Do not reuse chords until all have been displayed
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
    choice_2 = GetNotesScale()
    choice_3 = RandomInterval()
    choice_4 = RandomScale()
    choice_5 = RandomChord()
    player = Player()
    Menu().run()
