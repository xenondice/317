![alt text](https://i.imgur.com/UzyoMpD.png)
# NTNU's Experts in Teams 2018: Cyborg

## About
The project's goal is  to humanize NTNU's cyborg. This involves the following subgoals:
- Designing an outer shell
- Processing neural data
- Visualizing neural data

# Installation
You can install the project in two ways, either by using Anaconda, or by using pip. The latter is probably the simplest.

## Anaconda
If you are using Anaconda, you can quickly get the project up and running by cloning the project, opening the Anaconda prompt and executing:
```
cd 317
conda create -n eit --file requirements
activate eit
```
This will create a virtual environment for this project. This makes it easy to remove the installed packages afterwards, considering their collective size.

Since the package websocket-client, nessesary for the server functionality, is not available in the main Anaconda package repository, you will have to install this through pip. Open the Anaconda prompt and type the following:
```
activate eit
pip install websocket-client
```
You can also use the conda-forge repository:
```
conda install -c conda-forge websocket-client
```

## Pip
Clone the project and open up a terminal (with python 3) and type:
```
cd 317
pip install -r requirements.txt
```

## Pycharm and Anaconda
If you are using PyCharm and Anaconda, you will have to do the following:
- File -> Settings -> Project: 317 -> Project Interpeter
- Press the cog and Add local
- Navigate to the Anaconda installation folder, then env/eit/python.exe
- Press the arrow at the top right corner and Edit configurations
- Add a new python configuration
- Choose the script you are working on (add several configurations for the different files if needed) and the default interpeter

## Visual Studio Code and Anaconda
If you are using VSCode with Anaconda, you will have to open it and do the following after opening the 317 folder:
- SHIFT + CTRL + P, type "python interpreter" and choose the first option
- Choose the eit environment (may have to wait some time, if not available, add the path ..anaconda root../env/eit/python.exe to the settings.json file)
- SHIFT + CTRL + P again, type "default build task" and choose the first option, add the following task:
```
"label": "start",
"type": "shell",
"command": "${config:python.pythonPath} start.py",
"group": {
    "kind": "build",
    "isDefault": true
}
```
- Now press SHIFT + CTRL + B to run

## Getting the virtual model to work
On Windows, the freeglut.dll needed for OpenGL is included and everything should work out-of-the-box.

If you are using linux and want to use the virtual model, you will have to execute the following command after installing the project as described above:
```
apt-get install freeglut3-dev
```
The virtual model is, for the time being, not supported on Mac OS.

# Running the project
Open up a terminal with python 3, navigate to the project folder and type `python start.py --help` to get a list over the available arguments. Just running the start.py file will start the project with its default arguments, equivalent of executing the command:
```
python start.py --refresh-rate 10 --datatype frequency --led-model large_cube --interpreter induvidual-moving-average --colors blue red --file neural_sources/file/data/2017-10-20_MEA2_100000rows_10sec.csv --serial
```

# Project structure
The project is divided into three modules: neural sources, neural interpreters and neural presenters. Each of these modules represent a part of a three stage pipeline for visualizing neural data, and each module consists of several sub-modules that are interchangeable. The different sub-modules can be chosen by supplying the correct argument on runtime. The pipeline itself is located in the start.py file, with supplementary files located in the systems module.

## Start/system
This file marks the start of the project and holds the overall architecture.

Firstly, the input arguments are parsed by the environment.py file. This file is responsable for setting up the running environment based on the supplied input arguments. The environment is represented as a singelton holding the required arguments and pointers, located in setting.py.

An object for each stange in the pipe is then instanciated, in turn, based on the current environment. Eventually the project then enters an infinte loop contained in the neural source object. Start.py provides the neural source object with a callback function that passes the neural data from the source object, through the interpreter and at last to the presenter. The refresh rate is handled by the source object.

## Neural data sources
Marks the first step in the pipeline. This module is responsable for getting the neural data and creating a loop that passes the data on in regular intervals. The data is passed on through a callback to start.py.

There are currently three sources for neural data, which can be set by arguments: `--file`, `--server <ip>` and `--no-input`. The default is `--file`.

### File
This data source will read neural data from a `.csv` file depending on which data type selected (default: `frequency`):
* `--datatype frequency` outputs an array where each elements is the number of spikes detected after last refresh. The threshold value can be changed in the settings file (default: `-1e7`) **OBS: Negavtie value!**
* `--datatype intensity` outputs an array with the voltage recorded at each node.
> Tips:
> Increasing `--refresh-rate` will make file source mode more exiting, but may be limited by the presenter (in our experience, a refresh rate of 15 is the highest rate for the large LED cube)

### Server
This source will read neural data from a websocket server (https://github.com/cyborg-client/Remap-server) at the provided ip. The default port of 6780 can be overvritten by supplying the argument `--port <port>`. The LEDs on the presenter will turn red if the connection times out. Although supported by the remap-server, passing feedback signals back to the neurons is not yet supported by this program.
> Note:
> The remap-server doesn't support the intensity datatype and will fail if this datatype is supplied.

### No input
This source only contains a loop and supplies the callback with a zero-array of data. This is useful for intrepreters that don't use the neural data such as random (demo-programs)

## Data interpreters
Second step in the pipeline. This module in responsable for converting the Micro Electrode Array output to a array of RGB values appropriate for the model. We have provided a handful of different interpreters, but it is easy to create new ones. Interpreter classes has to implement a constructur function (and throw syntax error if the environment is invalid) and a render function. The render function takes to arguments, an input array of the neural data and an output array that is to be filled with the RBG LED values. The function returns nothing and is called before every refresh. A example is provided below:
```
import system.settings as settings
import random

class RandomMode:
    def __init__(self):
        pass

    def render(self, input_data, output_data):
        for i in range(settings.LEDS_TOTAL):
            for j in range(3):
                output_data[i*3 + j] = random.randint(0, 255)
```
The default interpreter is `individual-moving-average`. An explaination of the different interpreters is provided below. The demo-programs does not a neural source.

### Individual moving average
High and low color can be changed using `--colors` (default: `blue` and `red`).

### Moving average
High and low color can be changed using `--colors` (default: `blue` and `red`).

### Intensity
Intensity interpreter uses the voltage to place each node into 10 groups based on each node output intensity on the MEA plate. The highest voltage will always be in group 9 and lowest voltage will always be in group 0. High and low color can be changed using `--colors` (default: `blue` and `red`).

### Random
Demo prorgam. Randomizes every LED color.

### Smiley
Demo prorgam. Only works on the `large_cube` led model. Shows a smiley on the top side, while a wave is travelling around the sides while cycling through different colors.

### Snake
Demo program. Shows a snake travelling through the LED strip, changing color on each cycle.

### snake-white
Demo program. Shows a random-colored snake moving through the LED strip on a white background.

## Visual presenters
Default: `--serial`
### Serial
### 2D plot
### Virtual
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

## Miscellaneous
The project has some additional files of intrest.

### LED models
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
