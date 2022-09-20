# Pet Marketplace
This is a sample flask full stack web application that allows user to buy pets. 

Application files are structured inside core package.

The application consists of three pages.

1. Welcome Page:
    1. In this page, user will enter their name and then they will be redirected to Home Page.
    
2. Home Page:
    1. Here, user can select the pet they want to buy. They are given two options; Dog and Cat.
    2. Whenever user buys the pet, on the right side of the page user can see list of their pets with their serial numbers and sound
    
3. Admin Page:
    1. In the welcome page, when the user enters the name of the admin i.e. administrator (as defined in the ![config](./core/config.py) file), 
    they will be redirected to admin page.
    2. In the admin page, user will be able to see the list of all pets and their owner.


## How to run this application ?

Please, follow these steps to successfully run this application on your local machine:

1. Make sure you have the following dpendencies in your development environment:

    1.  Python 3.8.10 (You can be flexible with the version but, application is tested with this version only).
    2.  Any IDE or text editor of your choice.
    3.  Access to Command-Line or Terminal.

2. Clone this repository in your working directory.
3. In your terminal or command line, make sure you are pointing to working directory.
4. Now, go to root direcotry of this application i.e. 'pet-marketplace'.
5. Create python virtual environment (Recommended). Make sure you activate the virtual environment.
6. Install the dependencies by typing following command:

      `pip install -r requirements.txt`

6. Initialize the database. This application uses sqlite database. Type following command:
 
    `flask --app core init-db`
 
    This command will create database files inside 'tmp' directory and database tables as defined in the models. 

7. Now the flask application setup is complete, to run it application using development server, type:

      `flask --app core run -h localhost -p 3000`
      
    This command runs the core application package in <b>localhost:3000</b>. 
    
Now you can go to the browser, and enter <b>http://localhost:3000/</b> to start playing with this application :smile:

## Why Python ?

Our goal is to build a dynamic web application per the project requirements. As this project requires, ORM and template engines, it’s better to use a programming language that’s been used to build web application frameworks. Using frameworks, we can build an application that follows a consistent workflow and codebase by following its guidelines. In addition to this metric, I selected the initial list of programming languages using the following criterias.

