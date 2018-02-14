from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from random import randint

program = None
tex_ids = None
tex_ptr = None
leds = None
angle = 0.0


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
    global program, tex_ptr

    # Read shaders
    vert_code = open('def.vert').read()
    frag_code = open('def.frag').read()

    # Compile
    program = compileProgram(
        compileShader(vert_code, GL_VERTEX_SHADER),
        compileShader(frag_code, GL_FRAGMENT_SHADER)
    )

    tex_ptr = glGetUniformLocation(program, "tex")

def resize(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.01, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw_led_cube():
    global angle
    angle = angle + 0.1
    glTranslatef(0.0, 0.0, -6.0)

    glRotate(angle, 0.5, 1.0, 0.0)

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


def randomize():
    global leds
    x = randint(0, len(leds)-1)
    y = randint(0, len(leds[0])-1)
    z = randint(0, len(leds[0][0])-1)
    leds[x][y][z] = [randint(0,255),randint(0,255),randint(0,255)]

def display():
    global tex_ids, tex_ptr

    randomize()
    update_texture()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if program:
        glUseProgram(program)

    #glActiveTexture(GL_TEXTURE0)
    #glBindTexture(GL_TEXTURE0, tex_ids[0])
    #glUniform3i(tex_ptr, 0)

    draw_led_cube()
    glutSwapBuffers()
    #glUseProgram(None)


def create_textures():
    global tex_ids, leds

    tex_ids = glGenTextures(len(leds))
    glBindTexture(GL_TEXTURE_2D, tex_ids[0])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    update_texture()

    #gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, width, height, GL_RGB, GL_UNSIGNED_BYTE, texture)


def update_texture():
    global leds

    width = len(leds[0])
    height = len(leds[0][0])

    texture = bytearray([])
    for x in range(width):
        for y in range(height):
            for z in range(3):
                texture.append(int(leds[0][x][y][z]))

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture)


def mouse_used(*args):
    pass


def show_simulation(leds_in):
    global leds
    leds = leds_in
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'LED Visualizer')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMouseFunc(mouse_used)
    glutReshapeFunc(resize)
    init()
    create_textures()
    glutMainLoop()


show_simulation([
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ],
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ],
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ],
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ],
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ],
    [
        [[10, 100, 200], [10, 100, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [200, 10, 200], [10, 100, 200], [10, 100, 200]],
        [[10, 100, 200], [10, 100, 200], [100, 100, 20], [10, 100, 200]],
        [[0, 0, 200], [100, 100, 200], [100, 100, 200], [100, 100, 200]],
    ]
])

