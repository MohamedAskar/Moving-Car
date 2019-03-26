from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(10, 12, 12,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0.3315,0.7981,0.85,1)
    glClear(GL_COLOR_BUFFER_BIT)

angle = 0
x = 0
forward = True
car_Z = 0


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
    drawLines(-100,-11,0,-100,15,0,100,15,0,100,-11,0)
    glColor3f(0.36,0.3405,0.3132)
    glBegin(GL_POLYGON)
    glVertex(-50,0,-6)
    glVertex(-50,0,6)
    glVertex(40,0,6)
    glVertex(40,0,-6)
    glEnd()
    glColor3f(0.96,0.7608,0.1632)
    drawLines(-50,-5.2,0,-50,-4.6,0,40,-4.6,0,40,-5.2,0)
    drawLines(-50,5.5,0,-50,5,0,40,5,0,40,5.5,0)

def drawLines(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(x1,z1,y1)
    glVertex(x2,z2,y2)
    glVertex(x3,z3,y3)
    glVertex(x4,z4,y4)
    glEnd()
    

def drawCar():

    global car_Z
    global angle
    global x
    global forward

    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, -2.5 * 0.5 + car_Z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.7313,0.75,0.7275)
    glutSolidSphere(0.48,50,50)
    glColor3f(0.2425, 0.2425, 0.25)
    glutSolidTorus(0.2, 0.65, 12, 15)    

    glLoadIdentity()
    glTranslate(-2.5 + x, -2.5 * 0.25, -2.5 * 0.5 + car_Z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.7313,0.75,0.7275)
    glutSolidSphere(0.48,50,50)
    glColor3f(0.2425, 0.2425, 0.25)
    glutSolidTorus(0.2, 0.65, 12, 15)

    glLoadIdentity()
    glColor3f(0.82, 0.2046, 0.1722)
    glTranslate(x, 0, car_Z)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.33,0.3062,0.2409)
    glTranslate(x,0.7,car_Z)
    glScale(1,0,0.5)
    glutSolidCube(4.5)

    glLoadIdentity()
    glColor3f(0.82, 0.2046, 0.1722)
    glTranslate(x, 1.25, car_Z)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0.7313,0.75,0.7275)
    glTranslate(x+1.25, 1.25, car_Z)
    glScale(0,0.25,0.5)
    glutSolidCube(4)

    glLoadIdentity()
    glColor3f(.9,.9,0)
    glTranslate(x+2.5,.3, car_Z +0.8)
    glutSolidSphere(.25,6,6)

    glLoadIdentity()
    glColor3f(.9,.9,0)
    glTranslate(x+2.5,.3,car_Z - 0.5)
    glutSolidSphere(.25,6,6)

    glLoadIdentity()
    glTranslate(-2.5 + x, -2.5 * 0.25, 2.5 * 0.5 + car_Z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.7313,0.75,0.7275)
    glutSolidSphere(0.48,50,50)
    glColor3f(0.2425, 0.2425, 0.25)
    glutSolidTorus(0.2, 0.65, 12, 15)
    

    glLoadIdentity()
    glTranslate(2.5 + x, -2.5 * 0.25, 2.5*0.5 + car_Z)
    glRotate(angle, 0, 0, 1)
    glColor3f(0.7313,0.75,0.7275)
    glutSolidSphere(0.48,50,50)
    glColor3f(0.2425, 0.2425, 0.25)
    glutSolidTorus(0.2, 0.65, 12, 15)

    glLoadIdentity()
    glColor3f(0.7313,0.75,0.7275)
    glTranslate(x - 1.25 ,0,car_Z -0.1 )
    glScale(0.5,0.3,0)
    glutSolidCube(4)    

    if forward:
        angle -= 0.1
        x += 0.0005
        if x > 5:
            forward = False
    else:
        x -= 0.0005
        angle += 0.1
        if x < -5:
            forward = True



def display():

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    
    glLoadIdentity()
    glColor3f(0.98,0.8794,0.2254)
    glTranslate(8,11.5,0)
    glutSolidSphere(3,50,50)

    glLoadIdentity()
    drawRoad()

    glLoadIdentity()
    glColor3f(1,1,1)
    drawLines(-2,-0.3,0,-2,0.3,0,2,0.3,0,2,-0.3,0)
    drawLines(-8,-0.3,0,-8,0.3,0,-4,0.3,0,-4,-0.3,0)
    drawLines(-14,-0.3,0,-14,0.3,0,-10,0.3,0,-10,-0.3,0)
    drawLines(-20,-0.3,0,-20,0.3,0,-16,0.3,0,-16,-0.3,0)
    drawLines(-26,-0.3,0,-26,0.3,0,-22,0.3,0,-22,-0.3,0)
    drawLines(4,-0.3,0,4,0.3,0,8,0.3,0,8,-0.3,0)
    drawLines(10,-0.3,0,10,0.3,0,14,0.3,0,14,-0.3,0)
    
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