varying vec3 normal;
varying vec4 world_position;
in vec4 position;

void main() {
    normal = gl_Normal; // gl_NormalMatrix * for a interresting effect
    world_position = position;
    gl_Position = gl_ModelViewProjectionMatrix * position;
}