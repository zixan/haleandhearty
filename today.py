from lxml import html
import requests

r = requests.get(url='https://www.haleandheartytogo.com/store345/ajax.menu.php?action=get_category&category_id=1')

hxt = html.fromstring(r.text).xpath('//div[@id="Daily_Specials_-_A_la_Carte"]//div[@style="height:20px;padding:0px;display:table-cell;vertical-align:bottom;border:0px solid blue;"]')


for h in hxt: 
    a = h.xpath('(.//text())[position()=1]')[0].strip(); 
    if a:
        print a
