from pydub import AudioSegment
from pydub.playback import play
import ffmpeg

import os

pwd = os.getcwd()

audio1 = AudioSegment.from_wav(pwd + "/C.wav") #your first audio file
audio2 = AudioSegment.from_wav(pwd + "/E.wav") #your second audio file
audio3 = AudioSegment.from_wav(pwd + "/G.wav") #your third audio file
audio4 = AudioSegment.from_wav(pwd + "/B.wav")
#
mixed = audio1.overlay(audio2)          #combine , superimpose audio files
mixed1 = mixed.overlay(audio3)          #Further combine , superimpose audio files
mixed2 = mixed1.overlay(audio4)
# If you need to save mixed file
audio1.export('aaaaa.wav', format='wav')
# mixed1.export("aaaaaaaaa.wav", format='wav') #export mixed  audio file
play(audio1)                             #play mixed audio file
play(audio2)
play(audio3)
play(audio4)

play(mixed2)
