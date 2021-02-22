# FlaskNoteDetector
Using a data set creating a flask API for predicting using variance,skewness,curtosis,entropy
Problem : check image of notes and check .
Kaggle dataset : data was extracted from authentic and forge notes 
, converted to 400 * 400 and to gray-scale pictures with a resolution of 660 dpi

Kaggle problem : https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

# Deployed App Demo 
- Deployed app : https://flassger-banknote.herokuapp.com/
- Flasgger API : https://flassger-banknote.herokuapp.com/apidocs/ 

# How to install ? 
Clone the repo and simply use pip install -r requirements.txt to get all the dependencies.You can also create a seperate virtual environment for this process :-
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

# How to deploy on Heroku ? 
You can follow these steps to run Flask App on Heroku

 1. Install Heroku CLI ( https://devcenter.heroku.com/articles/heroku-cli ) 
 2. Push your code to git and create a heroku app ( https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#introduction)
 3. Define Procfile and install gunicorn dependency (pip install gunicorn)
add this entry to your profile

           web: gunicorn BankNote_FLASGER_API:app

where BankNote_FLASGER_API is the name of the python file and app is the name of flask app defined in the python file

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#define-a-procfile

 4. Save the dependency using pip freeze > requirements.txt and push code to github and heroku by using 

                 git push heroku main 

You can take a reference from my github flask Banknote repository which is deployed on heroku 

Github Link : https://github.com/Anirudh-thakur/FlaskNoteDetector

Heroku Link : https://flassger-banknote.herokuapp.com/apidocs

# How to create Docker image:-
1. Download docker (https://www.docker.com/products/docker-desktop)
2. Taking image for docker (continuumio/anaconda3:4.4.0) and creating docker file
3. Build docker image :
docker build -t money_api .
4. See the docker ( docker ps )
5. Run docker : docker run -p 8000:8000 money_api 

docker inspect money_api ( to get details )

common commands : 

FROM - Host system

COPY - would copy web app to root folder 

EXPOSE - expose port for accessing web app

WORKDIR - what is the working directory of code 

RUN - install requirement.txt 

CMD - python app.py (the file which will run the whole webApp)


# Steps followed :- 
1. Import data set 
2. split into dependent and independent variable 
3. test train split
4. Create random forest classifier 
5. Save predictor as pickle 
6. Create api using flask
7. Create get and post req 
8. Use postman to test 
9. Create swagger interface using flassger
10. Deploy on Heroku
11. Installing docker and creating DockerFile 

# References 
https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524

https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

https://www.youtube.com/watch?v=ipFUANeStYE

https://github.com/krishnaik06/Dockers

https://www.freecodecamp.org/news/how-to-get-a-docker-container-ip-address-explained-with-examples/

