#Script periodically checks for goals on the BBC website 
#Pushes a notification to Linux desktop

import requests, bs4

res = requests.get('https://www.bbc.co.uk/sport/football')

res.raise_for_status()
