import requests
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup

# page = requests.get('https://socialblade.com/youtube/top/50')

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999'
                    '#.XjV_uHUzbeQ')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('a'))       # find all <a>

week = soup.find(id='seven-day-forecast-body')  # taking the container for week
# print(week)     # showing only the container script

# print(week.find('li'))      # print all the li tags
items = week.find_all(class_='tombstone-container')  # print the week container
# print(items[1])

'''
Take all of the short description and temperature in different columns
'''
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_descriptions)
# print(temperatures)

weather_stuff = pd.DataFrame(
    {'Period': period_names,
     'Short Descriptions': short_descriptions,
     'Temperatures': temperatures,
     })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
weather_stuff.to_excel('weather.xlsx')
weather_stuff.to_html('weather.html')
