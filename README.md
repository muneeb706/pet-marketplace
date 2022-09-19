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
