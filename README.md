# storeManager-api  
[![Build Status](https://travis-ci.com/probuse/storeManager-api.svg?branch=master)](https://travis-ci.com/probuse/storeManager-api)
[![Coverage Status](https://coveralls.io/repos/github/probuse/storeManager-api/badge.svg?branch=master)](https://coveralls.io/github/probuse/storeManager-api?branch=master)
StoreManager-api is an API for the storeManager web application.  
StoreManager is a web application that helps store owners manage sales and product inventory records

## How to run it
To get the project  
`git clone https://github.com/probuse/storeManager-api.git `

Then:  
`cd  storeManager-api`

Run the api:  
`python run.py`

The api is now running on your local host at url ` http://127.0.0.1:5000/`

## How to access the endpoints
* http://127.0.0.1:5000/api/v1/products - returns a list of all products

## Dependencies
* Flask
* Flask-restful
* pytest
