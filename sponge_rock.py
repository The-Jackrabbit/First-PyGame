import pygame
import gamebox
import random

#http://www.spongebobia.com/spongebob-captures/content/episodes/galleries/005a%20-%20Pizza%20Delivery/005a%20-%20Pizza%20Delivery%20%28578%29.jpg
#http://www.unitedspongebob.com/pictures/rock/door.jpg
#http://www.rankopedia.com/CandidatePix/163423.gif

x = 800
y = 600
camera = gamebox.Camera(x, y)
music = gamebox.load_sound("Spongebob Pizza Song.wav")
musicplayer = music.play(-1)
sponge = gamebox.from_image(100, 500, "http://img2.wikia.nocookie.net/__cb20120809161518/spongebob/images/a/a0/Pizza_Delivery_Gallery_%2840%29.jpg")
floor = gamebox.from_color(400, 600, "light green", 200000, 100)
start_wall = gamebox.from_color(0, 200, "orange", 200, 1000)
sponge.size = 100,100
sponge.yspeed = 0
sponge.speedx = 0
death_screen = gamebox.from_text(camera.x + 3.5*x/5, 300, "you died.", "Cambria", 30, "red")
walls = [
    floor,
    start_wall
]
rocks = []
counter = 0


def level(keys):
    camera.clear("cyan")
    global x,y,sponge, counter,death_screen
    sponge.speedx = 0
    if pygame.K_RIGHT in keys:
        sponge.speedx += 10
        sponge.x += 10
    if pygame.K_LEFT in keys:
        sponge.speedx -= 10
        sponge.x -= 10
    if pygame.K_DOWN in keys:
        sponge.yspeed += 5
    sponge.yspeed += 1
    sponge.y = sponge.y + sponge.yspeed
    counter += 1
    if len(rocks) < 75:
        if counter % 25 == 0:
            rock = gamebox.from_image(random.randint(200 + 400*(counter/25), 600 +400*(counter/25)), camera.y+250, "patricksrock.png")
            rock.size = random.randint(50, 75), 50
            #rock = gamebox.from_color(random.randint(200 + 400*(counter/25), 600 +400*(counter/25)), camera.y+250, "white", random.randint(50,75), 20)
            rocks.append(rock)

    for wall in walls:
        if sponge.bottom_touches(wall):
            sponge.yspeed = 0
            if pygame.K_SPACE in keys:
                sponge.yspeed = -20
        if sponge.left_touches(wall) or sponge.right_touches(wall):
            if pygame.K_SPACE in keys:
                sponge.yspeed = -10
        if sponge.touches(wall):
            sponge.move_to_stop_overlapping(wall)
        camera.draw(wall)
    for rock in rocks:
        if sponge.touches(rock):
            death_screen.center = camera.center
            camera.draw(death_screen)
            gamebox.pause()
        camera.draw(rock)
    camera.x += 3
    if len(rocks) > 30:
        camera.x += 4
    if len(rocks) > 70:
        camera.x += 2
        sponge.speedx += 10
    camera.draw(sponge)
    camera.draw(floor)
    camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, level)