#Script periodically checks for goals on the GOAL website 
#Pushes a notification to Linux desktop

import requests, bs4, time

url = 'https://www.goal.com/en-gb/team/manchester-united/fixtures-results/6eqit8ye8aomdsrrq0hk3v7gh'

def match_finder(match_status):
    '''Finds the current game based on which games have FT'''
    match_count = 0
    for match in match_status:
        full_time = match.span
        print('Fulltime',full_time)
        if full_time != None:
            match_count += 1
            if full_time.string != 'FT':
                return match_count - 1


def get_data():
    res = requests.get(url)
    res.raise_for_status()

    soupified = bs4.BeautifulSoup(res.text)
    goals = soupified.find_all(class_="goals")
    teams = soupified.find_all(class_="team-name")
    match_status = soupified.find_all(class_='match-status')
    match_number = match_finder(match_status)
    print(match_number)
    print(teams[match_number*2].string)
    print(teams[(match_number*2)+1].string)

    print(goals[match_number*2].string)
    print(goals[match_number*2].string)

###MAIN LOOP
while True:
    get_data()
    time.sleep(60)