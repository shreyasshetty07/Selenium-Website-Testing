import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pymongo import MongoClient 

#mongo_url="mongodb://localhost:27017"
mongo_url="mongodb+srv://testauto135:testauto@cluster0.zatvjbz.mongodb.net/"
mongo_db=MongoClient(mongo_url)
print(mongo_db.list_databases)

#create db
db=mongo_db["TestLogs"]


driver = webdriver.Chrome()
driver.get("http://dummymensapparel.great-site.net/index.php")
driver.find_element(By.CSS_SELECTOR, ".navbar:nth-child(15) #shopcart").click()
driver.find_element(By.CSS_SELECTOR, "h4").click()
#assert driver.find_element(By.CSS_SELECTOR, "h4").text == "Items in Cart: 4"
get_text=driver.find_element(By.CSS_SELECTOR, "h4").text
if get_text=="Items in Cart: 3":
    t1="Cart item count Verified!"
    stat="Pass"
else:
    t1="Cart item count do not match :("
    stat="Fail"
driver.close()
ts=datetime.datetime.now()
date_time=ts.strftime("%d-%m-%Y, %H:%M:%S")
f = open("..\\file2.txt", "a")
f.write("\nTest Case on Items in Cart")
f.write("\n"+date_time+"   Run 1:"+"\t"+t1)
f.close()

db = mongo_db.TestLogs
coll = db.TestColl
cursor = coll.find({"TestName": "Count of Items in Cart"}).sort('id', -1).limit(1)[0]
print(cursor)
data=dict()

data["id"]=int(cursor["id"]) + 1
data["TestName"]="Count of Items in Cart"
data["time"]=datetime.datetime.now()
data["Output"]=t1
data["status"]=stat
x=coll.insert_one(data)