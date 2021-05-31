from playsound import playsound
import pygame

# used pygame to play the sound in background
def Play_Nomask():
    pygame.mixer.init()
    pygame.mixer.music.load("utils/Vocal_sound//1.mp3")
    pygame.mixer.music.play()


def Play_temperature():
    pygame.mixer.init()
    pygame.mixer.music.load("utils/Vocal_sound//2.mp3")
    pygame.mixer.music.play()


# used playsound so the program will execute after this function 
def Play_thank_you():
	playsound("utils/Vocal_sound//3.mp3")