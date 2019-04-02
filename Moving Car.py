from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(14, 10, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0.3315,0.7981,0.85,1)
    glClear(GL_COLOR_BUFFER_BIT)

angle = 0
move = 0
car_z = 0
forward = True
moveBall = 0
forwardBall = True


def arrowKey(key, x, y):
    global car_Z

    if key == GLUT_KEY_LEFT:
        car_Z += 0.5
    elif key == GLUT_KEY_RIGHT:
        car_Z -= 0.5
    display()


def drawRoad():
    glLoadIdentity()
    glColor3f(0.429,0.67,0.1139)
    drawLines(-50,-11,0,-50,15,0,50,15,0,50,-11,0)
    glColor3f(0.36,0.3405,0.3132)
    glBegin(GL_POLYGON)
    glVertex(-50,0,-6)
    glVertex(-50,0,6)
    glVertex(40,0,6)
    glVertex(40,0,-6)
    glEnd()
    glColor3f(0.96,0.7608,0.1632)
    drawLines(-50,-5.2,0,-50,-4.6,0,50,-4.6,0,50,-5.2,0)
    drawLines(-50,5.5,0,-50,5,0,50,5,0,50,5.5,0)
    glColor3f(1,1,1)
    drawLines(-2,-0.3,0,-2,0.3,0,2,0.3,0,2,-0.3,0)
    drawLines(-8,-0.3,0,-8,0.3,0,-4,0.3,0,-4,-0.3,0)
    drawLines(-14,-0.3,0,-14,0.3,0,-10,0.3,0,-10,-0.3,0)
    drawLines(-20,-0.3,0,-20,0.3,0,-16,0.3,0,-16,-0.3,0)
    drawLines(-26,-0.3,0,-26,0.3,0,-22,0.3,0,-22,-0.3,0)
    drawLines(4,-0.3,0,4,0.3,0,8,0.3,0,8,-0.3,0)
    drawLines(10,-0.3,0,10,0.3,0,14,0.3,0,14,-0.3,0)
    drawLines(12,-0.3,0,12,0.3,0,16,0.3,0,16,-0.3,0)
    drawLines(18,-0.3,0,18,0.3,0,22,0.3,0,22,-0.3,0)
    drawLines(24,-0.3,0,24,0.3,0,28,0.3,0,28,-0.3,0)


def drawLines(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    glLoadIdentity()
    glRotate(90,0,1,0)
    glBegin(GL_POLYGON)
    glVertex(x1,z1,y1)
    glVertex(x2,z2,y2)
    glVertex(x3,z3,y3)
    glVertex(x4,z4,y4)
    glEnd()
    

def drawCar():

    global car_z
    global angle
    global move
    global forward
    global moveBall
    global forwardBall

    glColor3f(0,0,0.3333333)
    glRotate(90,0,1,0)
    glTranslate(0 + moveBall -(.25*5),  0, 0)
    glutSolidSphere( .7, 10 , 10)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(-2.5 - move , -2.5*.25 , -2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutSolidTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(2.5 - move , -2.5*.25 , -2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutSolidTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(1,0,0)
    glRotate(90,0,1,0)
    glTranslate(-move,0,car_z)
    glScale(1,.25,.5)
    glutSolidCube(5)
    glLoadIdentity()

    glColor3f(1,1,0)
    glRotate(90,0,1,0)
    glTranslate(-move-2.5,0,car_z+.7)
    glutSolidSphere(.3,10,10)
    glLoadIdentity()

    glColor3f(1,1,0)
    glRotate(90,0,1,0)
    glTranslate(-move-2.5,0,car_z-.7)
    glutSolidSphere(.3,10,10)
    glLoadIdentity()

    glColor3f(0.99,0,0)
    glRotate(90,0,1,0)
    glTranslate(1.25 - move,  5*.25, car_z )
    glScale(.5 , .25 , .5)
    glutSolidCube(5)
    glLoadIdentity()

    glColor3f(1,1,1)
    glRotate(90,0,1,0)
    glTranslate(1.25 - move -(.25*5),  5*.25, car_z )
    glScale(0 , .25 , .5)
    glutSolidCube(4)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(1.25 - move -(.25*5),  5*.25, car_z )
    glScale(0 , .25 , .5)
    glutWireCube(4)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(2.5 - move , -2.5*.25 , 2.5*.5 +car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutSolidTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(-2.5 - move , -2.5*.25 , 2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutSolidTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    if forward:
        angle -= .1
        move += .009
        if move > 5.5:
            forward = False

    else:
        move -= .009
        angle += .1
        if move < -30:
            forward = True

    if forwardBall:
        moveBall += .03
        if moveBall > 35.5:
            forwardBall = False

    else:
        moveBall -= .03
        if moveBall < -8:
            forwardBall = True


def display():

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    
    glLoadIdentity()
    glColor3f(0.98,0.8794,0.2254)
    glTranslate(-18,8,0)
    glutSolidSphere(3,50,50)

    glLoadIdentity()
    drawRoad()
    
    glLoadIdentity()
    drawCar()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_SINGLE)
glutInitWindowSize(700, 700)
glutCreateWindow(b'Moving Car')
glutDisplayFunc(display)
glutIdleFunc(display)
glutSpecialFunc(arrowKey)
myInit()
glutMainLoop()