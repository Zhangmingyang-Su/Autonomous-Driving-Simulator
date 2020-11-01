# Autonomous Driving Simulator
This repository is for Self-Driving Cars simulator by using Udacity testing driving mode. Connecting Flask framework to implement real-time autonomous driving condition.

## Dataset
* [Link](https://github.com/rslim087a/track)


## Package Installation
* Keras
* OpenCV
* imgaug

## Vitual Environment Setup for Simulation
```
conda create --name myenviron
source activate myenviron
conda install -c anaconda flask
conda install -c conda-forge python-socketio
```

## Udacity Simulator for Autonomous Driving([Github](https://github.com/udacity/self-driving-car-sim))
![](Autonomous%20Driving%20Simulator/pics/udacity.png)
![](Autonomous%20Driving%20Simulator/pics/av.png)

Download Udacity simulator application for autonomous test


## Model Architecture
A end-to-end model in this repository is Nvidia model as described in [End-to-End Deep Learning for Self-Driving Cars](https://developer.nvidia.com/blog/deep-learning-self-driving-cars/)
![](Autonomous%20Driving%20Simulator/pics/nvidia.png)

## Result
* Straight Line

![](Autonomous%20Driving%20Simulator/pics/result1.gif)

* Left Turn

![](Autonomous%20Driving%20Simulator/pics/result2.gif)

* Right Turn

![](Autonomous%20Driving%20Simulator/pics/result3.gif)

Results for test and train error works very well, Image Shows after 100 epochs.

![](Autonomous%20Driving%20Simulator/pics/test.png)
