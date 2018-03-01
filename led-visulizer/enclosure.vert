varying vec4 world_normal;
varying vec4 world_position;
in vec4 position;
in vec4 normal;

void main() {
    world_normal = normal;
    world_position = position;
    gl_Position = gl_ModelViewProjectionMatrix * position;
}