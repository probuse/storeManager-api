# storeManager-api  
[![Build Status](https://travis-ci.com/probuse/storeManager-api.svg?branch=develop)](https://travis-ci.com/probuse/storeManager-api)
[![Coverage Status](https://coveralls.io/repos/github/probuse/storeManager-api/badge.svg?branch=develop)](https://coveralls.io/github/probuse/storeManager-api?branch=develop) 
[![Maintainability](https://api.codeclimate.com/v1/badges/612965a0756ff1a779fd/maintainability)](https://codeclimate.com/github/probuse/storeManager-api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/612965a0756ff1a779fd/test_coverage)](https://codeclimate.com/github/probuse/storeManager-api/test_coverage)
[![codecov](https://codecov.io/gh/probuse/storeManager-api/branch/master/graph/badge.svg)](https://codecov.io/gh/probuse/storeManager-api)



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
* http://127.0.0.1:5000/api/v1/products - `returns a list of all products`
* http://127.0.0.1:5000/api/v1/products/<product_id> - `returns a product with <product_id> as id`
* http://127.0.0.1:5000/api/v1/sales - `returns a list of all sales`
* http://127.0.0.1:5000/api/v1/sales/<sale_id> - `returns a sale with <sale_id> as id`

## Dependencies
* Flask
* Flask-restful
* pytest
