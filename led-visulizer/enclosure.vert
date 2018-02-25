varying vec3 normal;
varying vec3 world_normal;
varying vec4 world_position;
in vec4 position;

void main() {
    world_normal = gl_Normal;
    normal = gl_NormalMatrix * gl_Normal;
    world_position = position;
    gl_Position = gl_ModelViewProjectionMatrix * position;
}