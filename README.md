# Phishing-Detector

Internet and digital world are growing every day and everyone is becoming part of this world.
Because of this growth, everyday a new information or technology is entering this world. Most
people can’t track these new developments and they become target for deceiving. By creating
similar websites to authentic sites, people are getting deceived and and their information is
stolen by the creators of these phishing websites. In this paper, a model has been proposed to
detect phishing websites by using machine learning methods. Machine learning was done using
a certain data set and the best model was selected because of testing more than one model.

The program has been tested using machine learning methods and neural network. First, we
implemented our data set. Afterwards, we checked our data for missing information. We also
checked for outliers in this information because some outlier data can cause problems with
machine learning. To illustrate this, we made graphs with and without outliers.

Later, we had to divide our data into two as training and testing, but we divided our data
into three so that out machine couldn’t memorize the data directly and not cause problems in
other data sets. For this reason, the data trained with the training set and after that in model
selection part we used val data set to choose our best model and finally we used to test data set
for testing. The reason we added the model selection part is that we want to choose the best
algorithm while checking the given data. For this reason, we used three different algorithms.
These are KNN, RF and XGB.

As a result of running the algorithms, we got the best value from the RF algorithm. We
decided to choose RF because we checked precision and recall values and best one was in RF
algorithm. Then we looked at the RC value by running the RF algorithm. This value should be
between 0-1, 0 is the worst scenario and 1 is the best scenario. As a result of this scenario, our
success rate was 0.99. We then tested whether we could increase our success rate by establishing
a neural network. In this network there was 3 different layers and an output layer as result. In
the first layer there were 128 nodes to examine and in the second one there were 64, in third 16
and in the output layer there were 1 node as a result. However, at this stage, we decided that our
problem could be solved by using ML, after our success rate was 0.88 on our neural network RC
graph. As a conclusion we show that lots of websites are phishing websites to deceive people
and stole their information and we solve this problem by using machine learning methods.


Here is the demo link for deployment: https://predicting-phishing-or-not.herokuapp.com/

This repository is created by [Ozgur Dogan](https://github.com/ozgurdogan646), [Gulcin Betul Cetres](https://github.com/gulcinbetulcetres) and [Okan Bagriacik](https://github.com/OkanBagriacik).
