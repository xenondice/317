![alt text](https://i.imgur.com/UzyoMpD.png)
# NTNU's Experts in Teams 2018: Cyborg

## About
The project's goal is  to humanize NTNU's cyborg. This involves the following subgoals:
- Designing an outer shell
- Processing neural data
- Visulizing neural data

## Required packages/programs
# Linux
apt-get install freeglut3-dev


## Installation
If you are using Anaconda, you can quickly get the project up and running by cloning the project, opening the Anaconda prompt and executing:
```
cd 317
conda create -n eit --file requirements
activate eit
```
If you are using PyCharm, you have to do the following:
- File -> Settings -> Project: 317 -> Project Interpeter
- Press the cog and Add local
- Navigate to the Anaconda installation folder, then env/eit/python.exe
- Press the arrow at the top right corner and Edit configurations
- Add a new python configuration
- Choose the script you are working on (add several configurations for the different files if needed) and the default interpeter

## LED model visualizer
![alt_text](https://i.imgur.com/dXQbp2c.jpg)
### Controls
- Use the D key to switch to debug mode
- Press and hold left mouse button + move mouse to rotate the model
- Use the scroll wheel to zoom in and out
### API
First load the model's json file to a python dictionary object.
```python
import json
file = open(filename)
model = json.loads(file.read())
```
Then make an array of 3 times the number of LEDs to hold the colors and pass this + the dictionary to a new visualizer object.
This will open a window and show the model. Keep in mind that the visualizer is working in a new thread.
```python
led_colors = [0] * (len(model_dict['led-strip']) * 3)
visualizer = LedVisualizer(model, led_colors)
```
Now update the `led_colors` array and call `visualizer.refresh()` whenever you want the virtual model to change.
If you want to use the model file's led-groups, just access them from the dictionary object, but remeber to check for -1.
```python
 led_id = model['led-groups']['down-plane'][x][y]
 if led_id != -1:
     led_colors[led_id*3] = 255
     led_colors[led_id*3+1] = 255
     led_colors[led_id*3+2] = 255
```
## JSON model file example
```javascript
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
  // Use id -1 for placeholder LEDs.
  "led-groups": {
    "down-plane": [ // Group "down-plane" with a 2D matrix containing LEDs 0, 1, 2 and one placeholder.
      [0, 1],
      [2, -1]
    ]
  }
}
```
