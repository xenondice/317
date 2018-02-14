from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

program = None
vert_data = []

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

    prepare_led_cube()

    glLinkProgram(program)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, len(vert_data)*4, (4*len(vert_data)) *vert_data, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5*4, 0)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5*4, 3*4)
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)


def resize(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.01, 100.0)
    glMatrixMode(GL_MODELVIEW)


def prepare_led_cube():

    # X Z- wall
    vert_data.extend([0.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([0.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    # X Z+ wall
    vert_data.extend([0.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([0.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    # Y X- wall
    vert_data.extend([0.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([0.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    # Y X+ wall
    vert_data.extend([1.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([1.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    # Z Y- wall
    vert_data.extend([0.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([1.0, 0.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 0.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    # Z Y+ wall
    vert_data.extend([0.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates

    vert_data.extend([1.0, 1.0, 0.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([0.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates
    vert_data.extend([1.0, 1.0, 1.0])  # Position
    vert_data.extend([0.0, 0.0])  # Texture coordinates


def draw_led_cube():
    glTranslatef(-1.5, 0.0, -6.0)
    glutSolidCube(1.0)


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
