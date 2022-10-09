
#Factored Assessment
# For the database
### go to "/factored_assessment_db"

image creation: 
```
   $ docker build -t factored_assessment_db . 
```
run container:
```
docker run -d -t -i -p 3306:3306 --name factored_assessment_db factored_assessment_db
```
run phpMyAdmin:
```
docker run --name db_client -d --link swarch2022ii_db:db -p 8081:80 phpmyadmin
``` 

# For the Backend
### go to "/factored_assessment_ms"

start python's virtual environment:
```
env\Scripts\activate 
```
If missing, install libraries:
```
pip install fastapi uvicorn sqlalchemy pymysql
```
Go to the API Rest in this direction:
```
http://localhost:8000/docs
```

# For the Frontend
### go to "/factored_assessment_fe"

If missing, install:
```
npm install --save react-modal-login  
```
```
npm i react-inlinesvg
```
To run the React component:
```
npm start
```
To see the UI go to:
```
http://localhost:3000/
```