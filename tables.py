from bs4 import BeautifulSoup
import  requests
import csv
import pandas as pd

url ="https://www.webometrics.info/en/africa/uganda?sort=asc&order=World%20Rank"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

#print (soup)

university_table = soup.find('table',class_ = 'sticky-enabled') 
print (university_table)
data = []

for university in university_table.find_all('tbody'):
    rows = university.find_all('tr')
    for row in rows:
        ug_rank = row.find_all('td', class_ = '')[0].text
        world_rank = row.find_all('td',class_ = '')[1].text
        univervesity_name = row.find_all('td',class_ = '')[2].text
        impact_rank = row.find_all('td',class_ = '')[4].text
        opennes_rank = row.find_all('td',class_ = '')[5].text
        excellence_rank = row.find_all('td',class_ = '')[6].text        
              
        data.append((ug_rank,world_rank,univervesity_name,impact_rank,opennes_rank,excellence_rank))     
   
    
df = pd.DataFrame(data, columns=['Ug. Ranking', 'Worl Ranking', 'University Name','Imapct Rank','Oppennes Rank','Excellence Rank'])
df.to_csv('D:webscraping/uni.csv',index = False,encoding = 'utf-8')