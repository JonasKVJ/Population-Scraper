#Author: Jonas Stagnaro
#Date: 08-04-20
#Project: Population Comparison App 

from bs4 import BeautifulSoup
from django.http import HttpResponse

import datetime
import requests

def index(request):
    united_states_population_page = requests.get("https://en.wikipedia.org/wiki/United_States")
    india_population_page = requests.get("https://en.wikipedia.org/wiki/India")

    #We pass the page into a constructor and parse the HTML of the page into a tree of Python objects
    soup = BeautifulSoup(united_states_population_page.content, 'html.parser')
    
    #Here, the BeautifulSoup library uses a CSS selector to match elements 
    table_desc = soup.select("table .mergedrow td") 
    
    #The result here is a small section of the table on the right side of the Wikipedia page
    population_row = list(table_desc[16])
    
    #Scraping of the population number of the United States Wikipedia page
    #Type conversion in the lines below: list object -> list of strings -> string -> int
    population_obj = list(population_row[1]) #Extraction of the population number entry of the selected table row from a list into a single object
    string_list = [str(number) for number in population_obj] #Convert the population number to a list of strings
    string_with_commas = "".join(string_list) #Convert the list of strings to one string
    population_string = string_with_commas.replace(',', '') #Remove all commas to get a usable number
    united_states_population = int(population_string) #Convert it to an int for even more applicability 

    #Scraping of the population number of the India Wikipedia page
    soup = BeautifulSoup(india_population_page.content, 'html.parser')
    table_desc = soup.select("table .mergedrow td")
    population_row = list(table_desc[15])
    population_obj = list(population_row[0])
    string_list = [str(number) for number in population_obj]
    string_with_commas = "".join(string_list)
    population_string = string_with_commas.replace(',', '')
    india_population = int(population_string)

    #Return a nicely formatted table with HTML
return HttpResponse("""<html><body><h2>Population Statistics</h2><table border=true><t
r><th>Country</th><th>Current Population Size</th></tr><tr><td>United States</td><td>%s</t
d></tr><tr><td>India</td><td>%s</td></tr></table></body></html>
                    """ % (united_states_population,india_population))
