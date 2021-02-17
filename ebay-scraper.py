from bs4 import BeautifulSoup
import requests
import os

def niko():
  item_name = input("input item name: ")
  html = requests.get(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={item_name}&_sacat=0")
  bs = BeautifulSoup(html.text, "lxml")
  all_items = bs.find_all("div", class_= "s-item__info clearfix") 
  for item in all_items:
    ebay_title = item.find("h3", class_= ["s-item__title s-item__title--has-tags", "s-item__title"])
    ebay_price = item.find("span", class_="s-item__price")
    niko = open("niko.txt", "a")
    niko.write(f'''
{ebay_title.text} 
{ebay_price.text}
\n
  ''')


niko()