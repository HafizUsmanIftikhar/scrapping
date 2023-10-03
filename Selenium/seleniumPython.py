from selenium import webdriver
import pandas as pd
website='https://www.adamchoi.co.uk/'
path="/usr/bin/chromedriver"

driver=webdriver.Chrome(path)
driver.get(website)

all_matches_button=driver.find_element_by_x_path('//label[@analytic-event="All matches"]')
all_matches_button.click()
matches=driver.find_elements_by_tag_name('tr')

data = []
home_team = []
score = []
away_team = []

for match in matches:
    data.append(match.find_element_by_x_path('./td[1]').text)
    home_team.append(match.find_element_by_x_path('./td[2]').text)
    score.append(match.find_element_by_x_path('./td[3]').text)
    away_team.append(match.find_element_by_x_path('./td[4]').text)

df=pd.DataFrame({'data':data, 'home_team': home_team, 'score': score, 'away_team':away_team})
df.to_csv('football_data.csv', index=False)

driver.quit()
