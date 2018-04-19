![alt text](https://i.imgur.com/UzyoMpD.png)
# NTNU's Experts in Teams 2018: Cyborg

## About
The project's goal is  to humanize NTNU's cyborg. This involves the following subgoals:
- Designing an outer shell
- Processing neural data
- Visualizing neural data



# Installation

## Linux


# Project description

## Start


## Neural data sources
Default: `file`
### Server
### File
This data source will read neural data from a `.csv` file depending on which data type selected (default: `frequency`):
* `--datatype frequency` outputs an array where each elements is the number of spikes detected after last refresh. The threshold value can be changed in the settings file (default: `-1e7`) **OBS: Negavie value!**
* `--datatype intensity` outputs an array with the voltage recorded at each node.
> Tips:
> Increasing `--refresh-rate` will make file source mode more exiting.

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
