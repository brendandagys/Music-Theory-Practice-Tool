from pydub import AudioSegment
from pydub.playback import play
import ffmpeg

import os
import io
import sys
import subprocess

pwd = os.getcwd()
print()
audio1 = AudioSegment.from_wav(pwd + "/audio_files/1.wav") #your first audio file
audio2 = AudioSegment.from_wav(pwd + "/audio_files/5.wav") #your second audio file
audio3 = AudioSegment.from_wav(pwd + "/audio_files/8.wav") #your third audio file
audio4 = AudioSegment.from_wav(pwd + "/audio_files/11.wav")
#
mixed = audio1.overlay(audio2)          #combine , superimpose audio files
mixed1 = mixed.overlay(audio3)          #Further combine , superimpose audio files
mixed2 = mixed1.overlay(audio4)
# # If you need to save mixed file
# audio1.export('aaaaa.wav', format='wav')
mixed2.export(pwd + '/audio_files/to_play.wav', format='wav') #export mixed  audio file
                             #play mixed audio file
subprocess.call(['afplay', pwd + '/audio_files/1.wav'])
subprocess.call(['afplay', pwd + '/audio_files/5.wav'])
subprocess.call(['afplay', pwd + '/audio_files/8.wav'])
subprocess.call(['afplay', pwd + '/audio_files/11.wav'])

subprocess.call(['afplay', pwd + '/audio_files/to_play.wav'])
