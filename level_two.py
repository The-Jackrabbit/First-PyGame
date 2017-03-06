import gamebox
import pygame
import random
import global_stage
import level_one

x = 1300
y = 600

level = global_stage.level
camera = global_stage.camera

if global_stage.level == 2:
    musicplayer2 = music2.play(-1)
origin_x = 120
origin_y = 465
background = []
check = 0
stage = 1
not_lame = gamebox.load_sound('notlame.wav')
hit_check = 0
hit_moment = 0
death_move_check = 0
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
pizza_health = 8
bear_stage = 1
move_check = 0
cockroach_list = []
platform_list = []
c_stage = 1
rock_stage = 1
customer_house = gamebox.from_image(35320, y-30, "customers_house.png")
customer_house.scale_by(2)
rock = gamebox.from_image(origin_x, origin_y, "rock_4.png")
ground = gamebox.from_color(0, y + 230, "Peach Puff", 100000, 150)
sand = []
house = [gamebox.from_image(5320, y - 100, "track.png"), gamebox.from_image(21320, y - 100, "track.png"),
         gamebox.from_image(37320, y - 100, "track.png")]
wall = [gamebox.from_color(0, y, "White", 520, 1000),
        gamebox.from_color(10000, y, "White", 520, 1000)]

cockroach_an = []

for i in range(1, 50):
    background.append(gamebox.from_image(x/2 + 1000*(i - 1), y/2, "backgrund.jpg"))
    sand.append(gamebox.from_image(x, y+140, "ground.png"))
    if i < 2 or i > 3:
        cockroach = gamebox.from_image(500 + random.randint(1, 3)*i*1000, 180 + 550, "patricksrock.png")
        cockroach.width = random.randint(50, 130)
        cockroach.height = cockroach.width*random.randint(75, 125)*0.01
        cockroach_list.append(cockroach)


for j in range(len(background)):
    background[j].scale_by(1.3)
rock.speedx = 20
rock.speedy = 1
cockroach_count = 0

for i in range(5):
    platform_list.append(gamebox.from_image(2200 + 240*i, 180 + 500, "race_kelp.png"))
    platform_list.append(gamebox.from_image(3400 + 240*i, 180 + 400, "race_kelp.png"))
    platform_list.append(gamebox.from_image(2200 + random.randint(1, 15)*2400*i, 180 + 500, "race_kelp.png"))


def sponge_run_function(keys):
    global death_move_check, cockroach_count, hit_moment, hit_interval, hit_check, pizza_health, c_stage, jump_check, time, rock_stage
    platform_object = []
    if pygame.K_q in keys:
        quit()
    platform_object.append(ground)
    for platform in platform_list:
        platform_object.append(gamebox.from_color(platform.x, platform.y + 15, "white", 240, 100))
    hit_interval += 1
    time += 2
    rock.yspeed += 1
    if hit_interval == 2 and global_stage.level == 2 and level_one.spat_check == 1:
        camera.move(-9200, 0)
    if pygame.K_DOWN in keys:
        rock.yspeed += 4
    c_stage += 1/1.7
    if hit_interval == hit_moment + 25:
        hit_check = 0
    if c_stage >= 4:
        c_stage = 1

    if time == 30:
        time = 0
        jump_check = 0
    if rock.bottom_touches(ground):
        rock_stage += 1/1.2
    if int(rock_stage) >= 4:
        rock_stage = 1

    if not rock.bottom_touches(ground):
        rock_stage = 4
    rock.x = rock.x + rock.speedx
    rock.y = rock.y + rock.speedy
    '''
    for platform in platform_object:
        platform.y = platform.y + platform.yspeed
    '''
    # ----- COLLISION ------
    for cockroach in cockroach_list:
        if rock.touches(cockroach) and hit_check == 0:
            hit_moment = hit_interval
            pizza_health -= 1
            hit_check = 1
    if rock.x > 35250:
        quit()
    for platform in platform_object:
        if rock.bottom_touches(platform):
            rock.yspeed = 0
            rock.move_to_stop_overlapping(platform)
            if platform != platform_object[0]:
                platform.y += 100
            if pygame.K_SPACE in keys:
                rock.yspeed = -20
                jump_check = 1

        if rock.right_touches(platform) and hit_check == 0:
            pizza_health -= 1
            hit_check = 1
            hit_moment = hit_interval

    # ----- GEN ANIMATION -----
    if pizza_health > 0:
        health_file = 'pizza_health_{}'.format(pizza_health) + ".png"
    else:
        health_file = 'pizza_health_1.png'
    health_hud = gamebox.from_image(rock.x + 4*x/5, 100, health_file)
    rock_file = 'rock_{}'.format(int(rock_stage)) + '.png'
    rock_an = gamebox.from_image(rock.x, rock.y, rock_file)
    camera.clear("White")
    if hit_check == 1:
        rock_stage = 4
        rock.xspeed = 15
    else:
        rock.xspeed = 25
    for shift in range(3):
        if hit_check == 1 and hit_interval >= hit_moment + shift*4 and hit_interval < hit_moment + (shift+1)*4:
            rock_an.rotate(random.randint(-30, 5))
    # ----- DRAWING ------

    camera.clear("Black")
    if pizza_health > 0:
        for platform in platform_object:
            camera.draw(platform)
        for entry in background:
            camera.draw(entry)
        for entry in house:
            camera.draw(entry)
        camera.draw(customer_house)
        for platform in platform_list:
            camera.draw(platform)
        camera.draw(rock_an)
        camera.move(rock.xspeed, 0)
        for cockroach in cockroach_list:
            if rock.x + 1300 > cockroach.x and rock.x - 300 < cockroach.x:
                camera.draw(cockroach)
        camera.draw(health_hud)
    else:
        rock.xspeed = 0
        if death_move_check == 0:
            camera.move(19440, 0)
            death_move_check = 1
        death_screen = gamebox.from_image(rock.x + 20000, 400, "deathscreen.jpg")
        quit_text = gamebox.from_text(rock.x + 20200, 400, "Press q to quit", "Cambria",100,  "White")
        camera.draw(death_screen)
        camera.draw(quit_text)
    camera.display()

gamebox.timer_loop(30, sponge_run_function)
