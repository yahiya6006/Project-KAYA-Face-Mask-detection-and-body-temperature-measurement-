from playsound import playsound
import pygame

def Play_Nomask():
    pygame.mixer.init()
    pygame.mixer.music.load("utils/Vocal_sound//1.mp3")
    pygame.mixer.music.play()


def Play_temperature():
    pygame.mixer.init()
    pygame.mixer.music.load("utils/Vocal_sound//2.mp3")
    pygame.mixer.music.play()

