# import pygame
# import buttons

# class MainMenu():
#     def __init__(width, height):
#         game_paused = False
#         menu_state = "main"
#         sound_state = True
#         screen_width = width
#         screen_height = height
#         font = pygame.font.SysFont("arialblack", 40)
#         TEXT_COL = (255,255,255)


#         resume_img = pygame.image.load("assets/resume.png").convert_alpha()
#         resume_button = buttons.Button(screen_width/2-100, screen_height/3+50, resume_img, 8)

#         home_img = pygame.image.load("assets/Home.png").convert_alpha()
#         home_button = buttons.Button(screen_width/2+30, screen_height/2+98, home_img, 6)

#         setting_img = pygame.image.load("assets/settings.png").convert_alpha()
#         settings_button = buttons.Button(screen_width/2-150, screen_height/2+100, setting_img, 6)

#         sound_img = pygame.image.load("assets/sound.png").convert_alpha()
#         sound_button = buttons.Button(screen_width/2-100, screen_height/3+50, sound_img, 6)

#         nosound_img = pygame.image.load("assets/nosound.png").convert_alpha()
#         nosound_button = buttons.Button(screen_width/2-100, screen_height/3+50, nosound_img, 6)




#     def draw_text(text, font, text_col, x, y, screen):
#         img = font.render(text, True, text_col)
#         screen.blit(img, (x,y))


#     if game_paused == True:
#             if menu_state == "main":
#                 if resume_button.draw(screen):
#                     game_paused = False
#                 if settings_button.draw(screen):
#                     menu_state = "settings"
#                 if home_button.draw(screen):
#                     run = False
            
#             if menu_state == "settings":
#                 if sound_state == True:
#                     if sound_button.draw(screen):
#                         sound_state = False
#                 else:
#                     if nosound_button.draw(screen):
#                         sound_state = True
#         else:
#             draw_text("Press ECHAP to pause", font, TEXT_COL, screen_width/3,screen_height/2)