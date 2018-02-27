varying vec4 color;

void main() {
    color = vec4(1.0, 0.0, 0.0, 1.0);
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}