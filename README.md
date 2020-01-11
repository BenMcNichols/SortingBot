
# SortingBot

The primary resource for this code is the tensorflow documentation at the following link. It provides an excellent starting point for image analysis with tensorflow.
https://www.tensorflow.org/hub/tutorials/image_retraining.

## Stage 1 - Preliminary Setup

### Setting up Python:

Download the following files and save them to an easily accessible folder on your computer:
* Retrain.py
* Imagelabel.py
* TrainingData folder 

Install python using Anaconda on your PC
* This can be found at https://www.anaconda.com/distribution/
* Download the python 3.7 version. Do not select the option to add python to your PATH variables. 

Open Anaconda Prompt by searching for it in the start menu. A terminal window should appear.

Create a new environment by typing “conda create --name env1”
* Press “y” to proceed. 
* From here on, all of your anaconda work should be performed from this environment. You can select it when anaconda opens by typing “activate env1”
* You will be able to tell your active environment because it will be in parentheses on the leftmost side of the terminal. If it says (base) you are not in the correct environment.
* Your code editing should be performed in spyder. Open this by typing “spyder” into the anaconda terminal.

The following packages need to be installed for everything to work. Install them by typing “conda install “, followed by the package name. If this does not work you can try “pip install packagename” instead.
* numpy
* conda
* matplotlib
* tensorflow
* tensorflow_hub
* pyserial

Possibly more. Read the error messages if any come up (which they will). This might be the problem.

### Setting up Your Servo Control:
* This program uses an Arduino as a serial port to control the servo via usb from python, while the pc handles all of the recognition. This is a messy way to do things and increases the cost of the system significantly so there’s probably a better solution out there. 
If you could transfer your PC trained model to a raspberry pi this would have a nice small package, but I could see that being a very messy process.

### Setting Up The Camera
* Just plug it in and it should be good. I'm using a logitech camera and they're pretty utilitarian.
Note: Haven’t had any issues with this yet so it’s probably the next thing that will break. 

## Stage 2 - Training Data

Creating Training Data:
* At the moment, just copy pictures to subfolders of the TrainingData folder. For example, if you want three categories you would have three folders of pictures in the TrainingData folder.
Cleaner solution TBD

Training your Model:
1. Open anaconda prompt
1. type “python retrain.py --image dir ~”D:/Documents/PythonProjects/BeanSorter/TrainingData”
1. This could take up to ½ hour to run. You should hopefully see the accuracy get pretty close to 100% as at runs.
1. Once the training is complete, you should have created a folder of the training model. Mine was at D/tmp/retrain_logs
1. You can view data on your model by typing “tensorboard –logdir D:/pathtoyourdata/retrain_logs”
1. open a web browser and go to localhost:6006 to view your graphs.
1. close the program in console by typing C (or ctrl+c maybe?)

## Stage 3 - Using your model

1. You can test your model by opening the program ImageLabel.py in spyder. 
1. You will need to change the text in lines 84, 86, and 87 to direct your code to the proper locations of the test picture, trained model, and output labels.
1. Put the test picture in the folder you specified in step 1. 
1. Run the code with f5. It should output the percentage match of your picture with each category in the console.
