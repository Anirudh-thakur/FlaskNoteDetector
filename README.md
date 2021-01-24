# FlaskNoteDetector
Using a data set creating a flask API for predicting using variance,skewness,curtosis,entropy
Problem : check image of notes and check .
Kaggle dataset : data was extracted from authentic and forge notes 
, converted to 400 * 400 and to gray-scale pictures with a resolution of 660 dpi

Kaggle problem : https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

Steps followed :- 
1. Import data set 
2. split into dependent and independent variable 
3. test train split
4. Create random forest classifier 
5. Save predictor as pickle 
6. Create api using flask
7. Create get and post req 
8. use postman to test 
9. Create swagger interface using flassger
10. Deploy on Heroku