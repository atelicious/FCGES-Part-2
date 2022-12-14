# ***FCGES Technical Exam Part 2 - Python Web Programming***

Made and designed by: Elhy Tablazon (@atelicious)

Date first published: 11-21-2022

### ***Description***
This is a REST API made using django framework and django rest framework in accordance with the part 2 of the technical exam for FCGES.

### ***Business Requirements***
Build a simple trading system as a pure REST API with the endpoints given below. We want the users to be able to place orders to buy and sell stocks and track the overall value of their investments. Stocks will have an id, name, and price.

### ***Technical Requirements***
- Create an endpoint to let the user place orders. Each order should have the stock, quantity, and price. Each order the user places should be recorded.
- Create an endpoint to retrieve the total value invested in the user’s portfolio. Plus points if the user can retrieve data on an individual stock.

### ***Solution***
- By using the api/order endpoint, the user can place a buy/sell stock order. 
- By using the api/customer endpoint, the user can view their overall portfolio valuation 
- By using the api/customer/`<str:stock_id>` endpoint, the user can view the transactions that they made under a specific stock.
<br>

## ***Trading System API Documentation***
<br>

### ***How to use this API***
<br>

#### ***To log in to the trading API:***
1. Log in to the trading API by creating a post request to the endpoint api/login containing the valid username and password of the user.

    - Example input json format: `{"username":"username", "password":"password"}`

2. If successful, the user will recieve an output like this: `{"expiry": "2022-11-21T01:04:01.567006Z", "token": "36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f"}`

3. Use the provided `token` from the return data in step 2 as the header authorization token for the proceeding requests.

#### ***To log out of the trading API:***
1. Log out of the trading API by creating a post request to the endpoint `api/logout` containing the header authentication token of the user.

    - Example: `curl -X POST http://localhost:8080/api/logout -H 'Authorization: Token 36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f'`

2. If successful, the user will be logged out of the trading API and the token will be deleted in the database.


#### ***To get the customer portfolio valuation:***

1. Login to the trading API and set the header authorization token to the token obtained when logging in. 
2. Create a get request to `api/customer` endpoint using the token as the authorization token.

    - Example: `curl -X GET http://localhost:8080/api/customer -H 'Authorization: Token 36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f'`
3. If successful, the get request will return the data containing the `name` and `portfolio value` of the user.

    - Example: `{
                "stocks": "user",
                "portfolio valuation": "1000.00"
            }`

#### ***To get the customer data for specific stock:***

1. Login to the trading API and set the header authorization token to the token obtained when logging in. 
2. Use the provided `token` from the return data in step 1 as the header authorization token for the proceeding requests.
3. Create a get request to `api/customer/<str:id>` endpoint using the token as the authorization token and `<str:id>` should represent the stock that the user wants to view e.g. `AC`, `BDO`, `AEV` etc.

    - Example: `curl -X GET http://localhost:8080/api/customer/AC -H 'Authorization: Token 36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f'`
4. If successful, the get request will return the data containing the `name` and `portfolio value` of the user.

    - Example: `[{
                    "stock_qty": 10,
                    "price": "6655.0000"
                },
                {
                    "stock_qty": 10,
                    "price": "-6655.0000"
                }]`

#### ***To place a buy/sell stock order:***

1. Login to the trading API and set the header authorization token to the token obtained when logging in. 
2. Use the provided `token` from the return data in step 1 as the header authorization token for the proceeding requests.
3. Create a post request to `api/order/` endpoint containing the stock id, quantity and price of the order that is being placed. 
    To create a buy order, the price of the order should be set to positive while to create a sell order the price should be set to negative.
    - Example json input for buy order: `{
                                            "stock_id" : "AC",
                                            "stock_qty": 10,
                                            "price": 6550.0
                                        }`
    - Example json input for sell order: `{
                                            "stock_id" : "AC",
                                            "stock_qty": 10,
                                            "price": -6550.0
                                        }`
4. If successful, the post request will return the data reflecting the data that is saved in the database.

    - Example output for buy order: `{
                "stock_name" : "Ayala Corporation",
                "stock_qty": 10,
                "price": "6550.0"
            }`
    - Example output for sell order: `{
                "stock_name" : "Ayala Corporation",
                "stock_qty": 10,
                "price": "-6550.0"
            }`

<br>

### ***Installation***
<br>

Clone this repository using git:
<br>
> git clone https://github.com/atelicious/FCGES-Part-2.git
<br>

or download the code files from github as zip.

then install these following packages manually:
- Django Framework 
- Django REST Framework 
- django-rest-knox 

or by using the provided requirements.txt file:
<br>
> pip install -r requirements.txt
<br>

Once the repository and dependencies are downloaded, change your current working directory to the project directory, then run the API server using:
<br>
> python manage.py runserver
<br>

