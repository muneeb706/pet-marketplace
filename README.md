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
      
    This command runs the core application package at <b>localhost:3000</b>. 
    
Now you can go to the browser, and enter <b>http://localhost:3000/</b> to start playing with this application :smile:

## Why Python ?

Our goal is to build a dynamic web application per the project requirements. As this project requires, ORM and template engines, it’s better to use a programming language that’s been used to build web application frameworks. Using frameworks, we can build an application that follows a consistent workflow and codebase by following its guidelines. In addition to this metric, I selected the initial list of programming languages using the following list of criteria.

1. Object Oriented Programming (OOP):
    1. OOP-based codebases are easier to extend and maintain.
2. Data Structures:
    1. Data structures of different types must be supported since runtime complexity is dependent on the type of data structures used.
3. Community support and Learning resources:
    1. Strong community support is necessary for the long-term maintenance of the project.
    2. Learning resources along with good documentation should be available for the developer’s guidance.
4. Platform independence:
    1. Very important for the long-term maintainability of the application as we might need to migrate our application from one type of application server to another.

Using the criteria above, here is the list of programming languages I chose for comparison:

1. JavaScript
2. Python
3. Ruby
4. PHP
5. Java

<b>Note:</b> We can satisfy our project requirements with all of these languages and their web frameworks. However, I chose Python for this project and discarded others because of following reasons:

Why not JavaScript ?

JavaScript is very flexible and it has implicit type conversions, which makes debugging and maintaining good code quality difficult. 
It has Protoype based object inheritance model which is different from class-based model. This inheritance model is counter-intuitive because in prototypal inheritance, objects inherit from other objects. Constructors never come into the picture.

Why not Ruby ?

Ruby enforces some paradigms strictly to write clean code you have to learn these paradigms, hence increasing learning curve.
This stringency, also causes difficulty in migrating codebase to another programming language when needed.

Why not PHP ?

Beacues of lots of reported security issues, and lack of library support for modern web application development, e-g lack of support for machine learning capabilities etc.

Why not Java ?

It is a statically typed language which results in verbose code base. Deployment process is not straightforward as it needs to be compiled, and deployment can get expensive, if not properly configured (JVM heap size) as it consumes a lot of memory.

Finally, I chose Python because of following reasons:

1. Rich support of libraries for almost all types of features you need to support modern web application development.
2. It is very easy to migrate python application from one platform to another.
3. Very strong community as it is used for many purposes.
4. Syntactically, it is very easier to understand and code. Developers can focus more on solving problem than fixing technical issues.
5. Personally, I have been developing in Python consistently for past two years. In my experience, it's better to stick with what you know unless another technology offers a significant advantage.

## Why Flask ?

There are many different python web frameworks available and they can be divided into two categories:

1. Full Stack
2. Non Full Stack

A full stack framework offers end-to-end solutions for developing web applications. In this category, <b>Django</b> is the only reliable option as it is being actively maintained and third-party plugins are being developed at a rapid pace to enrich web applications based on it. Other frameworks in this category, such as Web2Py and TurboGears, have become stale.

Non-full-stack frameworks provide solutions at the component level, for example, for the development of application servers. However, with the help of different plugins, we can connect different components of a web application. In this category, <b>Flask</b> and <b>Pyramid</b> are the most popular and have a strong community. There are others like CherryPy and Python Bottle but these are not well-maintained. CherryPy documentation is not up to the mark while, Python Bottle does not have great plugin support for common use cases like web forms integration with database models.

It was difficult to decide between Flask and Pyramid, as both of these frameworks are well suited for our requirements. In the end, I decided to go with <b>Flask</b> as Pyramid is well-suited for applications that will scale in the future and is relatively a bit heavier framework than Flask. Pyramid is also more flexible as it offers multiple options to do one thing, which is good but it comes with the risk of an incoherent codebase.

