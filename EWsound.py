import RPi.GPIO as GPIO
import time
import pygame
import threading
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
sound_playing = {}
def play_sound(sound_file):
	if sound_file not in sound_playing or not sound_playing[sound_file]:
		sound_playing[sound_file] = True
		sound_playing[sound_file] = True
		sound = pygame.mixer.Sound(sound_file)
		sound.play()
		pygame.time.wait(int(sound.get_length() * 1000))
		sound_playing[sound_file] = False
		

def monitor_pins():
	try:
		GPIO.output(1, GPIO.HIGH)
		GPIO.output(2, GPIO.HIGH)
		GPIO.output(3, GPIO.HIGH)
		GPIO.output(4, GPIO.HIGH)
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(7, GPIO.HIGH)
		GPIO.output(8, GPIO.HIGH)
		GPIO.output(9, GPIO.HIGH)
		GPIO.output(10, GPIO.HIGH)
		while True:
			GPIO.output(1, GPIO.LOW)
		
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/train.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/StringF.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/G.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassD.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/LowBassStringC.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/F#.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(1, GPIO.HIGH)
			GPIO.output(2, GPIO.LOW)

			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassC#.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassLoCHiF.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/E.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassF#.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassC.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassG.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(2, GPIO.HIGH)
			GPIO.output(3, GPIO.LOW)
		
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/StringA.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/LowBassDrumC.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/E.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BirdSound.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Bongo.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(3, GPIO.HIGH)
			GPIO.output(4, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/LowB.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/DrumG.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/LowBassC.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/F#.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassG.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/String.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(4, GPIO.HIGH)
			GPIO.output(5, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Bongo.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiC.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Ratchet.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassStringE.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/JingleBells.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/CarMotor.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(5, GPIO.HIGH)
			GPIO.output(6, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/WoodBlock.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Cowbell.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Windchimes.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiG.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassF.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/F#.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(6, GPIO.HIGH)
			GPIO.output(7, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/C.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Bongo.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiStringA.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Guiro.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/StringG.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(7, GPIO.HIGH)
			GPIO.output(8, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiStringF#.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiA.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/PianoB.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/StringG.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassDrumC.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/StringD.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(8, GPIO.HIGH)
			GPIO.output(9, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Bongo.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Cymbal.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)

			GPIO.output(9, GPIO.HIGH)
			GPIO.output(10, GPIO.LOW)
			
			if GPIO.input(11) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/HiStringC.wav',)).start()
				time.sleep(0.1)
				
			if GPIO.input(12) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/VoiceChoirG.wav',)).start()
				time.sleep(0.1)
		
			if GPIO.input(13) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('//home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)
			
			if GPIO.input(14) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/Train.wav',)).start()
				time.sleep(0.1)
			if GPIO.input(15) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassDrumC.wav',)).start()
				time.sleep(0.1)
			if GPIO.input(16) == GPIO.LOW:
				threading.Thread(target = play_sound, args = ('/home/admin/Downloads/Wav2/BassF.wav',)).start()
				time.sleep(0.1)
				
			GPIO.output(10, GPIO.HIGH)
	finally:
		GPIO.cleanup()

monitor_thread = threading.Thread(target=monitor_pins)
monitor_thread.start()
try:
	monitor_thread.join()
except KeyboardInterrupt:
	sys.exit(0)
