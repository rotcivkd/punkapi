# -*- coding: utf-8 -*-

import requests
import json
from sys import argv

def retrieve_beerlist(api_url):
    pagination = 0
    allItems = []
    while True:
        #pagination increamenter
        pagination = pagination+1
        url_with_pagination = api_url+'&page='+str(pagination)+'&per_page=80'
        try:
            response = requests.get(url=url_with_pagination)
            res = response.json()
        except:
            res=''
        if len(res) == 0:
            break
        else:
            for element in res:
                allItems.append(element)
    return(allItems)
            
        
#Starting of the program  
var = argv[1] #first argument retrieve list by
var = var.lower()
output = argv[-1] #output file location

API_url = 'https://api.punkapi.com/v2/beers'

if var == 'beer-list':
    b_from = argv[2].split("=")[1]
    b_until = argv[3].split("=")[1]
    #Form a url with pagination as more number of records may expected in brewed case
    url = API_url+'?brewed_before='+b_until+'&brewed_after='+b_from
    beer_list = retrieve_beerlist(url)
    #create output file name based on input parameter
    ouput_filename = 'beer-list_'+'from'+b_until+'to'+b_from+'.json'
if var == 'beer-id':
    beer_id = argv[2]
    url = API_url+'?ids='+str(beer_id)
    beer_list = retrieve_beerlist(url)
    ouput_filename = 'beer-id_'+str(beer_id)+'.json'
if var == 'beer-name':
    beer_name = argv[3]
    url = API_url+'?beer_name='+str(beer_name)
    beer_list = retrieve_beerlist(url)
    ouput_filename = 'beer_name_'+str(beer_name)+'.json'

if len(beer_list) == 0:
    print ("Beer list is not retrieved, either data not available in API for the given input or API is not reachable")
else:
    ouput_filename = output+'\\'+ouput_filename
    #Write output file
    with open(ouput_filename, 'w') as file:
        file.write(json.dumps(beer_list))
    print ("Results written to the location - {}".format(output))
    