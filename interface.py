import pygame
import location
import numpy
from location import *
from playsound import playsound

pygame.init()

#function to launch the wheels
def launcher():
    
    global tokens
    
    print('Welcome to the Meme Slot Machine !!')

    memes = ["risitas", "pepe", "wojak", "dicaprio", "dogecoin"]
    proba_meme = [0.4, 0.25, 0.2, 0.1, 0.05]# =1
    
    
    
    meme_dict_img = {
        
    "risitas" : pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/risitas.png"),
    "pepe" : pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/pepe.png"),
    "wojak" : pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/wojak.png"),
    "dicaprio" : pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/dicaprio.png"),
    "dogecoin" : pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/dogecoin.png"),
}
    
    meme_dict_sound = {
        
    "risitas" : pygame.mixer.Sound("/Users/admin/programmation/depot_git/slot_machine/sound_effects/risitas.mp3"),
    "pepe" : pygame.mixer.Sound("/Users/admin/programmation/depot_git/slot_machine/sound_effects/just_do_it.mp3"),
    "wojak" : pygame.mixer.Sound("/Users/admin/programmation/depot_git/slot_machine/sound_effects/wouaaaaa.mp3"),
    "dicaprio" : pygame.mixer.Sound("/Users/admin/programmation/depot_git/slot_machine/sound_effects/lol.mp3"),
    "dogecoin" : pygame.mixer.Sound("/Users/admin/programmation/depot_git/slot_machine/sound_effects/Thug Life.mp3"),
}
    
    memes_dict = {
    
    "risitas" : 5,
    "pepe" : 15,
    "wojak" : 50,
    "dicaprio" : 150,
    "dogecoin" : 15000
}

    random_selected_three = numpy.random.choice(memes, 3, p=proba_meme)#list, nombre de tirage , proba
    meme_left = random_selected_three[0]
    tokens -= 5

    
    #change the image
    left_location.set_image(meme_dict_img[meme_left])
    center_location.set_image(meme_dict_img[random_selected_three[1]])
    right_location.set_image(meme_dict_img[random_selected_three[2]])
    
    print(f"{random_selected_three[0]} || {random_selected_three[1]} || {random_selected_three[2]}")

    if random_selected_three[0] == random_selected_three[1] == random_selected_three[2]:
        token = memes_dict[random_selected_three[0]]
        sound = meme_dict_sound[random_selected_three[0]]
        tokens = tokens + token
        print(f"Congratulations, you have won {token} tokens")
        sound.play()
        #if sound.play():
            
    else:
        print("You didn't win any token!")
        

#creation of the screen
height_screen = 650
width_screen = 1000
screen = pygame.display.set_mode((width_screen, 650))
pygame.display.set_caption("Meme Slot Machine!")
black = [0, 0 ,0]
white = [255, 255, 255]
green = [18, 164, 81]
tokens = 1000
background_sound = pygame.mixer.Sound("sound_effects/background_sound.mp3")
background_sound.play()

#creation of the text for the token quantity 
font = pygame.font.SysFont(None, 32)
text_score = font.render('Score :', True, black)



#load slot-machine assets
slot_machine = pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/slot.png")
score = pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/score.png")
#loop to maintain the app ONx
App_ON = True

while App_ON:
    
    #load color of the screen
    screen.fill(green)
    screen.blit(slot_machine, (location.slot_x, location.slot_y))#tuple to indicate position
    location.locations.draw(screen)
    screen.blit(score, (232, 320))
    screen.blit(text_score, (350, 552))
    number_of_tokens = font.render(str(tokens), True, black)
    screen.blit(number_of_tokens, (560, 552))

    
    pygame.display.flip()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            App_ON = False
             
            
    #check if a player clik in keyboard key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                launcher()
                