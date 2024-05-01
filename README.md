# Basic Web Scraping Script for Flipkart

## Project Description

This is a python script which will scrape **Flipkart** webpages to scrape the product details like name, price, rating.

## Table of Contents

- [File Structure](#file-structure)
- [Important Note](#important-note)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## File Structure 

- main.py (main python scripting file)
- README.md 

## Important Note

- This script is only valid for _Flipkart_ product pages not for any other webpage
- Replace the Flipkart page URL in the main.py and start the script
- It will generate a `product_details.csv` file which will contain all the details of the products

## Features

- Scrape Flipkart webpages to scrape the product details like name, price, rating

## Prerequisites

- Python [Installation Guide](https://www.python.org/downloads/)
- Ensure you have Python installed along with the `beautifulsoup4`, `selenium` and `webdriver-manager` libraries, which can be installed via pip:
    ```bash
    pip install beautifulsoup4 selenium webdriver-manager
    ```

## Installation

1. Clone the repository:

git clone <REPO_URL> 

2. Navigate to the project directory:

cd ATG-POC3

3. Put your Flipkart products page URL in main.py

4. Run the main python script `main.py`
    ```bash 
    python main.py
    ``` 

## Usage

- Just replace your URL in the main.py file with your own URL and then run the script
- Currently only supports Flipkart products pages 