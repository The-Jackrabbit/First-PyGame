# Connor Bottcher (cb4wa) Luke Masters (lsm5fm)

import pygame
import gamebox
import global_stage
import game_final_1
import sponge_run


music1 = gamebox.load_sound('Spongebob_Uke.wav')
music2 = gamebox.load_sound('Spongebob Pizza song.wav')


music2_count = 0
counter = 0
credit_count = 0
play_count = 0
option_count = 0
control_count = 0
sound_count = 0
camera = global_stage.camera
level_1 = 0
level_2 = 0
level_3 = 0
wasd_count = 0
sound_level = 0.5
char1 = gamebox.from_color(10, 10, "red", 50, 5)
char2 = gamebox.from_text(250, 50, "ya Motha", "Cambria", 70, "orange", True, True)
# char3 = gamebox.from_image(100, 100, "http://images6.fanpop.com/
# image/photos/33000000/The-Customer-s-House-krusty-krab-pizza-33032845-512-384.jpg")
char3 = gamebox.from_image(200, 400,
            "http://3219a2.medialib.glogster.com/creeperman913/media"
            "/18/18ee0bb8dd40f9d96af0d3dfd14687f97923fdf2/spongebob.png")
char4 = gamebox.from_text(350, 150, "By Luke and Connor (lsm5fm and cb4wa)", "Cambria", 30, "orange", False, True)
char5 = gamebox.from_text(683, 200, "Press 'P' to Play", "Cambria", 50, "red")
char6 = gamebox.from_text(683, 400, "Press 'O' for Options", "Cambria", 50, "red")
char7 = gamebox.from_text(683, 600, "Press 'C' for Credits", "Cambria", 50, "red")
titlebackground = gamebox.from_image(683, 384, "http://i.imgur.com/liXLthM.png")
titlebackground.size = 1366, 768
pygame.mouse.set_visible(False)


def set_all_volume(keys):
    global sound_count, sound_level
    camera.clear("sky blue")
    if pygame.K_q in keys:
        quit()
    toggle_off = gamebox.from_text(683, 200, "To turn off sound, press 'n'", "Cambria", 40, "red")
    back = gamebox.from_text(125, 50, "press 'b' for back", "Cambria", 30, "red")
    if pygame.K_n in keys:
        music1.stop()
        music2_count = 1
    if pygame.K_b in keys:
        sound_count = 0
        title(keys)
    camera.draw(toggle_off)
    camera.draw(back)
    camera.display()


def control(keys):
    global control_count, wasd_count, arrow_keys_count
    camera.clear("sky blue")
    if pygame.K_q in keys:
        quit()
    txt1 = gamebox.from_text(683, 200, "press '1' to make your controls wasd", "Cambria", 40, "red")
    txt2 = gamebox.from_text(683, 400, "press '2' to make your controls the arrow keys", "Cambria", 40, "red")
    back = gamebox.from_text(125, 50, "press 'b' for back", "Cambria", 30, "red")
    camera.draw(txt1)
    camera.draw(txt2)
    camera.draw(back)
    if pygame.K_b in keys:
        control_count = 0
        title(keys)
    if pygame.K_1 in keys:
        global_stage.wasd_count = 1
    if pygame.K_2 in keys:
        global_stage.wasd_count = 0

    camera.display()


def tick_options(keys):
    global control_count, option_count, sound_count
    camera.clear("sky blue")
    if pygame.K_q in keys:
        quit()
    opt1 = gamebox.from_text(683, 200, "press 't' for controller controls", "Cambria", 40, "red")
    opt2 = gamebox.from_text(683, 500, "press 's' for sound controls", "Cambria", 40, "red")
    pic1 = gamebox.from_image(683, 350, "https://d30y9cdsu7xlg0.cloudfront.net/png/195040-200.png")
    pic2 = gamebox.from_image(683, 650, "http://images.clipartpanda.com/music-note-transparent-background-RTAR6agTL.png")
    back = gamebox.from_text(125, 50, "press 'b' for back", "Cambria", 30, "red")
    pic1.size = 200, 220
    pic2.size = 200, 220
    camera.draw(opt1)
    camera.draw(opt2)
    camera.draw(pic1)
    camera.draw(pic2)
    camera.draw(back)
    if pygame.K_t in keys:
        control_count += 1
    if pygame.K_s in keys:
        sound_count += 1
    if control_count != 0:
        control(keys)
    if pygame.K_b in keys:
        option_count = 0
    if option_count == 0:
        title(keys)
    if sound_count != 0:
        set_all_volume(keys)
    if control_count == 0 and sound_count == 0:
        camera.display()


def tick_creds(keys):
    global credit_count
    cred_char = gamebox.from_text(683, 200,
                                  "A special thanks to the following:  Luther Tychonievich for the gamebox functions", "Cambria", 40, "red")
    back = gamebox.from_text(125, 50, "press 'b' for back", "Cambria", 30, "red")
    camera.clear("sky blue")
    if pygame.K_q in keys:
        quit()
    camera.draw(cred_char)
    camera.draw(back)
    camera.display()
    if pygame.K_b in keys:
        credit_count = 0
    if credit_count == 0:
        title(keys)


def title(keys):
    global credit_count, play_count, option_count, sound_level
    pygame.mixer.music.set_volume(sound_level)
    if pygame.K_q in keys:
        quit()
    camera.clear("red")
    camera.draw(titlebackground)
    camera.draw(char2)
    camera.draw(char4)
    camera.draw(char5)
    camera.draw(char6)
    camera.draw(char7)
    camera.draw(char3)
    if pygame.K_p in keys:
        global_stage.level += 1
    if pygame.K_o in keys:
        option_count += 1
    if pygame.K_c in keys:
        credit_count += 1
    if pygame.K_ESCAPE in keys:
        gamebox.stop_loop()
    if credit_count != 0:
        tick_creds(keys)
    if option_count != 0:
        tick_options(keys)
    if global_stage.level == 1:
        musicplayer1 = music1.play(-1)
        gamebox.timer_loop(30, game_final_1.tick)
    elif global_stage.level == 2:
        music1.stop()
        musicplayer2 = music2.play(-1)
        gamebox.timer_loop(30, sponge_run.sponge_run_function)
    if play_count == 0 and credit_count == 0 and option_count == 0:
        camera.display()

while global_stage.quit_check == 0:
    if global_stage.level == 0:
           gamebox.timer_loop(30, title)
    if global_stage.level == 1:
        music1 = gamebox.load_sound('Spongebob_Uke.wav')
        musicplayer1 = music1.play(-1)
        gamebox.timer_loop(30, game_final_1.tick)
    if global_stage.level == 2:
        music1.stop()
        music2 = gamebox.load_sound('Spongebob Pizza song.wav')
        musicplayer2 = music2.play(-1)
        if music2_count != 0:
            music2.stop()
        gamebox.timer_loop(30, sponge_run.sponge_run_function)
