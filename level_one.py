import pygame
import gamebox
import global_stage
x = 1366
y = 768

#if global_stage.level == 1:

level = global_stage.level
origin_x = 260
origin_y = 543
death_move_check = 0
camera = global_stage.camera
background = []
check = 0
stage = 1
not_lame = gamebox.load_sound('notlame_louder.wav')
hit_check = 0
hit_moment = 0
hit_interval = 0
circle_stage = 1
face_check = 0
time = 0
jump_check = 0
seconds = 0
minutes = 0
jf_stage = 1
spat_stage = 1
secretformula_check = 0
spat_check = 0
stick_check = 0
health = 3
bear_stage = 1
move_check = 0
platforms = [gamebox.from_image(5385, y/2 - y/6, "platform_kelp.png"),
             gamebox.from_image(5180,  y/2 - y/6, "platform_kelp.png")]
character = gamebox.from_image(origin_x, origin_y, 'spongebob_run.png')
ground = gamebox.from_color(0, y, "Peach Puff", 100000, 70)
house = gamebox.from_image(5320, y - 240, "house.png")
wall = [gamebox.from_color(0, y, "White", 520, 1000),
        gamebox.from_color(10000, y, "White", 950, 1000)]
bear_list = [gamebox.from_image(6900, y - y/10, "seabear_1.png"), gamebox.from_image(8500, y - y/10, "seabear_1.png"), gamebox.from_image(4500, y - y/10, "seabear_1.png"),
             gamebox.from_image(5000, y - y/10, "seabear_1.png"), gamebox.from_image(4000, y - y/10, "seabear_1.png"),
             gamebox.from_image(3500, y - y/10, "seabear_1.png"), gamebox.from_image(2500, y - y/10, "seabear_1.png"),
             gamebox.from_image(3000, y - y/10, "seabear_1.png")]
jump_list = [ground]
jf_list = [gamebox.from_image(5550, y/2 + 20, "jellyfish_1.png"), gamebox.from_image(5575, y/2 + 20, "jellyfish_1.png"),
           gamebox.from_image(2850, y/2 + 20, "jellyfish_1.png"), gamebox.from_image(2875, y/2 + 20, "jellyfish_1.png")]
kelp_list = []
for xy in range(4):
    kelp_list.append(gamebox.from_image(2550 + xy*30, y - y/15, "ground_kelp.png"))
    kelp_list.append(gamebox.from_image(2050 + xy*30, y - y/15, "ground_kelp.png"))
for x in range(3):
    platforms.append(gamebox.from_image(2100 + x*500, y/2+y/7, "platform_kelp.png"))
    platforms.append(gamebox.from_image(2100 + x*500, y/2 - y/7, "platform_kelp.png"))
    platforms.append(gamebox.from_image(3500 + x*240, y/2 - y/7, "platform_kelp.png"))
    platforms.append(gamebox.from_image(4900 + x*240, y/2 + y/7, "platform_kelp.png"))
    platforms.append(gamebox.from_image(6700 + x*240, 200, "platform_kelp.png"))
