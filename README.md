# TrialApp
A simple Django application to manage sea trials.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup & Usage](#setup-&-usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information
The Idea for the app was born cause I have been working in the shipbuilding industry for several years and my company had a problem with accounting for sea trial.
The construction of the ship is divided into a few stages. The main stages of building a ship are designed, purchasing, building, commissioning and trials at sea. 
This app focuses on dock trials and sea trial phase. 
During sea trials, the shipowner and the contractor supervise if scheduled trials go according to the trial plan.
If the ship's performance and efficiency are as previously agreed, the trials are passed.

If the ship fails sea trial. The shipowner has the right to request corrections to the tested areas. The application allows you to create a list of sea trials and assign comments to them if the trial was not successful.

> More about sea trials https://en.wikipedia.org/wiki/Sea_trial

## Technologies Used
- asgiref==3.6.0
- Django==4.1.5
- django-filter==22.1
- django-widget-tweaks==1.4.12
- sqlparse==0.4.3
- tzdata==2022.7
- unicodecsv==0.14.1

## Features
List the ready features:
- CRUD for Dock Trials
- CRUD for Dock Trials comments
- Export data(Dock Trial and Dock Trial comments) to .csv file
- User registration
- CRUD for User
- User password change
- filters for Dock Trials and dock Trial comments

## Setup & Usage
Write in cmd: 

To create database and migrate

```py manage.py migrate```

To load sample data into the database

```py manage.py loaddata data.json```

To web server on the local machine

```py manage.py runserver```



## Project Status
The Project is in progress. I will try to add some new features in the future.

## Room for Improvement

Room for improvement:
- CRUD user


To do:
- CRUD Sea Trial
- CRUD Sea Trial comments
- User password reset
- …



## Contact
Created by micwoszk@wp.pl - feel free to contact me!
