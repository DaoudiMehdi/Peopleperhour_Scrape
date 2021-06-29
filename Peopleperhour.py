
import requests
from bs4 import BeautifulSoup
import pandas as pd

mylist=[]
service = input("Enter service name :")
max_page = int(input("Enter number of pages : "))
max_page= max_page+1
service = service.replace(" ", '+')

def funcurl(link):

  lien= requests.get(link)
  soup= BeautifulSoup(lien.text , 'lxml')
  try:
   name = soup.find('header' ,class_="clearfix").text.replace("  " , "").replace("\n" , "")
  except Exception:
     name = "null"
  try:
    price = soup.find('div' ,class_="price-container text-center gutter-bottom").text.replace(" " , "").replace("\n" , "") 
  except Exception:
     price = "null"
  try:
    delivery = soup.find('span' , class_="value js-delivery-days").text
  except Exception:
    delivery="null"

  try:  
    divv = soup.find_all('div' , class_="col-xs-4 text-center no-padding popover-toggle")[1]
    rating=divv.find('span' , class_="value").text
  except Exception:
    rating="null"
  try:
    ul = soup.find('ul' , class_="horizontal")
    views=ul.find_all('span' , class_="value")[0].text
    sales=ul.find_all('span' , class_="value")[1].text
  except Exception:
    views="null"
    sales="null"
  try:
    seller =soup.find('a', class_="crop member-short-name").text
  except Exception:
    seller= "null"
  try:
    seller_jobs=soup.find('div', class_="member-job-title crop").text
  except Exception:
    seller_jobs="null"
  data= {
    "Name" : name,
    "Price": price,
    "Delivery" : delivery,
    "Seller" : seller,
    "Seller jobs" : seller_jobs,
    "View":views,
    "Sales" :  sales,
    "Rating" : rating,
    "Link" : link

    }
  return data
  


  
for i in range(1,max_page):



  url = f"https://www.peopleperhour.com/services/{service}?page={i}&ref=search"

  lien= requests.get(url)
  soup= BeautifulSoup(lien.text , 'lxml')

  rows= soup.find_all('div' , class_="card⤍HourlieTile⤚3DrJs")
  for row in rows:
    link = row.a['href']
    data=funcurl(link)
    mylist.append(data)


df=pd.DataFrame(mylist)



df.to_csv (r'./Peapoleperhour.csv', index = False, header=True)

#by_daoudimehdi980@gmail.com