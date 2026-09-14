import pygame
import sys
import json

pygame.init()

love_level_number = 0
scene = "player_room_day"
save_check = False

#player data
progress = {
    "player_name": "You",
    "love_status": 0,
    "saved": False,
    "scene": "player_room_day",
}

scene = progress["scene"]

try:
    with open("play_data.json", "r", encoding="utf-8") as file:
        progress = json.load(file)
        load_level_number = progress.get("love_status", 0)
        scene = progress.get("scene", "player_room_day")
        save_check = True
except (FileNotFoundError, json.JSONDecodeError):
    save_check = False

# display
screen = pygame.display.set_mode((2400, 1080))
width, height = screen.get_size()
# ====================================

# time
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
# ====================================

#icon, logo and caption
sim_logo_load = pygame.image.load("images/dating_sim_logo.png").convert_alpha()
pygame.display.set_icon(sim_logo_load)
pygame.display.set_caption("A DATE")

logo = pygame.image.load("logo.jpg")
logo_rect = logo.get_rect(center=(width//2, height//2))
# ====================================

#audio
# -- menu music
pygame.mixer.music.load('audio/menu.mp3')
btn_select_sound = pygame.mixer.Sound('audio/btn_select_sound.mp3')
# ====================================

# fonts
font = pygame.font.Font("fonts/BlocksUniverse-Bold.otf", 150)
level_font = pygame.font.Font("fonts/BlocksUniverse-Light.otf", 50)
board_text = pygame.font.Font("fonts/BlocksUniverse-Italic.otf", 100)
# ====================================

# bg
menu_bg_y = 0
menu_bg_load = pygame.image.load("bgs/menu_bg.jpg").convert()
menu_bg_scaled = pygame.transform.scale(menu_bg_load, (2000, 2000))

menu_bg = menu_bg_scaled

menu_bg_pos = (0, 0)

# settings bg
settings_bg_load = pygame.image.load("bgs/settings_bg.jpg").convert()
settings_bg_scaled = pygame.transform.scale(settings_bg_load, (2300, 2300))

settings_bg = settings_bg_scaled

settings_bg_pos = (0, 0)

# player bgs
#day room
player_room_bg_load = pygame.image.load("bgs/player_room_bg.jpg").convert()
player_room_bg_scaled = pygame.transform.scale(player_room_bg_load, (2300, 2300))

player_room_bg = player_room_bg_scaled

player_room_bg_pos = (0, 0)

#night room
player_room_night_bg_load = pygame.image.load("bgs/player_room_night_bg.jpg").convert()
player_room_night_bg_scaled = pygame.transform.scale(player_room_night_bg_load, (2300, 2300))

player_room_night_bg = player_room_night_bg_scaled

player_room_night_bg_pos = (0, 0)
# ====================================

# sprites
# dialogue board
dialogue_board_load = pygame.image.load('images/dialogue_board.png').convert_alpha()
dialogue_board_scaled = pygame.transform.scale(dialogue_board_load, (1100, 500))

dialogue_board = dialogue_board_scaled

dialogue_board_pos = dialogue_board.get_rect(center=(width//2, height//2 + 800))

# love level
love_level_load = pygame.image.load('images/love_level.png').convert_alpha()
love_level_scaled = pygame.transform.scale(love_level_load, (50, 50))

love_level = love_level_scaled

love_level_pos = love_level.get_rect(center=(width//2 - 430, height//2 + 960))

# love level text
love_level_text = level_font.render(str(love_level_number), True, (255, 255, 255))
love_level_text_pos = love_level_text.get_rect(center=(width//2 - 380, height//2 + 960))

# ====================================

# characters
menu_char_load = pygame.image.load('characters/reina_menu.png').convert_alpha()
menu_char_scaled = pygame.transform.scale(menu_char_load, (2000, 2000))

menu_char = menu_char_scaled

menu_char_pos = menu_char.get_rect(center=(width//2 + 200, height//2 + 500))
# ====================================

# menu logo
sim_logo_scaled = pygame.transform.scale(sim_logo_load, (1000, 1000))

sim_logo = sim_logo_scaled

sim_logo_pos = sim_logo.get_rect(center=(width//2, height//2 - 750))
# ====================================

# BUTTONS

# play
play_btn_load = pygame.image.load('images/menu_play_static.png').convert_alpha()
play_btn_scaled = pygame.transform.scale(play_btn_load, (500, 170))

play_btn = play_btn_scaled

play_btn_pos = play_btn.get_rect(center=(width//2, height//2 + 500))

# hover
play_btn_hover_load = pygame.image.load('images/menu_play_hover.png').convert_alpha()
play_btn_hover_scaled = pygame.transform.scale(play_btn_hover_load, (500, 170))

play_btn_hover = play_btn_hover_scaled

play_btn_hover_pos = play_btn_hover.get_rect(center=(width//2, height//2 + 500))

# settings
settings_btn_load = pygame.image.load('images/menu_settings_static.png').convert_alpha()
settings_btn_scaled = pygame.transform.scale(settings_btn_load, (500, 170))

settings_btn = settings_btn_scaled

settings_btn_pos = settings_btn.get_rect(center=(width//2, height//2 + 700))

# hover
settings_btn_hover_load = pygame.image.load('images/menu_settings_hover.png').convert_alpha()
settings_btn_hover_scaled = pygame.transform.scale(settings_btn_hover_load, (500, 170))

settings_btn_hover = settings_btn_hover_scaled

settings_btn_hover_pos = settings_btn_hover.get_rect(center=(width//2, height//2 + 700))

#settings menu
settings_menu_load = pygame.image.load('images/settings_menu.png').convert_alpha()
settings_menu_scaled = pygame.transform.scale(settings_menu_load, (1000, 1500))

settings_menu = settings_menu_scaled

settings_menu_pos = settings_menu.get_rect(center=(width//2, height//2))

# settings music text
settings_menu_music_text = font.render("Mute", True, (255, 255, 255))
settings_menu_music_text_pos = settings_menu_music_text.get_rect(center=(width//2 - 200, height//2 - 500))

# settings button with logo
settings_logo_btn_load = pygame.image.load("images/settings_gear.png").convert_alpha()
settings_logo_btn_scaled = pygame.transform.scale(settings_logo_btn_load, (200, 200))

settings_logo_btn = settings_logo_btn_scaled

settings_logo_btn_pos = settings_logo_btn.get_rect(center=(width//2 + 400, height//2 - 1000))

#hover
settings_logo_btn_hover_load = pygame.image.load("images/settings_gear_hover.png").convert_alpha()
settings_logo_btn_hover_scaled = pygame.transform.scale(settings_logo_btn_hover_load, (200, 200))

settings_logo_btn_hover = settings_logo_btn_hover_scaled

settings_logo_btn_hover_pos = settings_logo_btn_hover.get_rect(center=(width//2 + 400, height//2 - 1000))

#checkbox checked
checkbox_check_load = pygame.image.load('images/checkbox_check.png').convert_alpha()
checkbox_check_scaled = pygame.transform.scale(checkbox_check_load, (200, 200))

checkbox_check = checkbox_check_scaled

checkbox_check_pos = checkbox_check.get_rect(center=(width//2 + 300, height//2 - 500))

#checkbox unchecked
checkbox_uncheck_load = pygame.image.load('images/checkbox_uncheck.png').convert_alpha()
checkbox_uncheck_scaled = pygame.transform.scale(checkbox_uncheck_load, (200, 200))

checkbox_uncheck = checkbox_uncheck_scaled

checkbox_uncheck_pos = checkbox_uncheck.get_rect(center=(width//2 + 300, height//2 - 500))

# return button
return_btn_load = pygame.image.load('images/return_button.png').convert_alpha()
return_btn_scaled = pygame.transform.scale(return_btn_load, (200, 200))

return_btn = return_btn_scaled

return_btn_pos = return_btn.get_rect(center=(width//2 - 400, height//2 - 1000))

#hover
return_btn_hover_load = pygame.image.load('images/return_button_hover.png').convert_alpha()
return_btn_hover_scaled = pygame.transform.scale(return_btn_hover_load, (200, 200))

return_btn_hover = return_btn_hover_scaled

return_btn_hover_pos = return_btn_hover.get_rect(center=(width//2 - 400, height//2 - 1000))

# save button
save_btn_load = pygame.image.load('images/save_button.png').convert_alpha()
save_btn_scaled = pygame.transform.scale(save_btn_load, (200, 200))

save_btn = save_btn_scaled

save_btn_pos = save_btn.get_rect(center=(width//2 + 200, height//2 - 1000))

# hover
save_btn_hover_load = pygame.image.load('images/save_button_hover.png').convert_alpha()
save_btn_hover_scaled = pygame.transform.scale(save_btn_hover_load, (200, 200))

save_btn_hover = save_btn_hover_scaled

save_btn_hover_pos = save_btn_hover.get_rect(center=(width//2 + 200, height//2 - 1000))

# load button
load_btn_load = pygame.image.load('images/menu_load_static.png').convert_alpha()
load_btn_scaled = pygame.transform.scale(load_btn_load, (500, 170))

load_btn = load_btn_scaled

load_btn_pos = load_btn.get_rect(center=(width//2, height//2 + 900))

# hover
load_btn_hover_load = pygame.image.load('images/menu_load_hover.png').convert_alpha()
load_btn_hover_scaled = pygame.transform.scale(load_btn_hover_load, (500, 170))

load_btn_hover = load_btn_hover_scaled

load_btn_hover_pos = load_btn_hover.get_rect(center=(width//2, height//2 + 900))
# ====================================

# launch settings
mode = "loading"
previous_scene = None
menu_music_play = False
running = True
music_mute = False
loaded = False
saved = False
# ====================================

# launch
while running:

# mouse position
    mouse_pos = pygame.mouse.get_pos()
# ====================================

# exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # clicking
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # if menu
                if mode == "menu":
                    if play_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        mode = "play"
                    elif settings_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        mode = "settings"
                    elif save_check and load_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        loaded = True
                        mode = "play"
                # if settings
                elif mode == "settings":
                    if checkbox_check_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        music_mute = not music_mute
                        if music_mute:
                            pygame.mixer.music.set_volume(0)
                        else:
                            pygame.mixer.music.set_volume(1)
                        
                    elif return_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        mode = "menu"
                
                # if play
                elif mode == "play":
                    if return_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        mode = "menu"
                    elif settings_logo_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        mode = "settings"
                    elif save_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        saved = True
                    elif load_btn_pos.collidepoint(event.pos):
                        btn_select_sound.play()
                        loaded = True
                        

# ====================================

# logo
    if mode == "loading" and pygame.time.get_ticks() - time >= 5000:
        mode = "menu"
# ====================================

# music/sound starter
    if mode == "menu" and not menu_music_play:
        pygame.mixer.music.play(-1)
        menu_music_play = True
# ====================================

    screen.fill((0, 0, 0))
    
# saving system
    if saved:
        progress["love_status"] = love_level_number
        progress["scene"] = scene
        progress["saved"] = True
        with open("play_data.json", "w", encoding="utf-8") as file:
            json.dump(progress, file, indent=4, ensure_ascii=False)
        saved = False
        save_check = True

# load system
    if loaded:
        try:
            with open("play_data.json", "r", encoding="utf-8") as file:
                progress = json.load(file)
                love_level_number = progress.get("love_status", 0)
                scene = progress.get("scene", "player_room_day")
                love_level_text = level_font.render(str(love_level_number), True, (255, 255, 255))
        except FileNotFoundError:
            pass
        loaded = False
# ====================================

    
# MODE
    # logo
    if mode == "loading":
        screen.blit(logo, logo_rect)
    # menu
    elif mode == "menu":
        # background
        screen.blit(menu_bg, (0, menu_bg_y))
        screen.blit(menu_bg, (0, menu_bg_y + 640))
        menu_bg_y -= 20
        if menu_bg_y <= -300:
            menu_bg_y = 0
        
        # menu text
        screen.blit(sim_logo, sim_logo_pos)
        
        # reina menu
        screen.blit(menu_char, menu_char_pos)
        
        # play button
        if play_btn_pos.collidepoint(mouse_pos):
            screen.blit(play_btn_hover, play_btn_hover_pos)
        else:
            screen.blit(play_btn, play_btn_pos)

        # settings button
        if settings_btn_pos.collidepoint(mouse_pos):
            screen.blit(settings_btn_hover, settings_btn_hover_pos)
        else:
            screen.blit(settings_btn, settings_btn_pos)
  
        # save check
        if save_check:
            if load_btn_pos.collidepoint(mouse_pos):
                screen.blit(load_btn_hover, load_btn_hover_pos)
            else:
                screen.blit(load_btn, load_btn_pos)
# ====================================

    # settings
    elif mode == "settings":
        # bg
        screen.blit(settings_bg, settings_bg_pos)
        
        #bg menu
        screen.blit(settings_menu, settings_menu_pos)
        
        # settings music text
        screen.blit(settings_menu_music_text, settings_menu_music_text_pos)
        
        # return button
        if return_btn_pos.collidepoint(mouse_pos):
            screen.blit(return_btn_hover, return_btn_hover_pos)
        else:
            screen.blit(return_btn, return_btn_pos)
            
        #checkboxes
        if music_mute:
            screen.blit(checkbox_check, checkbox_check_pos)
        else:
            screen.blit(checkbox_uncheck, checkbox_uncheck_pos)
# ====================================

    # play
    elif mode == "play":
        # SCENES
        if scene == "player_room_day":
            screen.blit(player_room_bg, player_room_bg_pos)
        elif scene == "player_room_night":
            screen.blit(player_room_night_bg, player_room_night_bg_pos)
            
        # dialogue board
        screen.blit(dialogue_board, dialogue_board_pos)
        
        # return button
        if return_btn_pos.collidepoint(mouse_pos):
            screen.blit(return_btn_hover, return_btn_hover_pos)
        else:
            screen.blit(return_btn, return_btn_pos)
        
        # love level on board
        screen.blit(love_level, love_level_pos)
        screen.blit(love_level_text, love_level_text_pos)
        
        # settings button in play
        if settings_logo_btn_pos.collidepoint(mouse_pos):
            screen.blit(settings_logo_btn_hover, settings_logo_btn_hover_pos)
        else:
            screen.blit(settings_logo_btn, settings_logo_btn_pos)

        # save button
        if save_btn_pos.collidepoint(mouse_pos):
            screen.blit(save_btn_hover, save_btn_hover_pos)
        else:
            screen.blit(save_btn, save_btn_pos)
    
# ====================================

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()