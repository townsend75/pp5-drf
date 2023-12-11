# ArtXChange API

ArtXChange API is the backend service used by the [ArtXChange Application](https://pp5-frontend-4b5821b7dc88.herokuapp.com/)


## Development Goals

The API is designed to provide a backend service for the ArtXChange front end application, so that it can perform Create, Read, Update and Delete operations through the user interface.

## Agile Planning

The project was developed using agile methods.All stories were given labels to signify importance. The labels were Must have, Should have, Could have. The stories were completed in order of importance so as to ensure the core features were included in the project.

The Kanban board was created using Github projects. 

## User Stories

### Setup

- As a user i can create an account so that I can access all the features for signed in users
- As a developer I can set up the databases necessary for the project so that I can build the app

### Posts

- As a user I can create posts
- As a user I can edit and delete posts

### Profiles

- As a user i can create a profile
- As a user I can edit my profile
-As a developer I can provide a blank template with a default image

** API endpoints

User Story:
As a developer I can set up the databases necessary for the project so that I can build the app

The project was created in a virtual environment with all necessary packages installed and frozen in the requirements text.
The setting were edited to hide any secret variables.

User Story: 
As a developer I can connect with the cloudinary database so that images can be stored and uploaded

A cloudinary account was linked to the project so that images can be uploaded through the account.

User Story:
As a User I can create an account so that I can access all the website features

Django rest framework and dj-rest-auth were installed and added to the url patterns and site packages to make use of their built in authenification system.

Endpoint: /profiles

User Story:
As a developer I can create api views so that they are available on the front end

Methods:

-POST Create a user profile
-GET Retrieve a list of artists

Endpoint: /profiles/int:pk

Methods:

-GET View a single user profile
-PUT edit a user profile
-DELETE delete any given profile

User Story:
As a developer I can create a contact model so that users can contact the site administrators

Endpoint: /contacts

Methods: 

-POST contact the site administrators

Endpoint: /contacts/int:pk

- GET Retrieve a single contact
-PUT Update contact form
- DELETE Delete contact request

User Story
As a user I can create posts
As a user I can edit and delete my posts so that I have full control over my information

Endpoint: /posts

Methods:

-POST User to create a new post
-GET Retrieve a list of all posts

Endpoint /posts/int:pk

Methods:

-GET Retrieve a single post
-PUT Update a post
-DELETE Delete a post


## Security

The IsOwnerOrReadOnly class was added to ensure only the content creators can edit or delete the relevant information.

## Technologies

- Django
Main framework for App creation
- Django Rest Framework
Framework used for creating the API
-Heroku
Used to host the application
- Cloudinary
Used for image hosting
- Gitpod
Used for writing the relevant code
-Github
Repository for storing code


## Python Packages

- dj-database-url==0.5.0
Used to parse the DATABASE_URL connection settings
- dj-rest-auth==2.1.9
Authentification system
- Django==3.2.23
Main framework for starting the project
- django-allauth==0.44.0
Used for authentification
- django-cloudinary-storage==0.3.0
Used to connect with the cloudinary storage site
- django-filter==23.4
Used to filter API results in serializers
- djangorestframework==3.14.0
Framework used for building API endpoints
- djangorestframework-simplejwt==4.7.2
Used with django rest framework to create access tokens for aithentification
- gunicorn==21.2.0
Used for deployment of WSGI applications
- Pillow==8.2.0
Imaging library
- psycopg2==2.9.9
PostgreSQL database adaptor to allow deployed application to perform crud on the database
- PyJWT==2.8.0
Used to create python web tokens for authentification


## Testing


