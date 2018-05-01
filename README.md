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
This source will read neural data from a websocket server (https://github.com/cyborg-client/Remap-server) at the provided ip. The default port of 6780 can be overvritten by supplying the argument `--port <port>`. The LEDs on the presenter will turn red if the connection times out. Although supported by the remap-server, passing feedback signals back to the neurons is not yet supported by this program. Also note that the remap-server doesn't support the intensity datatype and will fail if this datatype is supplied.

### No input
This source only contains a loop and supplies the callback with a zero-array of data. This is useful for intrepreters that don't use the neural data such as random (demo-programs)

## Data interpreters
Default: `individual-moving-average`
### Individual moving average
### Moving average
### Intensity
Intensity interpreter uses the voltage to place each node into 10 groups based on each node output intensity on the MEA plate. The highest voltage will always be in group 9 and lowest voltage will always be in group 0. High and low color can be changed using `--colors` (default: `green` and `red`)
### Random
### Smiley
### Snake


## Visual presenters
Default: `--serial`
### Serial
### 2D plot
### Virtual

## Miscellaneous
The project has some additional files of intrest.
