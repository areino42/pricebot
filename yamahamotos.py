################# YAMAIMPORT LTDA #######################



from bs4 import BeautifulSoup
import requests
from datetime import date



#### MOTOS

url= "http://www.yamahamotos.cl/productos/motos/"
r  = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
b = soup.find_all('li',{ "class" : "itemprod" })



for li in b:
    sql="insert into yamaha values("
    marca = "'yamaha',"
    categoria = "'" + ' '.join(li['class'])+ "',"   
    
    sql_values_modelo="" 
    for c in li.find_all("h3"):
        v=c.text
        sql_values_modelo= sql_values_modelo+"'"+ v.replace("'"," ") + "'," 
    
    sql_values_precio=""
    for d in li.find_all("p",{ "class" : "elprecio" }):
        w=d.text
        sql_values_precio= sql_values_precio+"'"+ w.replace("'"," ") + "'," 
                                                           
    time = "'"+str(date.today())+"'"

                              
    p = (sql + marca + categoria + sql_values_modelo + sql_values_precio + time + ")" )    
    print p


### ATV


url= "http://www.yamahamotos.cl/productos/atv/"
r  = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
b = soup.find_all('li',{ "class" : "itemprod" })



for li in b:
    sql="insert into yamaha values("
    marca = "'yamaha',"
    categoria = "'" + ' '.join(li['class'])+ "',"   
    
    sql_values_modelo="" 
    for c in li.find_all("h3"):
        v=c.text
        sql_values_modelo= sql_values_modelo+"'"+ v.replace("'"," ") + "'," 
    
    sql_values_precio=""
    for d in li.find_all("p",{ "class" : "elprecio" }):
        w=d.text
        sql_values_precio= sql_values_precio+"'"+ w.replace("'"," ") + "'," 
                                                           
    time = "'"+str(date.today())+"'"

                              
    p = (sql + marca + categoria + sql_values_modelo + sql_values_precio + time + ")" )    
    print p



### UTV


url= "http://www.yamahamotos.cl/productos/utv/"
r  = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
b = soup.find_all('li',{ "class" : "itemprod" })



for li in b:
    sql="insert into yamaha values("
    marca = "'yamaha',"
    categoria = "'" + ' '.join(li['class'])+ "',"   
    
    sql_values_modelo="" 
    for c in li.find_all("h3"):
        v=c.text
        sql_values_modelo= sql_values_modelo+"'"+ v.replace("'"," ") + "'," 
    
    sql_values_precio=""
    for d in li.find_all("p",{ "class" : "elprecio" }):
        w=d.text
        sql_values_precio= sql_values_precio+"'"+ w.replace("'"," ") + "'," 
                                                           
    time = "'"+str(date.today())+"'"

                              
    p = (sql + marca + categoria + sql_values_modelo + sql_values_precio + time + ")" )    
    print p
