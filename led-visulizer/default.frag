#define MAX_LEDS 300
#define MIN_DISTANCE 0.01
#define LED_AMP 10

varying vec3 normal;
varying vec4 world_position;

uniform vec4[MAX_LEDS] led_positions;
uniform vec4[MAX_LEDS] led_colors;

void main() {
    vec3 color_sum = vec3(0.0, 0.0, 0.0);
    for (int i = 0; i < led_colors.length(); i++) {
        float dist = distance(world_position, led_positions[i]);
        if (dist < MIN_DISTANCE) dist = MIN_DISTANCE;
        dist = MIN_DISTANCE/dist;
        vec4 led_color = led_colors[i];
        color_sum.x += led_color.x * dist * LED_AMP;
        color_sum.y += led_color.y * dist * LED_AMP;
        color_sum.z += led_color.z * dist * LED_AMP;
    }
    gl_FragColor = vec4(color_sum, 1.0);
}