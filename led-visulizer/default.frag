#define MAX_LEDS 300
#define MIN_DISTANCE 0.01

varying vec3 normal;
varying vec3 world_position;
//uniform vec3[MAX_LEDS] led_positions;
//uniform vec3[MAX_LEDS] led_colors;

void main() {
    vec3 color_sum = vec3(0, 0, 0);
    //for (int i = 0; i < MAX_LEDS; i++) {
    //    float dist = distance(position, led_positions[i]);
    //    if (dist < MIN_DISTANCE) dist = MIN_DISTANCE;
    //    dist = MIN_DISTANCE/dist;
    //    color_sum.x += led_colors[i].x * dist;
    //    color_sum.y += led_colors[i].y * dist;
    //    color_sum.z += led_colors[i].z * dist;
    //}
    gl_FragColor = vec4(color_sum, 1.0);
}