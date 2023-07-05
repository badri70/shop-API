# shop-API

## About application

This is a simple API for a store where you can get a list of products, 
get a specific product, add an item to your cart, 
and get a list of the items in your cart. Additionally, 
there is an authorization system for tokens.

## How to start the server?

You need to copy this application to your PC. 
Next, as soon as you open the application in your code editor, 
you need to install all the libraries you need using the `'pip install -r requirements.txt command'`.

Then, in the terminal, type the command `'python3 manage.py runserver'` after which you will start the local server. 
Additionally, you need to migrate all the tables that describe the database tables, use the `'python3 manage.py makemigrations'` 
command and then issue the `'python3 manage.py migrate'` command. 

After that, you will need to create a super user so that you can easily use the Django admin. 
To do this, enter the command `'python3 manage.py createsuperuser'` in the terminal, after which you will be asked to enter a username, email and password.

## Endpoints
This application has a registration and authorization system.
To register, you need to send a *POST* request to the address `'http://127.0.0.1:8000/api/v1/auth/users/'` in the body of the request, you need two mandatory fields **username and password**. 
Optionally, you can add email fields.

For authorization, you also need to send a *POST* request, but to the address `'http://127.0.0.1:8000/auth/token/login/'` in the 
request body you need two mandatory fields **username and password**. Upon successful authorization, a token will be returned to you.

To get a list of all products in the store, you need to send a *GET* request to `'http://127.0.0.1:8000/api/v1/products/'`, 
or you can get a specific product, just add the product id at the end. For example `'http://127.0.0.1:8000/api/v1/products/4/'`.

To add a product to the basket, you need to send a *POST* request to the address `'http://127.0.0.1:8000/api/v1/products/4/add_basket/'` 
but you already need to use the token that you received during authorization, you need to add it to the request header. **`For example Authorization: Token fadghpoawh4easl34lhopguo23.`** This is necessary so that the system knows that you are authorized. 
If this request is sent again, then the number will simply increase.

And in order to receive a list of goods in the basket, you need to send a *GET* request to `'http://127.0.0.1:8000/api/v1/basket/'` here you also need to add your authorization token.
