#this file manages the location of meme in the app

import pygame


#class to manage the location
class Location(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("/Users/admin/programmation/depot_git/slot_machine/assets_slot_machine/dogecoin.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def set_image(self, image):
        self.image = image

#location of slot machine assets:

slot_x = 150
slot_y = -50
wheel_y = slot_y + 330

#loaded of the locations
locations = pygame.sprite.Group()        
left_location = Location(slot_x + 98, wheel_y) #248
center_location = Location(slot_x + 252, wheel_y) #402
right_location = Location(slot_x + 405, wheel_y) #555

#storage location in the group
locations.add(left_location)
locations.add(center_location)
locations.add(right_location)