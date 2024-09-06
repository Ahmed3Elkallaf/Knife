import pygame
import random
import winsound
pygame.font.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Knife game")

run = True
clock = pygame.time.Clock()

knife_img = pygame.transform.rotate(pygame.transform.flip(pygame.transform.scale(pygame.image.load("knife.png"),(100,40)),False,True),90)
knife2_img = pygame.transform.scale(pygame.image.load("knife2.png"),(30,120))
knife3_img = pygame.transform.scale(pygame.image.load("knife3.png"),(30,140))
knife4_img = pygame.transform.scale(pygame.image.load("knife4.png"),(30,140))
knife5_img = pygame.transform.scale(pygame.image.load("knife5.png"),(30,140))
knife6_img = pygame.transform.scale(pygame.image.load("knife6.png"),(30,140))
knife7_img = pygame.transform.scale(pygame.image.load("knife7.png"),(30,140))
knife8_img = pygame.transform.scale(pygame.image.load("knife8.png"),(30,140))
knife9_img = pygame.transform.scale(pygame.image.load("knife9.png"),(30,140))
knife10_img = pygame.transform.scale(pygame.image.load("minecraft_diamond_sword.png"),(60,130))
knife11_img = pygame.transform.scale(pygame.image.load("flame sword.png"),(60,170))


knife_skin = [knife_img,knife2_img,knife3_img,knife4_img,knife5_img,knife6_img,knife7_img,knife8_img,knife9_img,knife10_img,knife11_img]
knife_type = 0

knife_x = 350
knife_y = 400
throw = False
knife_speed = 10
knife_hitbox = pygame.Rect((knife_x,knife_y,100,40))

Target_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Target.png"),(80,80)),90)
Target = Target_img.get_rect()
Target.x = 300
Target.y = random.randint(0,200)
Target_speed = 5

right = True

screen_display = 1
FONT = pygame.font.SysFont("Timer",80)
FONT2 = pygame.font.SysFont("Timer",40)
FONT3 = pygame.font.SysFont("Consolas",40)
play_button = pygame.Rect((295,240,160,70))
How_to_play_button = pygame.Rect((10,10,100,30))
skin_button = pygame.Rect((295,340,160,70))
menu_button = pygame.Rect((700,20,100,30))
exit_button = pygame.Rect((295,440,160,70))

# knife checkbox
checkbox = pygame.Rect((40,100,30,120))
checkbox2 = pygame.Rect((120,100,30,140))
checkbox3 = pygame.Rect((200,100,30,140))
checkbox4 = pygame.Rect((40,280,30,140))
checkbox5 = pygame.Rect((120,280,30,140))
checkbox6 = pygame.Rect((200,280,30,140))
checkbox7 = pygame.Rect((280,100,30,140))
checkbox8 = pygame.Rect((280,280,30,140))
checkbox9 = pygame.Rect((360,100,30,140))
checkbox10 = pygame.Rect((40,440,60,130))

def draw_checkboxes():
    pygame.draw.rect(screen,(0,0,0),checkbox)
    pygame.draw.rect(screen,(0,0,0),checkbox2)
    pygame.draw.rect(screen,(0,0,0),checkbox3)
    pygame.draw.rect(screen,(0,0,0),checkbox4)
    pygame.draw.rect(screen,(0,0,0),checkbox5)
    pygame.draw.rect(screen,(0,0,0),checkbox6)
    pygame.draw.rect(screen,(0,0,0),checkbox7)
    pygame.draw.rect(screen,(0,0,0),checkbox8)
    pygame.draw.rect(screen,(0,0,0),checkbox9)
    pygame.draw.rect(screen,(0,0,0),checkbox10)

score = 0
loop_time = 0


