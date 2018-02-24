from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from colour import Color
from threading import Thread
from random import randint
from ctypes import sizeof
import json
import time

class LedVisualizer:
    """
    Simulates the LED cube in different configurations in OpenGL.
    You have to provide a json dictionary at instantiation, this should refer to a json file.
    You also have to provide a pointer to the array of led colors.
    After this, use the refresh function to update the LEDs.
    The current shader supports up to 100 LEDS, update the shader variable if more.
    """

    model = None
    program = None
    led_colors = None
    led_buffer_colors = None
    led_buffer_color_index = None
    led_buffer_positions = None
    led_buffer_position_index = None
    visualizer_thread = None

    vao_id = None
    vab_id = None
    attr_pos_loc = None

    horizontal_angle = 0.0
    vertical_angle = 0.0
    refresh_queued = True
    delta_time = None
    last_time = None
    n_leds = None

    clear_color = Color('gray')
    debug = False
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
        self.n_leds = len(model['led-strip'])
        self.last_time = time.time()

        self.led_buffer_colors = (GLfloat * (3*self.n_leds))(*led_colors)
        self.led_buffer_positions = (GLfloat * (3*self.n_leds))(0)
        i = 0
        for v in model['led-strip']:
            self.led_buffer_positions[i] = v[0]
            self.led_buffer_positions[i+1] = v[1]
            self.led_buffer_positions[i+2] = v[2]
            i += 3

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
        glEnable(GL_VERTEX_ARRAY)

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

        self.vao_id = glGenVertexArrays(1)
        glBindVertexArray(self.vao_id)

        vertex_data = (GLfloat * 12)(*[
            -0.5, -0.5, -1, 1.0,
            2, -0.5, -1, 1.0,
            -0.5, 2, -1, 1.0
        ])

        self.vab_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vab_id)

        self.attr_pos_loc = glGetAttribLocation(self.program, 'position')
        glEnableVertexAttribArray(self.attr_pos_loc)

        glVertexAttribPointer(self.attr_pos_loc, 4, GL_FLOAT, GL_FALSE, 0, GLvoid)

        glBufferData(GL_ARRAY_BUFFER, len(vertex_data) * sizeof(GLfloat), vertex_data, GL_STATIC_DRAW)

        glBindVertexArray(0)
        glDisableVertexAttribArray(self.attr_pos_loc)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

        """
        indexes = glGenBuffers(2)
        self.led_buffer_color_index = indexes[0]
        self.led_buffer_position_index = indexes[1]

        glBindBuffer(GL_UNIFORM_BUFFER, self.led_buffer_color_index)
        glBufferData(GL_UNIFORM_BUFFER,
                     len(self.led_buffer_colors)*sizeof(GLfloat),
                     self.led_buffer_colors,
                     GL_STREAM_DRAW)

        glBindBuffer(GL_UNIFORM_BUFFER, self.led_buffer_position_index)
        glBufferData(GL_UNIFORM_BUFFER,
                     len(self.led_buffer_positions)*sizeof(GLfloat),
                     self.led_buffer_positions,
                     GL_STATIC_DRAW)

        glBindBuffer(GL_UNIFORM_BUFFER, 0)

        color_binding_point = 1
        position_binding_point = 2

        color_block_index = glGetUniformBlockIndex(self.program, b'led_colors')
        glUniformBlockBinding(self.program, color_block_index, color_binding_point)
        glBindBufferBase(GL_UNIFORM_BUFFER, color_binding_point, self.led_buffer_color_index)

        position_block_index = glGetUniformBlockIndex(self.program, b'led_positions')
        glUniformBlockBinding(self.program, position_block_index, position_binding_point)
        glBindBufferBase(GL_UNIFORM_BUFFER, position_binding_point, self.led_buffer_position_index)
        """

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

    def _draw_model(self):
        self.horizontal_angle += 10 * self.delta_time
        glTranslatef(0.0, 0.0, -6.0)

        glRotate(self.horizontal_angle, 0.5, 1.0, 0.0)

        glBindVertexArray(self.vao_id)
        glDrawArrays(GL_TRIANGLES, 0, 12)
        glBindVertexArray(0)

        '''if self.debug:
            led_coords = self.model['led-strip']
            glBegin(GL_LINES)
            for i in range(1, len(led_coords)):
                prev_led = led_coords[i-1]
                next_led = led_coords[i]
                glVertex3f(prev_led[0], prev_led[1], prev_led[2])
                glVertex3f(next_led[0], next_led[1], next_led[2])
            glEnd()

        enclosure_coords = self.model['led-enclosure']

        glBegin(GL_TRIANGLES)
        for vertex in enclosure_coords:
            glVertex3f(vertex[0][0], vertex[0][1], vertex[0][2])
            glVertex3f(vertex[1][0], vertex[1][1], vertex[1][2])
            glVertex3f(vertex[2][0], vertex[2][1], vertex[2][2])
        glEnd()
        '''
    def _render(self):
        now_time = time.time()
        self.delta_time = now_time - self.last_time
        self.last_time = now_time

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.refresh_queued:
            print('refreshing')
            for i in range(3*self.n_leds):
                self.led_buffer_colors[i] = self.led_colors[i]
            """
            glBindBuffer(GL_UNIFORM_BUFFER, self.led_buffer_color_index)
            glBufferSubData(GL_UNIFORM_BUFFER,
                            0,
                            len(self.led_buffer_colors)*sizeof(c_float),
                            self.led_buffer_colors)
            glBindBuffer(GL_UNIFORM_BUFFER, 0)
            """
            self.refresh_queued = False

        glLoadIdentity()

        glUseProgram(self.program)

        self._draw_model()

        glutSwapBuffers()

        glUseProgram(0)

    def _mouse_used(*args):
        pass

    def refresh(self):
        self.refresh_queued = True

    def running(self):
        return self.visualizer_thread.is_alive()


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
    vis.debug = True

    time.sleep(2)

    while vis.running():
        for i in range(len(led_colors)):
            led_colors[i] = randint(0, 255)
        vis.refresh()
        time.sleep(1)
