# Phishing-Detector
<p align="center">
  <img src="https://news.lenovo.com/wp-content/uploads/2020/10/phishing-illustration.jpg" />
</p>
Internet and digital world are growing every day and everyone is becoming part of this world.
Because of this growth, everyday a new information or technology is entering this world. Most
people can’t track these new developments and they become target for deceiving. By creating
similar websites to authentic sites, people are getting deceived and and their information is
stolen by the creators of these phishing websites. In this paper, a model has been proposed to
detect phishing websites by using machine learning methods. Machine learning was done using
a certain data set and the best model was selected because of testing more than one model.

## Methodology
We used grid search and cross validation for model selection. Trained 3 different algorithms (and Neural Nets.) with various parameters. We set paramaterer grids and use cross validation for avoid overfitting. We use precision and recall rather than accuracy. Because accuracy not always gives best results. A

**Here is the structure of our models:**


![structure](static/images/structure.jpg "Structure")

## Results
After the grid search CV we choose the best performanced algorithm which is Random Forest Classifier. Actually all algorithms gave good performances including Neural Nets. But we choose best one which is Random Forest Classifier.

**Here is the Precision and Recall Scores of Algorithms**

| Algorithm                     | Precision | Recall|
|----------------------------|---------------|-------------|
| Random Forest Classifier            |      0.954       |      0.954      |
| XGBoost Classifier          |          0.930     |      0.929      |
| KNeighbors Classifier          |       0.881       |      0.880      |


Also we deploy our model using Heroku and Flask. Here is the interface of our web deployment.


**Here is the demo link for deployment**: https://predicting-phishing-or-not.herokuapp.com/

This repository is created by [Ozgur Dogan](https://github.com/ozgurdogan646), [Gulcin Betul Cetres](https://github.com/gulcinbetulcetres) and [Okan Bagriacik](https://github.com/OkanBagriacik).
