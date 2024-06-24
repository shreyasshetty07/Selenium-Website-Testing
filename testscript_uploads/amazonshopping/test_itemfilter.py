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
  
  
driver.get("http://dummymensapparel.great-site.net/itemcategory.php?catid=1")
driver.set_window_size(1552, 832)
"""
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "password").click()
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "login_user").click()
driver.find_element(By.ID, "shirt").click()
"""
driver.find_element(By.ID, "casual").click()
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
driver.find_element(By.CSS_SELECTOR, "h3:nth-child(2)").click()
get_text=driver.find_element(By.CSS_SELECTOR, "h3:nth-child(2)").text
if get_text=="Items Count: 3":
    t1="Occasions Filter Working"
    stat="Pass"
else:
    t1="Filter option not Working :("
    stat="Fail"
driver.close() 
ts=datetime.datetime.now()
date_time=ts.strftime("%d-%m-%Y, %H:%M:%S")
f = open("..\\file2.txt", "a")
f.write("\nTest Case on Item Filters")
f.write("\n"+date_time+"   Run 1:"+"\t"+t1)
f.close()

db = mongo_db.TestLogs
coll = db.TestColl
cursor = coll.find({"TestName": "Filter on Items"}).sort('id', -1).limit(1)[0]
print(cursor)
data=dict()

data["id"]=int(cursor["id"]) + 1
data["TestName"]="Filter on Items"
data["time"]=datetime.datetime.now()
data["Output"]=t1
data["status"]=stat
x=coll.insert_one(data)