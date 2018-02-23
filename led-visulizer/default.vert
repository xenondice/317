varying vec3 normal;
varying vec3 position;

void main() {
    normal = gl_NormalMatrix * gl_Normal;
    position = gl_Vertex;
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}