for i in range(4):
    jf_list.append(gamebox.from_image(1700 + 25*i, 1.28*440, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(4200 + 25*i, 1.28*320, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(4350 + 25*i, 1.28*370, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(4500 + 25*i, 1.28*420, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(4650 + 25*i, 1.28*490, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(6000 + 25*i, 1.28*370, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(6300 + 25*i, 1.28*450, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(6000 + 25*i, 1.28*550, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(6300 + 25*i, 1.28*270, "jellyfish_1.png"))
for i in range(2):
    jf_list.append(gamebox.from_image(600 + i*25, 1.28*520, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(800 + i*25, 1.28*500, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(1000 + i*25, 1.28*480, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(1200 + i*25, 1.28*460, "jellyfish_1.png"))
    jf_list.append(gamebox.from_image(1400 + i*25, 1.28*440, "jellyfish_1.png"))


for jellyfish in jf_list:
    jump_list.append(jellyfish)
for platform in platforms:
    jump_list.append(platform)
for i in range(50):
    background.append(gamebox.from_image(x/2 + 1000*i, y/2, "backgrund.jpg"))
for j in range(len(background)):
    background[j].scale_by(1.3)

character.yspeed = 0
x_coord = 0


def tick(keys):
    global death_move_check, hit_interval, hit_moment, hit_check, health, secretformula_check, stick_check,\
        move_check, x, y, stage, face_check, time, seconds, minutes, jf_stage, check, \
        spat_stage, spat_check, bear_stage, circle_stage, x_coord, level

    hud = [gamebox.from_color(character.x, 0, "White", 100000, 120)]
    hit_interval += 1
    character.xspeed = 0
    character.yspeed += 1
    circle_check = 0
    time += 1
    jf_stage += 1/3
    spat_stage += 1/3
    bear_stage += 1/3
    if circle_stage >= 9:
        circle_stage = 8
    if time == 30:
        seconds += 1
        move_check = 0
    if time == 60:
        check = 0
        time = 0
        seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if int(seconds) < 10:
        second = '0{}'.format(str(seconds))
    else:
        second = str(seconds)
    if hit_moment + 30 == hit_interval:
        hit_check = 0
    for jellyfish in jf_list:
        if time < 30:
            jellyfish.yspeed = -2
        else:
            jellyfish.yspeed = 2
        jellyfish.y = jellyfish.y + jellyfish.yspeed
    for bear in bear_list:
        if time < 30:
            bear.speedx = -10
        else:
            bear.speedx = 10
        bear.x = bear.x + bear.speedx
    character.y = character.y + character.yspeed


    # ----- GEN ANIMATION -----
    timer = gamebox.from_text(character.x - 225, y/25, "{}".format(str(int(minutes))) + ":{}".format(second), "haettenschweiler", 40, "Black")
    hud.append(timer)
    tie_hud = gamebox.from_image(character.x + 400, y/20 - 20, "tie_hud.png")
    tie_hud.scale_by(0.8)
    hud.append(tie_hud)
    secretformula_hud_file = 'secretformula_check{}'.format(str(secretformula_check)) + ".png"
    secretformula_hud = gamebox.from_image(character.x - 50, y/20 - 5, secretformula_hud_file)
    hud.append(secretformula_hud)
    health_hud_file = 'health_hud_1.png'
    health_hud_a = gamebox.from_image(character.x + 850, y/20 - 8, health_hud_file)
    health_hud_b = gamebox.from_image(character.x + 925, y/20 - 8, health_hud_file)
    health_hud_c = gamebox.from_image(character.x + 1000, y/20 - 8, health_hud_file)
    if health <= 2:
        health_hud_a = gamebox.from_image(character.x + 850, y/20 - 8, 'health_hud_0.png')
    if health <= 1:
        health_hud_b = gamebox.from_image(character.x + 925, y/20 - 8, 'health_hud_0.png')
    if health <= 0:
        health_hud_c = gamebox.from_image(character.x + 1000, y/20 - 8, 'health_hud_0.png')
    hud.append(health_hud_a)
    hud.append(health_hud_b)
    hud.append(health_hud_c)
    stick_hud_file = "stick_check{}".format(str(stick_check)) + ".png"
    stick_hud= gamebox.from_image(character.x - 150, y/20 - 5, stick_hud_file)
    hud.append(stick_hud)
    spat_hud_file = "spat_check{}".format(str(spat_check))+".png"
    spat_hud = gamebox.from_image(character.x - 100, y/20, spat_hud_file)
    hud.append(spat_hud)
    if stage >= 7:
        stage = 1
    if spat_stage >= 4 or bear_stage >= 4:
        spat_stage = 1
        bear_stage = 1
    if int(jf_stage) == 8:
        jf_stage = 1
    sb = 'running_{}'.format(str(int(stage)))+'.png'
    character_an = gamebox.from_image(character.x, character.y - 10, sb)
    character_an.scale_by(.5)
    jf_file = 'jellyfish_{}'.format(str(int(jf_stage)))+'.png'
    jellyfish_an = []
    secretformula_file = 'secretformula_{}'.format(str(int(spat_stage)))+".png"
    secretformula = gamebox.from_image(7500, 700, secretformula_file)
    spat_file = 'spatula_{}'.format(str(int(spat_stage)))+".png"
    spatula = gamebox.from_image(5100, 100, spat_file)
    stick_file = 'stick_{}'.format(str(int(spat_stage)))+".png"
    stick = gamebox.from_image(2100, 100, stick_file)
    circle = gamebox.from_image(character.x, character.y + 30, 'circle_8.png')
    bear_an = []
    seabear_file = 'seabear_{}'.format(str(int(bear_stage)))+".png"
    # ----- DRAW DISTANCE -----
    for bear in bear_list:
        if character.x + 1123 > bear.x and character.x - 300 < bear.x:
            bear_an.append(gamebox.from_image(bear.x, bear.y, seabear_file))
    for seabear in bear_an:
        if time > 30:
            seabear.flip()
    for jellyfish in jf_list:
        if character.x + 1123 > jellyfish.x and character.x - 300 < jellyfish.x:
            jellyfish_an.append(gamebox.from_image(jellyfish.x, jellyfish.y, jf_file))
    if pygame.K_q in keys:
        quit()
    #  ----- WASD INPUT -----
    if character.touches(ground) and stick_check == 1:
        if pygame.K_c in keys:
            circle_check = 1
        else:
            circle_check = 0
    if global_stage.wasd_count != 0 and health > 0:
        if pygame.K_d in keys and circle_check == 0:
            character.xspeed += 9.5
            character.x += 9.5
            for item in hud:
                item.speedx += 9.5
            if face_check == 1:
                character_an.flip()
                face_check = 0
        if pygame.K_a in keys and circle_check == 0:
            character.speedx -= 9.5
            character.x -= 9.5
            for item in hud:
                item.speedx -= 9.5
            if face_check == 0:
                character_an.flip()
                face_check = 1


        # -----WASD COLLISION -----
        for object in jump_list:
            if character.bottom_touches(object):
                if pygame.K_a not in keys and pygame.K_d not in keys:
                    stage = 1
                if pygame.K_a in keys or pygame.K_d in keys and pygame.K_SPACE not in keys:
                    stage += 1/1.3
                character.yspeed = 0
                character.move_to_stop_overlapping(object)
                if pygame.K_SPACE in keys:
                    stage = 5
                    character.yspeed = -16

    #  ----- ARROW INPUT -----
    if global_stage.wasd_count == 0 and health > 0:
        if pygame.K_RIGHT in keys and circle_check == 0:
            character.xspeed += 9.5
            character.x += 9.5
            for item in hud:
                item.speedx += 9.5
            if face_check == 1:
                character_an.flip()
                face_check = 0
        if pygame.K_LEFT in keys and circle_check == 0:
            character.speedx -= 9.5
            character.x -= 9.5
            for item in hud:
                item.speedx -= 9.5
            if face_check == 0:
                character_an.flip()
                face_check = 1


        # ----- ARROW COLLISION -----
        for object in jump_list:
            if character.bottom_touches(object):
                if pygame.K_LEFT not in keys and pygame.K_RIGHT not in keys:
                    stage = 1
                if pygame.K_LEFT in keys or pygame.K_RIGHT in keys and pygame.K_SPACE not in keys:
                    stage += 1/1.3
                character.yspeed = 0
                character.move_to_stop_overlapping(object)
                if pygame.K_SPACE in keys:
                    stage = 5
                    character.yspeed = -16
    for w in wall:
        if character.touches(w):
            character.move_to_stop_overlapping(w)
    if character.touches(spatula) and spat_check == 0:
        spat_check = 1
        not_lame.play()
    if character.touches(stick) and stick_check == 0:
        stick_check = 1
        not_lame.play(0)
    if character.touches(secretformula) and secretformula_check == 0:
        secretformula_check = 1
        not_lame.play(0)
    for platform in platforms:
        if character.bottom_touches(platform):
            if pygame.K_DOWN in keys:
                character.y = character.y + y/10


    # ----- DEATH CHECK -----
    for jellyfish in jf_list:
        if character.bottom_touches(jellyfish):
            stage = 2
        if character.top_touches(jellyfish) and hit_check == 0:
            health -= 1
            hit_check = 1
            hit_moment = hit_interval
    for seabear in bear_an:
        if character.touches(seabear) and hit_check == 0 and circle_check == 0:
            health -= 1
            hit_check = 1
            hit_moment = hit_interval
        if circle_check == 1 and character.touches(seabear):
            health += 0


    # ----- DRAWING -----
    camera.clear("Black")
    if health != 0:
        for entry in background:
            camera.draw(entry)
        camera.draw(ground)
        camera.draw(house)
        for jellyfish in jellyfish_an:
            camera.draw(jellyfish)
        if secretformula_check == 0:
            camera.draw(secretformula)
        if stick_check == 0:
            camera.draw(stick)
        if spat_check == 0:
            camera.draw(spatula)
        for seabear in bear_an:
            camera.draw(seabear)
        if face_check == 1:
            character_an.flip()
        if circle_check == 1:
            camera.draw(circle)
        camera.draw(character_an)
        for entry in hud:
            camera.draw(entry)
        for platform in platforms:
            if character.x + 1300 > platform.x and character.x - 400 < platform.x:
                camera.draw(platform)
    else:
        if death_move_check == 0:
            camera.move(19600, 0)
            death_move_check = 1
        death_screen = gamebox.from_image(character.x + 20000, 400, "deathscreen.jpg")
        quit_text = gamebox.from_text(character.x + 20200, 400, "Press q to quit", "Cambria",100,  "White")
        camera.draw(death_screen)
        camera.draw(quit_text)

    camera.move(character.speedx, 0)
    if health == 0:
        x_coord = character.x
    if stick_check == 1 and spat_check == 1 and secretformula_check == 1 and character.x >= 9400:
        camera.draw(gamebox.from_image(9750, 400,"continue.png"))
        level = 2
    camera.display()
    spat_check = 1
    secretformula_check = 1
    stick_check = 1
    if health == 0:
        if death_move_check == 0:
            camera.move(20000, 0)
            death_move_check = 1
        death_screen = gamebox.from_image(character.x + 20000, 400, "deathscreen.jpg")
        camera.draw(death_screen)
        #gamebox.pause()
        '''
        character_an = gamebox.from_image(character.x, character.y, 'crying.png')
        gamebox.pause()
        '''



ticks_per_second = 30
global_stage.level = level

# gamebox.timer_loop(ticks_per_second, tick)
