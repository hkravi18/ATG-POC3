# Import beautiful soup library for html parsing
from bs4 import BeautifulSoup

# Importing selenium for browser based web scraping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Importing csv to create csv file with product details
import csv

# Chrome webdriver to open the webpage 
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    """
    Initializes and returns a Chrome WebDriver (opens chrome browser).
    """
    
    # Set up Chrome driver using ChromeDriverManager to handle driver setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def load_page(driver, url):
    """
    Loading the webpage in the given driver and wait until the URL is the expected one.
    """
    
    # Waiting for elements to load
    wait = WebDriverWait(driver, 10)
    
    # Navigate to the provided URL
    driver.get(url)
    
    # Waiting until loaded page url matches the expected URL
    wait.until(EC.url_to_be(url))
    
    # Return the current URL after waiting
    return driver.current_url

def parse_page(driver):
    """
    Parses the page source of the currently loaded page in the driver and extracts data.
    """
    # Extract the page source
    page_source = driver.page_source
    
    # Using BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, features="html.parser")
    
    # Find all 'div' elements with class 'slAVV4' (Flipkart product div specific class name)
    divs = soup.find_all('div', class_='slAVV4')
    
    # Returning all divs (all products on the page)
    return divs

def extract_and_display_data(divs):
    """
    Extract and print data from the parsed div elements.
    """
    
    product_details = []
    
    # Loop through each div (product) and extracting required details
    for div in divs:
        
        # Name of the product
        name = div.find('a', class_="wjcEIp").text
        
        # Price of the product
        price = div.find('div', class_="Nx9bqj").text
        
        # Rating of the product
        rating = div.find('div', class_="XQDdHH").text
        
        # Adding the product details to the list
        product_details.append({
            "name": name,
            "price": price,
            "rating": rating
        })        
        
    # Returning product details list
    return product_details

def write_to_csv(data, filename='product_details.csv'):
    """
    Function to write the extracted data to a CSV file.
    """
    fieldnames = ['name', 'price', 'rating']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    """
    Main function to start web scraping.
    """
    
    # Webpage URL
    url = "https://www.flipkart.com/6bo/ai3/3oe/~cs-eg8ins5tde/pr?sid=6bo%2Cai3%2C3oe&collection-tab-name=Keyboard-BDS&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkRlYWwncyBZb3UgQ2FuJ3QgUmVzaXN0ISJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&nnc=31GOFF5R8QLX_MERCH&otracker=bp_browse_announcement_6bo%2Cai3%2C3oe"
    
    # Initialize the web driver
    driver = initialize_driver()
    
    # Load the webpage
    current_url = load_page(driver, url)
    
    # Checking if the loaded URL matches the expected URL
    if current_url == url:
        # Parsed data (product divs)
        divs = parse_page(driver)
        # Extracting details
        product_details = extract_and_display_data(divs)
        write_to_csv(product_details)
        
    
    # Close the web driver
    driver.quit()

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
