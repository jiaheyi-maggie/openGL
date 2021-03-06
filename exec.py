import pygame
from OpenGL.GL import *
from OpenGL.raw.GLU import *
from pygame.locals import *
import cube

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -40)
    #glRotatef(25, 2, 1, 0)

    object_passed = False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5, 0.0, 0.0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5, 0.0, 0.0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, -0.5, 0.0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 0.5, 0.0)
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                if event.button == 4: #forward mouse wheel roll
#                    glTranslatef(0, 0, 0.5)
#                if event.button == 5:
#                    glTranslatef(0, 0, -0.5)

        #glRotatef(1, 3, 1, 1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX) #get current location
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        if camera_z < -1:
            object_passed = True

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(0, 0, 0.50)
        cube.Cube()
        pygame.display.flip()
        pygame.time.wait(10)


for i in range(10):
    main()

pygame.quit()
quit()