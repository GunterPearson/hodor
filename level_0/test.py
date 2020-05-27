#!/usr/bin/python3

from lxml import html
import requests

page = requests.get("http://158.69.76.135/level0.php")
pload = {'id': '1715', 'holdthedoor':'submit'}
for x in range(1024):
    r = requests.post("http://158.69.76.135/level0.php", data = pload)
print("done!")
