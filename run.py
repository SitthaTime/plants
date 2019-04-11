# Import ========================= Import ========================= Import
import pygame
import sys
from os.path import join

# Function ======================= Function ======================= Function
# เช็คว่าตำแหน่งเมาส์ โดนปุ่มไหม
def is_hit_box(position,box_a,box_b):
    # position คือ ตำแหน่งเมาส์ (tuple 2 element)(จุด x,y)
    # box_a คือ จุดมุมซ้ายบนของปุ่ม (tuple 2 element)(จุด x,y)
    # box_b คือ จุดมุมขวาล่างของปุ่ม (tuple 2 element)(จุด x,y)

    if box_a[0] < position[0] < box_b[0] : # ถ้า x อยู่ระหว่างนั้น
        if box_a[1] < position[1] < box_b[1] :
            return True
    
    return False


# Class ========================== Class ========================== Class
# resouce_manager ---------------- resouce_manager
class Sound():
    def __init__(self):
        self.main_theme = None
        self.change_page = pygame.mixer.Sound(join('assets','sound','change_page.wav'))
        self.click = None

class Image():
    def __init__(self):
        self.main_bg = pygame.image.load(join('assets','image','stupid_bg.png')).convert()
        

# Menu --------------------------- Menu
# หน้าฟาร์มของผู้เล่น
class Player_farm():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
        
# shop
class Shop_menu():
    def __init__(self):
        self.inprocess = True

    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'

# คลัง
class Storage_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                   return 'exit'

# แปรรูป
class Process_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            # Exit game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'

# Achievement
class Achievement_manu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return 'exit'
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                
# main menu
class Main_menu():
    def __init__(self):
        self.inprocess = True
    
    def run():
        global sound_
        global image_
        # background 
        window.blit(Image().main_bg, (0, 0))

        # newgame botton
        pygame.draw.rect(window, (150,0,150),[220, 100, 380, 100], 3)
        # continue botton
        pygame.draw.rect(window, (0,150,150),[220, 200, 380, 100], 3)
        # credit botton
        pygame.draw.rect(window, (150,150,0),[220, 300, 380, 100], 3)
        # exit botton
        pygame.draw.rect(window, (150,0,0),[220, 400, 380, 100], 3)

        pygame.display.update()
        # loop per second 
        clock = pygame.time.Clock()

        run = True
        while run:


            # loop per second 
            clock.tick(30)
        
            # input - output
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # Botton ------------------------- Botton
                mouse_pos = pygame.mouse.get_pos()

                # ปุ่ม newgame
                newgame_a = (220,100)
                newgame_b = (500,200)
                if is_hit_box(mouse_pos,newgame_a, newgame_b):
                    
                    # วาดปุ่มเรืองแสง
                    pygame.display.update()

                    growing = None

                    if event.type == pygame.MOUSEBUTTONUP:
                        sound_.click.play()
                        return 'newgame'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม continue
                continue_a = (220,200)
                continue_b = (500,300)
                if is_hit_box(mouse_pos,continue_a, continue_b):
                    
                    # เรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        sound_.click.play()
                        return 'load'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม credit
                credit_a = (220,300)
                credit_b = (500,400)
                if is_hit_box(mouse_pos,credit_a, credit_b):
                   
                    # เรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        sound_.click.play()
                        return 'credit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                # ปุ่ม exit
                quit_a = (220,400)
                quit_b = (500,500)
                if is_hit_box(mouse_pos,quit_a, quit_b):
                    
                    # เรืองแสง (ถ้าว่างค่อยทำ)
                    pygame.display.update()

                    if event.type == pygame.MOUSEBUTTONUP:
                        sound_.click.play()
                        return 'exit'
                else:
                    # วาดปุ่ม ปกติ (ถ้าว่างค่อยทำ)
                    pygame.display.update()

# newgame
class Newgame_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run
                
        return run
    
# loadgame
class Load_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run

        return run

# credit
class Credit_menu():
    def __init__(self):
        self.inprocess = True
    
    def run(self):
        global sound_
        global image_
        run = True
        while run:
            for event in pygame.event.get():
                # Exit game 
                if event.type == pygame.QUIT:
                    return not run
                if event.type == pygame.MOUSEBUTTONUP:
                    return run
                
        return run


# Mechanic ----------------------- Mechanic
class Player():
    def __init__(self):
        self.money = 0
        self.player_farm = Player_farm()
        self.inventory = Inventory()

class Inventory():
    def __init__(self):
        # ผัก
        self.wheat = 0
        self.wheat_seed = 0
        self.cucumber = 0
        self.cucumber_seed = 0
        self.tomato = 0
        self.tomato_seed = 0
        self.potato = 0
        self.potato_seed = 0
        self.purplecabbage = 0
        self.purplecabbage_seed = 0
        # ผลไม้
        self.orange = 0
        self.orange_seed = 0
        self.mango = 0
        self.mango_seed = 0
        self.apple = 0
        self.apple_seed = 0
        self.melon = 0
        self.melon_seed = 0
        self.grape = 0
        self.grape_seed = 0
        # แปรรูป
        self.wheat_processed = 0
        self.cucumber_processed = 0
        self.tomato_processed = 0
        self.potato_processed = 0
        self.purplecabbage_processed = 0
        
        self.orange_processed = 0
        self.mango_processed = 0
        self.apple_processed = 0
        self.melon_processed = 0
        self.grape_processed = 0

class Farmland():
    def __init__(self):
        self.size = 4

        
class Plant():
    def __init__(self):
        self.type = None


# Launcher ======================= Launcher ======================= Launcher 
pygame.init()
resolution = (800,600)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cute, Ginger, Cat-ting Stealing Vegetables")


window.fill((255,255,255))
pygame.display.update()

# init resouce manager
sound_ = Sound()
image_ = Image()

# Main Loop ====================== Main Loop ====================== Main Loop 
def main():
    selected = 'main'
    run = True
    while run:
        if selected == 'main':
            main = Main_menu()
            main.run()
        
        if selected == 'newgame':
            main = Newgame_menu()
            main.run()
        
        if selected == 'load':
            main = Load_menu()
            main.run()
        
        if selected == 'credit':
            main = Credit_menu()
            main.run()
        
        if selected == 'player_farm':
            main = Player_farm()
            main.run()
        
        if selected == 'acheivement':
            main = Achievement_manu()
            main.run()
        
        if selected == 'shop':
            main = Shop_menu()
            main.run()

        if selected == 'storage':
            main = Storage_menu()
            main.run()
        
        if selected == 'process':
            main = Process_menu()
            main.run()

        if selected == 'shop':
            main = Shop_menu()
            main.run()

        if selected == 'exit':
            run = False
            
        

# RUN !
main()

# EXIT !
pygame.quit()
