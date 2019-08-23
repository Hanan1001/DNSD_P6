# DNSD_P6
DNSD project deliverables for project 6 "Disaster pipeline"

## About the project 
Following a disaster, there are a number of different problems that may arise. Different types of disaster response organizations take care of different parts of the disasters and observe messages to understand the needs of the situation. They have the least capacity to filter out messages during a large disaster, so predictive modeling can help classify different messages more efficiently.

In this project we used RandomForest classifier as our main model. 

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Table of contents 
**Jupyer Notebook Files** <br>
Required files for the ETL model and for the ML model
[ETL notebook found here](https://github.com/Hanan1001/DNSD_P6/blob/master/ML%20Pipeline%20Preparation.ipynb)
 and 
[ML notebook found here](https://github.com/Hanan1001/DNSD_P6/blob/master/ML%20Pipeline%20Preparation.ipynb)
<br>
**Data File** <br>
For console part of the project it has the data files, database and a python file to process data
[can be found here](https://github.com/Hanan1001/DNSD_P6/tree/master/data)
 <br>
**Models file** <br>
Has the classifier model and the training and evaluating python files 
[can be found here](https://github.com/Hanan1001/DNSD_P6/tree/master/models)
 <br>
**App File** <br>
Has the run file that allows us to visulize our results
[can be found here](https://github.com/Hanan1001/DNSD_P6/tree/master/app)
<br>

## ScreenShots of my run file
![alt text](https://github.com/Hanan1001/DNSD_P6/blob/master/Capture1.JPG)
![alt text](https://github.com/Hanan1001/DNSD_P6/blob/master/Capture2.JPG)
![alt text](https://github.com/Hanan1001/DNSD_P6/blob/master/Capture3.JPG)


## Acknowledgement 
I would like to thank MiSK Academy for this opprotunity and the team at Udacity for cooredinating such a fruitful program
