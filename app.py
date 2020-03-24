import pygame
import os
from time import sleep
from random import randint

pygame.init()

#Size of things
screen_width = 800
screen_height = 600

screen_size = (screen_width, screen_height)
image_size = (120, 100)

#Colors
powderblue = (176,224,230)
white = (255,255,255)
black = (0,0,0)

#Positions
troll_pos_x = 320
troll_pos_y = 480

step_of_troll = 10
size_of_ball = 10


main_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("testgame")
main_screen.fill(powderblue)

#Trollface pics
troll_face = pygame.image.load(os.path.join('/home/sup/code/python/pygame_things/images/', 'troll.png'))
troll_face = pygame.transform.scale(troll_face, image_size)

sad_troll = pygame.image.load(os.path.join('/home/sup/code/python/pygame_things/images/', 'sad_troll.png'))
sad_troll = pygame.transform.scale(sad_troll, image_size)

def clear_screen():
	main_screen.fill(powderblue)
	main_screen.blit(troll_face, (troll_pos_x, troll_pos_y))
	pygame.display.update()

def draw_random_ball():
	pygame.draw.circle(main_screen, black, (randint(11,screen_width -11),randint(11,screen_height -11)), size_of_ball)

def move_face(suunta, num):
	main_screen.fill(powderblue)
	if suunta == "x":
		global troll_pos_x
		troll_pos_x += num
	elif suunta == "y":
		global troll_pos_y
		troll_pos_y += num
	print(f'({troll_pos_x} {troll_pos_y})')
	main_screen.blit(troll_face, (troll_pos_x, troll_pos_y))
	pygame.display.update()

face_atm = troll_face

run = True
while run:

	pygame.time.delay(10)

	#Move while pressed
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		move_face("y", -step_of_troll)
	if keys[pygame.K_DOWN]:
		move_face("y", step_of_troll)
	if keys[pygame.K_LEFT]:
		move_face("x", -step_of_troll)
	if keys[pygame.K_RIGHT]:
		move_face("x", step_of_troll)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		#Key inputs
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False
			if event.key == pygame.K_SPACE:
				if face_atm != troll_face:
					face_atm = troll_face
				else:
					face_atm = sad_troll
				pygame.display.update()
			if event.key == pygame.K_1:
				for lol in range(1000):
					draw_random_ball()
					pygame.display.update()
			if event.key == pygame.K_2:
				clear_screen()
					

	main_screen.blit(face_atm, (troll_pos_x, troll_pos_y))
	pygame.display.update()

pygame.quit()