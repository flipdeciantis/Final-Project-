# Final-Project-

## Description

### This app is designed to fetch retail sales, GDP data, and a given stock. It also provides a graph with the data overlaid for easy interpretation.

## Functionality

### The user is asked to input a stock symbol (i.e. "NFLX").

### A request is made for the current levels of the retail sales, GDP data, and stock price.

### Data is compiled and exported to a CSV file.

## Information Requirements

### Information Inputs

#### Chosen stock symbol
#### API response

### Information Outputs

#### API request
#### Retail sales level
#### GDP level
#### Stock level
#### CSV file export

## Setup


Create and activate a virtual environment:

```sh
conda create -n project-env python=3.8

conda activate project-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```


### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```
