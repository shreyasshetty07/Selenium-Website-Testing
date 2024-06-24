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

pc=0
pf=0
# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)
web_url=configs.get("Login_URL").data
driver.get(web_url)

gmailId="vaadi@gmail.com"
passWord = "yoyo"
try:
    loginBox = driver.find_element(By.NAME, 'email')
    loginBox.send_keys(gmailId)
 
    passWordBox = driver.find_element(By.NAME, 'password')
    passWordBox.send_keys(passWord)
 
    nextButton = driver.find_element(By.NAME, 'login_user')
    nextButton.click()
# Get page title
    title = driver.title
    
except:
    print('Login Failed')
    
get_text=driver.title
if get_text=="Bootstrap Example":
    t1="Login Success"
    pc=pc+1;
    stat="Pass"
else:
    t1="Login Unsuccesfull"
    pf=pf+1;
    stat="Fail"
driver.close() 

#test-Sport
driver = webdriver.Chrome()
vars = {}
driver.get("http://mensapparel.great-site.net/login.php")
driver.set_window_size(1536, 816)
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "password").click()
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "login_user").click()
driver.find_element(By.CSS_SELECTOR, ".active .btn").click()
driver.find_element(By.CSS_SELECTOR, ".container-fluid h1").click()
#driver.find_element(By.CSS_SELECTOR, ".container-fluid h1").text == "Sports For Men"
get_text=driver.find_element(By.CSS_SELECTOR, ".container-fluid h1").text
if get_text=="Sports For Men":
    t1=t1+"\nCarosel Button is Working"
    pc=pc+1
    stat="Pass"
else:
    t1=t1+"\nCarosel Button not Working :("
    pf=pf+1
    stat="Fail"
driver.close() 

#add to cart
driver = webdriver.Chrome()
driver.get("http://dummymensapparel.great-site.net/itemcategory.php?catid=1")
driver.set_window_size(1552, 832)
#driver.find_element(By.CSS_SELECTOR, ".catg:nth-child(3) img").click()
driver.find_element(By.CSS_SELECTOR, ".brands:nth-child(6) img").click()
driver.find_element(By.LINK_TEXT, "Add To Bag").click()
driver.find_element(By.CSS_SELECTOR, "h4").click()

get_text=driver.find_element(By.CSS_SELECTOR, "h4").text
if get_text=="Items in Cart: 4":
    t1=t1+"\nItem added to cart Succesfully!!"
    pc=pc+1
    stat="Pass"
else:
    t1=t1+"\nAdd to Cart Unsuccesfull :("
    pf=pf+1
    stat="Fail"
driver.close() 

#cart count
driver = webdriver.Chrome()
driver.get("http://dummymensapparel.great-site.net/index.php")
driver.find_element(By.CSS_SELECTOR, ".navbar:nth-child(15) #shopcart").click()
driver.find_element(By.CSS_SELECTOR, "h4").click()
#assert driver.find_element(By.CSS_SELECTOR, "h4").text == "Items in Cart: 4"
get_text=driver.find_element(By.CSS_SELECTOR, "h4").text
if get_text=="Items in Cart: 5":
    t1=t1+"\nCart item count Verified!"
    pc=pc+1
    stat="Pass"
else:
    t1=t1+"\nCart item count do not match :("
    pf=pf+1
    stat="Fail"
driver.close()


#item filter
driver = webdriver.Chrome()
driver.get("http://dummymensapparel.great-site.net/itemcategory.php?catid=1")
driver.set_window_size(1552, 832)
driver.find_element(By.ID, "casual").click()
driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
driver.find_element(By.CSS_SELECTOR, "h3:nth-child(2)").click()
get_text=driver.find_element(By.CSS_SELECTOR, "h3:nth-child(2)").text
if get_text=="Items Count: 3":
    t1=t1+"\nOccasions Filter Working"
    pc=pc+1
    stat="Pass"
else:
    t1=t1+"\nFilter option not Working :("
    pf=pf+1
    stat="Fail"
driver.close() 


#logout
driver = webdriver.Chrome()
vars = {}
driver.get("http://mensapparel.great-site.net/login.php")
driver.set_window_size(1536, 816)
driver.find_element(By.NAME, "email").click()
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "password").click()
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "login_user").click()
driver.find_element(By.XPATH, "/html/body/nav[2]/div/a[1]").click()
title = driver.title
if title=="E-Com Login":
    t1=t1+"\nLogOut Succesfull"
    pc=pc+1
    stat="Pass"
else:
    t1=t1+"\nLogOut Unsuccesfull :("
    pf=pf+1
    stat="Fail"
driver.close() 





ts=datetime.datetime.now()
date_time=ts.strftime("%d-%m-%Y, %H:%M:%S")
f = open("file2.txt", "a")
f.write("\n\nTest Suite:")
f.write("\n"+date_time+"   Run 1:"+"\t"+t1+"  Number of Test case Passed"+str(pc)+"  Number of test case failed"+str(pf))
f.close()

#Enter data to database
db = mongo_db.TestLogs
coll = db.TestColl
cursor = coll.find({"TestSuiteName": "All Test Cases"}).sort('TSid', -1).limit(1)[0]
print(cursor)
data=dict()

data["TSid"]=int(cursor["TSid"]) + 1
data["TestSuiteName"]="All Test Cases"
data["time"]=datetime.datetime.now()
data["Output"]=t1
data["pc"]=pc
data["pf"]=pf
x=coll.insert_one(data)