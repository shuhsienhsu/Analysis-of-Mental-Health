import csv
import requests

url_continent = 'http://apps.who.int/gho/athena/data/GHO/SDGSUICIDE,SDG_SH_STA_SCIDEN?filter=COUNTRY:-;REGION:*&x-sideaxis=REGION;SEX&x-topaxis=GHO;YEAR&profile=crosstable&format=csv'
r_continent = requests.get(url_continent)
r_continent.encoding = 'utf-8'
with open('suicide_rate_continent.csv', 'w', encoding = 'utf-8') as w:
    w.write(r_continent.text)
with open('suicide_rate_continent.csv', 'r', encoding = 'utf-8') as r:
    with open('suicide_rate_continent_title.csv', 'w', encoding = 'utf-8') as w:
        r.seek(0)
        r.readline()
        for line in r:
            w.write(line)

url_governance = 'http://apps.who.int/gho/athena/data/GHO/MH_25,MH_1,MH_2,MH_3,MH_4,MH_5?filter=COUNTRY:*;REGION:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR&profile=crosstable&format=csv'
r_governance = requests.get(url_governance)
r_governance.encoding = 'utf-8'
with open('governance.csv', 'w', encoding = 'utf-8') as w:
    w.write(r_governance.text)
with open('governance.csv', 'r', encoding = 'utf-8') as r:
    with open('governance_title.csv', 'w', encoding = 'utf-8') as w:
        r.seek(0)
        r.readline()
        for line in r:
            w.write(line)

url_unemployment = 'https://quality.data.gov.tw/dq_download_csv.php?nid=6637&md5_url=81f98a3d1e7745c7a86108c9fb885dda'
r_unemployment = requests.get(url_unemployment)
r_unemployment.encoding = 'utf-8'
with open('unemployment.csv', 'w', encoding = 'utf-8') as w:
    w.write(r_unemployment.text)

url_taiwan_suiciderate = "http://tspc.tw/tspc/uploadfiles/Image/106_suicide_rate.png"
response = requests.get(url_taiwan_suiciderate)
if response.status_code == 200:
    with open("taiwan_suiciderate.jpg", 'wb') as f:
        f.write(response.content)

url_taiwan_suiciderate_age = "http://tspc.tw/tspc/uploadfiles/Image/106_suicide_rate(age%20group).png"
response = requests.get(url_taiwan_suiciderate_age)
if response.status_code == 200:
    with open("taiwan_suiciderate_age.jpg", 'wb') as f:
        f.write(response.content)





#output = open('first_edit.csv', 'wb')
#writer = csv.writer(output)
#for row in csv.reader(input):
 #   if row[2]!=0:
  #      writer.writerow(row)

    #text3 = json.load(k)