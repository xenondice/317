from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from colour import Color
from threading import Thread
from random import randint
import json
import time

class LedVisualizer:
    """
    Simulates the LED cube in different configurations in OpenGL.
    You have to provide a json dictionary at instantiation, this should refer to a json file.
    You also have to provide a pointer to the array of led colors.
    After this, use the refresh function to update the LEDs.
    """

    model = None
    program = None
    led_colors = None
    led_color_buffer = None
    visualizer_thread = None

    horizontal_angle = 0.0
    vertical_angle = 0.0
    refresh_queued = True
    delta_time = None
    last_time = None

    clear_color = Color('gray')
    fov = 45.0
    close = 0.01
    far = 1000
    window_width = 800
    window_height = 600
    window_title = b'LED Visualizer'

    def __init__(self, model, led_colors):
        if len(model['led-strip']) != len(led_colors)//3:
            raise ValueError('LED color array does not fit current model')

        self.model = model
        self.led_colors = led_colors
        self.led_color_buffer = list(led_colors)
        self.last_time = time.time()

        def thread_func():
            self._init_glut()
            self._init_opengl()
            glutMainLoop()

        self.visualizer_thread = Thread(
            name='visualizer',
            target=thread_func)

        self.visualizer_thread.start()

    def _init_opengl(self):
        glClearColor(
            self.clear_color.get_red(),
            self.clear_color.get_green(),
            self.clear_color.get_blue(),
            1.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        if not glUseProgram:
            raise EnvironmentError('Missing shader objects')

        # Open shader files
        vert_file = open('default.vert')
        frag_file = open('default.frag')

        # Compile
        self.program = compileProgram(
            compileShader(vert_file.read(), GL_VERTEX_SHADER),
            compileShader(frag_file.read(), GL_FRAGMENT_SHADER)
        )

        vert_file.close()
        frag_file.close()

    def _init_glut(self):
        glutInit()
        glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(self.window_width, self.window_height)
        glutCreateWindow(self.window_title)
        glutDisplayFunc(self._render)
        glutIdleFunc(self._render)
        glutMouseFunc(self._mouse_used)
        glutReshapeFunc(self._resize)

    def _resize(self, width, height):
        if height == 0:
            height = 1

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, float(width)/float(height), self.close, self.far)
        glMatrixMode(GL_MODELVIEW)

    def _draw_led_cube(self):
        self.horizontal_angle += 10 * self.delta_time
        glTranslatef(0.0, 0.0, -6.0)

        glRotate(self.horizontal_angle, 0.5, 1.0, 0.0)

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

    def _draw_model(self, debug):
        pass

    def _render(self):

        now_time = time.time()
        self.delta_time = now_time - self.last_time
        self.last_time = now_time

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.refresh_queued:
            print('refreshing')
            for i in range(len(self.led_color_buffer)):
                self.led_color_buffer[i] = self.led_colors[i]
            self.refresh_queued = False

        glLoadIdentity()

        if self.program:
            glUseProgram(self.program)

        self._draw_led_cube()
        #self._draw_model(True)

        glutSwapBuffers()

    def _mouse_used(*args):
        pass

    def refresh(self):
        self.refresh_queued = True


if __name__ == "__main__":
    # TODO: Make the model global for all the scripts and add error check
    model = 'cube'
    model_file = open('{}.json'.format(model))
    model_dict = json.loads(model_file.read())
    model_file.close()
    model_dict['name'] = model

    led_colors = [
        255, 0, 0,
        0, 255, 0,
        0, 0, 255]

    vis = LedVisualizer(model_dict, led_colors)

    while True:
        time.sleep(1)
        for i in range(len(led_colors)):
            led_colors[i] = randint(0, 255)
        vis.refresh()