while run:
    if screen_display == 2:   # game loop
        pygame.draw.rect(screen,("green"),knife_hitbox)
        screen.fill(("white"))
        clock.tick(60)
        screen.blit(Target_img,Target)
        screen.blit(knife_skin[knife_type],(knife_x,knife_y))

        knife_hitbox.x = knife_x
        knife_hitbox.y = knife_y

        pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            throw = True

        if throw:
            knife_y -= knife_speed


        if Target.right >= 800:
            right = True
        elif Target.x <= 0:
            right = False

        if right:
            Target.x -= Target_speed
        else:
            Target.x += Target_speed


        if knife_hitbox.colliderect(Target):
            throw = False
            knife_x = 350
            knife_y = 400
            Target.y = random.randint(0,200)
            Target_speed += 0.2
            score += 1
            winsound.PlaySound("knife throw.wav",1)

        if knife_y <= 0:
            throw = False
            knife_x = 350
            knife_y = 400
            Target_speed += 0.2
            score -= 1

        if key[pygame.K_ESCAPE]:
            exit()

        if key[pygame.K_m]:
            screen_display = 1
            score = 0

        pygame.draw.rect(screen,("green"),menu_button)
        menu_text = FONT2.render(f"MENU" , 1 , "black")
        screen.blit(menu_text,(700,23))

        if pygame.mouse.get_pressed()[0] and menu_button.collidepoint(pos):
            screen_display = 1
            score = 0

        loop_time += 1

        score_text = FONT3.render(f"Score: {round(score)}" , 5 , "black")
        screen.blit(score_text,(10,10))

        if key[pygame.K_0]:
            knife_type = 0

        if key[pygame.K_1]:
            knife_type = 1

        if key[pygame.K_2]:
            knife_type = 2

        if key[pygame.K_3]:
            knife_type = 3

        if key[pygame.K_4]:
            knife_type = 4

        if key[pygame.K_5]:
            knife_type = 5

        if key[pygame.K_6]:
            knife_type = 6

        if key[pygame.K_7]:
            knife_type = 7

        if key[pygame.K_8]:
            knife_type = 8

        if key[pygame.K_9]:
            knife_type = 9

        if key[pygame.K_LSHIFT] and key[pygame.K_k]:
            knife_type = 10

        if score >= 50:
            knife_type = 10

        if knife_type == 10:
            knife_speed = 20
        else:
            knife_speed = 10


    if screen_display == 1:  # menu
        screen.fill(("white"))
        clock.tick(60)
        pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] and play_button.collidepoint(pos):
            screen_display = 2
            Target_speed = 5
            Target.y = random.randint(0,200)

        pygame.draw.rect(screen,("yellow"),play_button)
        pygame.draw.rect(screen,("green"),skin_button)
        pygame.draw.rect(screen,("blue"),How_to_play_button)
        pygame.draw.rect(screen,("red"),exit_button)
        play_text = FONT.render(f"PLAY" , 1 , "black")
        screen.blit(play_text,(300,250))
        exit_text = FONT.render(f"EXIT" , 1 , "black")
        screen.blit(exit_text,(300,450))
        skin_text = FONT.render(f"SKIN" , 1 , "black")
        screen.blit(skin_text,(300,350))
        Help_text = FONT2.render(f"HELP" , 1 , "white")
        screen.blit(Help_text,(20,13))

        if pygame.mouse.get_pressed()[0] and exit_button.collidepoint(pos):
            exit()

        if pygame.mouse.get_pressed()[0] and skin_button.collidepoint(pos):
            screen_display = 3

        if key[pygame.K_RETURN]:
            screen_display = 2
            Target_speed = 5
            Target.y = random.randint(0,200)

        if key[pygame.K_ESCAPE]:
            exit()

        if key[pygame.K_s]:
            screen_display = 3

        if pygame.mouse.get_pressed()[0] and How_to_play_button.collidepoint(pos):
            screen_display = 4


    if screen_display == 3:   # skin screen
        draw_checkboxes()
        screen.fill(("white"))
        pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()

        pygame.draw.rect(screen,("green"),menu_button)
        menu_text = FONT2.render(f"MENU" , 1 , "black")
        screen.blit(menu_text,(700,23))

        # knife skins
        screen.blit(knife_skin[0],(40,100))
        screen.blit(knife_skin[1],(120,100))
        screen.blit(knife_skin[2],(200,100))
        screen.blit(knife_skin[3],(40,280))
        screen.blit(knife_skin[4],(120,280))
        screen.blit(knife_skin[5],(200,280))
        screen.blit(knife_skin[6],(280,100))
        screen.blit(knife_skin[7],(280,280))
        screen.blit(knife_skin[8],(360,100))
        screen.blit(knife_skin[9],(40,440))

        if pygame.mouse.get_pressed()[0] and menu_button.collidepoint(pos):
            screen_display = 1

        if pygame.mouse.get_pressed()[0] and checkbox.collidepoint(pos):
            knife_type = 0
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox2.collidepoint(pos):
            knife_type = 1
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox3.collidepoint(pos):
            knife_type = 2
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox4.collidepoint(pos):
            knife_type = 3
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox5.collidepoint(pos):
            knife_type = 4
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox6.collidepoint(pos):
            knife_type = 5
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox7.collidepoint(pos):
            knife_type = 6
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox8.collidepoint(pos):
            knife_type = 7
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox9.collidepoint(pos):
            knife_type = 8
            winsound.PlaySound("knife sound.wav",1)

        if pygame.mouse.get_pressed()[0] and checkbox10.collidepoint(pos):
            knife_type = 9
            winsound.PlaySound("knife sound.wav",1)
            
        if key[pygame.K_m]:
            screen_display = 1

        if key[pygame.K_ESCAPE]:
            exit()

    if screen_display == 4:   # how to play screen
        screen.fill(("white"))
        pos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] and menu_button.collidepoint(pos):
            screen_display = 1

        if key[pygame.K_m]:
            screen_display = 1
            score = 0
        
        How_to_play_img = pygame.transform.scale(pygame.image.load("htp.png"),(800,400))
        screen.blit(How_to_play_img,(0,0))

        pygame.draw.rect(screen,("green"),menu_button)
        menu_text = FONT2.render(f"MENU" , 1 , "black")
        screen.blit(menu_text,(700,23))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    pygame.display.update()