To check if the server is running, the user can visit the link http://localhost:8080 either by using the browser or by sending a get request and the user will receieve a json response like this:

`{
    "API_NAME": "TRADING API",
    "ENDPOINTS": ["api/stocks", "api/customer", "api/order", "api/login", "api/logout", "api/customer/<str:id>"]
}`
<br>
<br>

### ***API ENDPOINTS***

This API provides several endpoints, each with different use cases. For example, "api/stocks" endpoint gives a comprehensive list of stocks available while "api/customer" provides the name of the user together with its portfolio valuation. Provided below are the list of API endpoints available.

### ***List of Available API Endpoints***
<br>

- ***api/stocks***
    - Description: This endpoint returns a json object containing the list of all `stocks` that are currently saved in the database.
    - Allowed Method(s): `GET`
    - Authentication required: `NO`
    - Sample return data:
        -   `{
            "stocks": [
            {
                "stock_id": "AC",
                "name": "Ayala Corporation",
                "price": "665.5000"
            },
            {
                "stock_id": "AEV",
                "name": "Aboitiz Equity Ventures, Inc.",
                "price": "56.7500"
            }, . . .
            }`
- ***api/customer***
    - Description: This endpoint returns a json object containing the `name` of the user currently logged in, together with the `portfolio valuation` of that user.
    - Allowed Method(s): `GET`
    - Authentication required: `YES`
    - Sample return data:
        -   `{
                "stocks": "user",
                "portfolio valuation": "1000.00"
            }`
    - Note: The `portfolio valuation` is encoded as a string as decimal values cannot be serialized in JSON format.
- ***api/customer/`<str:stock_id>`***
    - Description: This endpoint returns the transactions that the user had made under a specific stock.
    - Allowed Method(s): `GET`
    - Authentication required: `YES`
    - Sample return data:
        - if the data for the current stock exists:
            - `[{
                    "stock_qty": 10,
                    "price": "6655.0000"
                },
                {
                    "stock_qty": 10,
                    "price": "-6655.0000"
                }]`
        - if the data for the current stock does not exist:
            - `[]`
    - Note: The `<str:stock_id>` is a string that represents the stock that the user wants to get specifically. For example, if the user want to obtain information about their transactions
    in stock `AC` then the url would be something like this: `https://localhost:8080/api/customer/AC`
- ***api/order***
    - Description: This endpoint accepts a json object containing the `stock id`, `quantity` of the stock and the total `price` of the order. 
    Returns a json object containing the stock name, quantity, and the price of the order that is processed by the server.
    - Allowed Method(s): `POST`
    - Authentication required: `YES`
    - Accepted data format:
        -   `{
                "stock_id" : "AC",
                "stock_qty": 10,
                "price": 6550.0
            }`
    - Sample return data:
        -   `{
                "stock_name" : "Ayala Corporation",
                "stock_qty": 10,
                "price": "6550.0"
            }`
    - Additional Notes:
        - The `price` on the return data is encoded as a string as decimal values cannot be serialized in JSON format.
        - To denote the `buying` and `selling` of stock, the API checks for the arithmetic property of the price, meaning a 
        `positive` price value denotes a buying of stock while a `negative` value denotes selling of stock.
        - The API also double checks the price provided in the order, meaning if the order contains `10` stocks of `AC`, then the price should be equal to 
        the current price of `AC` multiplied by the quantity. 
        - The user can only sell stocks that they own, meaning if the user only has `10` stocks of `AC` in their portfolio then they can only sell a maximum of `10` stocks of `AC`.
- ***api/login***
    - Description: This endpoint accepts a json object containing the valid `username` and `password` of the user.
    Returns a json object containing the `token` needed for authenticating requests and the `expiry` of this token.
    - Allowed Method(s): `POST`
    - Authentication required: `NO`
    - Accepted data format:
        -   `{
                "username" : "username",
                "password": "password"
            }`
    - Sample return data:
        -   `{
                "expiry": "2022-11-21T01:04:01.567006Z",
                "token": "36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f"
            }`
    - Additional Notes:
        - In order to access the API endpoints that require authentication, the user must first login through the api/login endpoint to get an authorization token.
        - This authorization token is needed to be added on the headers of the requests being made
        to endpoints that require authentication. 
            - For example: `curl -X GET http://localhost:8080/api/customer -H 'Authorization: Token 36e078e307adc010c8591903d6e12fcd65158966c6ba9d75d5ae5b90ff2faa9f'`
- ***api/logout***
    - Description: This endpoint accepts a post request containing the valid `token` in the header of the request and logs out the current user.
    - Allowed Method(s): `POST`
    - Authentication required: `YES`
    - Additional Notes:
        - The current token being passed in this endpoint is also being deleted in the database. In order to create new requests, the user must login again and get a new authorization token.
<br>
