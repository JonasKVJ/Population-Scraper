#Author: Jonas Stagnaro
#Date: 08-04-20
#Project: Population Comparator

from bs4 import BeautifulSoup
from django.http import HttpResponse

import datetime
import requests

def index(request):
    united_states_population_page = requests.get("https://en.wikipedia.org/wiki/United_States")
    india_population_page = requests.get("https://en.wikipedia.org/wiki/India")

#Type conversion: list object -> list of strings -> string -> int
    soup = BeautifulSoup(united_states_population_page.content, 'html.parser')
    table_desc = soup.select("table .mergedrow td")
    population_row = list(table_desc[16])
    population_obj = list(population_row[1])
    string_list = [str(number) for number in population_obj]
    string_with_commas = "".join(string_list)
    population_string = string_with_commas.replace(',', '')
    united_states_population = int(population_string)

    soup = BeautifulSoup(india_population_page.content, 'html.parser')
    table_desc = soup.select("table .mergedrow td")
    population_row = list(table_desc[15])
    population_obj = list(population_row[0])
    string_list = [str(number) for number in population_obj]
    string_with_commas = "".join(string_list)
    population_string = string_with_commas.replace(',', '')
    india_population = int(population_string)

return HttpResponse("""<html><body><h2>Population Statistics</h2><table border=true><t
r><th>Country</th><th>Current Population Size</th></tr><tr><td>United States</td><td>%s</t
d></tr><tr><td>India</td><td>%s</td></tr></table></body></html>
                    """ % (united_states_population,india_population))