Before moving forward, I would also like to mention FastAPI framework which is built using Flask. This framework supports asynchronous code execution with the help of ASGI server. However, this is relatively new framework, stability and long term maintainability could be a problem in the future as the project grows. If performance was the essential requirement for our project then I would have considered FastAPI.

Now, the final battle was between Flask and Django. Flask is a minimalist framework, Django is a huge framework, offering many features and solutions right out of the box however, it is very big and unnecessary for small projects like ours. <b>Flask</b> is well-suited for this kind of small project, which are not likely to scale that much and we always have the option to enrich flask applications with the help of plugins as we need. Choosing Flask also helps in keeping application package size minimal hence, making deployments easier to manage. Flask also gives you full control over every single component of the application e-g it is relatively easier to switch between different ORMs and templating engines. We can have this flexibility in Django as well but at the cost of adding complexity in configuration.

## Why SQLAlchemy ORM ?

Since I decided to go forward with Flask, <b>SQLAlchemy</b> is the most popular ORM with it. However, before choosing SQLAlchemy for this project, I analyzed the pros and cons of different ORMs.

<b>Django ORM</b> is a default ORM for the Django Framework but it can be integrated with Flask. 
Even though Django itself is ideal for large and complex applications but its ORM is mainly suited for straightforward use cases and queries. This is probably because, it uses active record implementation, meaning, the database structure has to be in sync with the model's structure.
In my personal experience, I end up writing SQL for complex queries to improve performance in the Django projects.

Another option was to use <b>Peewee</b>, which is best suited for lightweight and simple projects like ours but, if our project grows then this would have caused some problems as it is not built for complex queries.

During my research, I found out about <b>Pony ORM</b>, which seemed very well suited for our project
but I had to discard it in favor of SQLALchemy because of my prior experience with it and I couldn’t find any significant reason to try out a new ORM which is not backed by a strong community as well.

Other than popularity and stability I chose SQLALchemy because it allows you to take full advantage of underlying database features, and it can be tuned for performance improvements. With this tuning, we can improve query performance especially, in the case of many-to-many relationships. SQLAlchemy uses data mapper implementation where models are not tied with underlying database structure hence allowing the flexibility of tuning. However, the codebase can get verbose.

## Why Jinja2 ?

Jinja2 is the default templating engine of Flask and a very popular one in the python community.
It has all the features for small to large-scale projects, ranging from filtering, and inheritance to ahead-of-time compilation. However, speed was not the main reason for choosing Jinja2, as performance bottlenecks in a web application are mostly in the data retrieval process/algorithm. Personally, I prefer templating engine with simple and neat syntax, where the focus should be more on how the content is rendered. The syntax should not obscure the content so that developers are able to find the content rendering logic inside markup tags easily.

Django template is another templating engine, which is very similar to Jinja2 and easy to use. Although there are some performance concerns with it I might have chosen this engine just because of its simplicity, but, it is difficult to integrate it outside of the Django ecosystem.

I also researched Mako, Chameleon, and Cheetah. Mako is a very easy and straightforward engine and is good for any type of project. I couldn’t find any significant reason not to use it for this project. It's just that Jinja2 is widely adopted and trusted. However, Mako is gaining popularity as its subsequent versions are improving, especially, in terms of performance. I didn’t like Chameleon because of its verbose syntax and Cheetah because of the lack of resources to learn.

## Why unittest ?

I compared only two libraries to choose from for unit testing. 

1. unittest 
2. pytest

To pick a library for unit testing, I take the following points into consideration:

1. Running time of unit tests as it affects the productivity of developers.
2. Provides an intuitive approach for dividing tests into three parts
    1. Arrange ( setup environment and data)
    2. Act (execute methods for testing)
    3. Assert (asserts the response of the executed methods)
3. Easy to configure, locally and in the CI/CD workflow.
4. Intuitive ways for mocking dependencies.
5. Ability to calculate code coverage.

Pytest and unittest both satisfy above conditions while pytest is more intuitive, simple, compact, and faster. However, for this project, I chose unittest as it comes with the python standard library and downloading another package for the simple project like ours was unnecessary.
