# JSON model file commented example
```
{
  // Defines the sequential positions of the LEDs in the led strip in 3D space.
  // 1 unit = 1 meter.
  "led-strip": [
    [0, 0, -1.1], // The first LED position in [X,Y,Z].
    [1, 0, -1.1],
    [0, 1, -1.1]
  ],

  // Defines a polygonal model behind which the LEDs will sit.
  // Follow the right-hand-rule to ensure the normals of the polygons
  // points out towards the observer.
  "led-enclosure": [
    [[-0.5, -0.5, -1], [2, -0.5, -1], [-0.5, 2, -1]] // First triangular polygon, normal along negative Z.
  ],

  // Defines groups that can be used in the code to easier control single LEDs.
  // Accessible through a dictionary object in code, group name is arbitrary.
  // Use n-dimensional arrays with the ids of the LEDs (zero-indexed).
  "led-groups": {
    "down-plane": [0, 1, 2] // Group "down-plane" with the LEDs 0, 1 and 2.
  }
}
```