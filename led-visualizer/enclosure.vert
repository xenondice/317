varying vec4 world_normal;
varying vec4 world_position;
varying vec3 view_vector;
in vec4 position;
in vec4 normal;
uniform vec3 cam_pos;

void main() {
    world_normal = normal;
    world_position = position;
    view_vector = normalize(cam_pos - position.xyz);
    gl_Position = gl_ModelViewProjectionMatrix * position;
}