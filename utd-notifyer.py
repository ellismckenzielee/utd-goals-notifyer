#Script periodically checks for goals on the GOAL website 
#Pushes a notification to Linux desktop

import requests, bs4

url = 'https://www.goal.com/en-gb/team/manchester-united/fixtures-results/6eqit8ye8aomdsrrq0hk3v7gh'

res = requests.get(url)
res.raise_for_status()

soupified_GOAL = bs4.BeautifulSoup(res.text)
goals = soupified_GOAL.select('.goals')
print(goals)