# To-Do List Application

## Project description
The objective of this project is to develop an app for users to keep track of their daily and weekly tasks. Users can create an account, log in, and maintain a personalized to-do list. This application includes features such as task creation, editing, deletion, marking tasks as complete, adding descriptions and deadlines, and searching within the to-do list.
The project follows a [YouTube tutorial](https://www.youtube.com/watch?v=llbtoQTt4qw&ab_channel=DennisIvy) by Dennis Ivy.

## Project dependencies
* Django (4.2.11)

## Set up this App
1. Clone this repository.
2. Navigate to the todolist folder and run ```make install-dev```
3. Run migrations with ```make dev-migrate```
4. Create a superuser by running ```make dev-superuser```
5. Run ```make dev-start``` to check out the app in your browser under ```http://127.0.0.1:8000```