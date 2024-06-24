import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from pymongo import MongoClient 
from jproperties import Properties 

configs = Properties() 
  
with open('C:\\xampp\\htdocs\\Selenium-Website-Testing\\server\\ScriptData.properties','rb') as read_prop: 
    configs.load(read_prop) 
mongo_url={configs.get("MongoDB_Connect").data}
#mongo_url="mongodb+srv://testauto135:testauto@cluster0.zatvjbz.mongodb.net/"
mongo_db=MongoClient(mongo_url)
print(mongo_db.list_databases)

#create db
db=mongo_db["TestLogs"]
"""
#create Collection
coll=db.create_collection("TestColl") 
#create document
data=dict()
data["id"]=1
data["TestName"]="Login to the Website"
data["time"]=datetime.datetime.now()
data["status"]="Success"
x=coll.insert_one(data)
"""
# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)
web_url=configs.get("Login_URL").data
driver.get(web_url)

gmailId="hello@gmail.com"
passWord = "123"
try:
    loginBox = driver.find_element(By.NAME, 'email')
    loginBox.send_keys(gmailId)
 
    #nextButton = driver.find_elements_by_id('//*[@id ="identifierNext"]')
    #nextButton[0].click()
 
    passWordBox = driver.find_element(By.NAME, 'password')
    passWordBox.send_keys(passWord)
 
    nextButton = driver.find_element(By.NAME, 'login_user')
    nextButton.click()
# Get page title
    title = driver.title

# Test if title is correct
    assert 'Bootstrap Example' in title
    print("TEST 0: "+title+" test passed")
    print('Login Successful...!!')
    
except:
    print('Login Failed')
    
get_text=driver.title
if get_text=="Bootstrap Example":
    t1="Login Success"
    stat="Pass"
else:
    t1="Login Unsuccesfull"
    stat="Fail"
driver.close() 
ts=datetime.datetime.now()
date_time=ts.strftime("%d-%m-%Y, %H:%M:%S")
f = open("file2.txt", "a")
f.write("\nTest Case on login")
f.write("\n"+date_time+"   Run 1:"+"\t"+t1)
f.close()

db = mongo_db.TestLogs
coll = db.TestColl
cursor = coll.find({"TestName": "Login to the Website"}).sort('id', -1).limit(1)[0]
print(cursor)
data=dict()

data["id"]=int(cursor["id"]) + 1
data["TestName"]="Login to the Website"
data["time"]=datetime.datetime.now()
data["Output"]=t1
data["status"]=stat

x=coll.insert_one(data)

