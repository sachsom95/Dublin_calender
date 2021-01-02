[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Dublin_calender
 
NOTE : for project tasks look here
[Project!!](https://github.com/sachsom95/Dublin_calender/projects/2)

### This is Dublin calendar the latest spaghetti creation.. 
Keep record of events in a calendar without an entire calender being shoved to the screen. Shows events, dates and descriptions.  Deployed in Heroku with postgres<p align="center">
  <p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/55349036/103449320-7667f400-4c9e-11eb-881f-35bbcfc47e4a.gif">
</p>

### CRUD operations are possible.
Nothing fancy here move on
<p align="center">
  <img width="600" height="400"src="https://user-images.githubusercontent.com/55349036/103449333-a9aa8300-4c9e-11eb-9df4-3544ec69d6ae.gif">
</p>


### wanna show others how busy you are .
Use the share calender to send links bhhhaamm!.


#### Still lot to impliment :(.


### How to run app locally

Here are the steps to properly run the application:<br>

- Create conda environment → "conda create --name calender_app=3.7" 
- Activate the environment → "conda activate calender_app"
- Go inside the project folder there should be a "requiments.txt"
- Run → "pip install -r requirments.txt"
- Now navigate to 'dublin_calender/dublin_calender/' on your terminal, you should now be able to see the manage.py file
- In terminal run following command "python manage.py makemigrations"
- Now run following command "python manage.py migrate"
- Finally run "python manage.py runserver" This will run the server go to the link being shown in terminal and the App should work 
- Create super user using → "python manage.py createsuperuser"


