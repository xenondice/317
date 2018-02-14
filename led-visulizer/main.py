from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

program = None


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glShadeModel(GL_SMOOTH)

    if not glUseProgram:
        print('Missing Shader Objects!')
        sys.exit(1)
    global program

    # Read shaders
    vert_code = open('def.vert').read()
    frag_code = open('def.frag').read()

    # Compile
    program = compileProgram(
        compileShader(vert_code, GL_VERTEX_SHADER),
        compileShader(frag_code, GL_FRAGMENT_SHADER)
    )


def resize(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.01, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw_led_cube():
    glTranslatef(-1.5, 0.0, -6.0)

    glBegin(GL_QUADS)

    # Front face
    glNormal3f(0.0, 0.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)

    # Back face
    glNormal3f(0.0, 0.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Top face
    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Bottom face
    glNormal3f(0.0, -1.0, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Right face
    glNormal3f(1.0, 0.0, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Left face
    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if program:
        glUseProgram(program)
    draw_led_cube()
    glutSwapBuffers()


def mouse_used(*args):
    pass


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b'LED Visualizer')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMouseFunc(mouse_used)
    glutReshapeFunc(resize)
    init()
    glutMainLoop()
