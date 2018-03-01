#define MAX_LEDS 300
#define ENCLOSURE_SPREAD 8000
#define LED_AMPLIFICATION 2
#define ENCLOSURE_FROSTING 30.0
#define ENCLOSURE_COLOR vec3(1.0, 1.0, 1.0)

varying vec4 world_normal;
varying vec4 world_position;

uniform vec4[MAX_LEDS] led_positions;
uniform vec4[MAX_LEDS] led_colors;
uniform vec2 hdr;

void main() {

    vec3 ambient_light = vec3(1.0, 1.0, 1.0);
    vec3 ambient_normal = vec3(0.474, 0.316, 0.158);
    float ambient_bounce = 0.8;

    float intensity = clamp(dot(world_normal, ambient_normal), 0, 1);
    intensity = intensity * (1 - ambient_bounce) + ambient_bounce;
    vec3 color_sum = ENCLOSURE_COLOR * ambient_light * intensity * 0.5;
    //float change_sum = 0.0;

    for (int i = 0; i < led_colors.length(); i++) {

        vec4 distance_vector = world_position - led_positions[i];
        float distance_squared = dot(distance_vector, distance_vector);
        //float normal_distance_squared = dot(world_normal, distance_vector); // Using just normal here yields '3D'
        //float planar_distance_squared = distance_squared - normal_distance_squared;

        float spread = exp(-ENCLOSURE_SPREAD * distance_squared / 2.0);
        //change_sum += gaussian_spread;
        //float spread = 1/sqrt(distance_squared);

        vec4 led_color = led_colors[i];
        float bias = mod(dot(world_position,world_position)*52461156.0+25651584.0,1000)/1000.0;
        bias = 1.0 - bias/ENCLOSURE_FROSTING;

        color_sum += led_color.xyz * spread * bias * LED_AMPLIFICATION;
    }

    color_sum = color_sum / hdr.x - hdr.y;

    //change_sum = clamp(1 - change_sum, 0, 1);
    //color_sum += ENCLOSURE_COLOR * change_sum;

    gl_FragColor = vec4(color_sum, 1.0);
}