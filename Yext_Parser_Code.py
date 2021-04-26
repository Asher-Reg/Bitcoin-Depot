from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#This program logs into Yext in a chrome browser and navigates the login page
#Once logged in the program navigates to the 'duplicates' page and checks all of the potential duplicate listings within marketing platforms
#Marks duplicates for removal and leaves non-duplicates alone

f = open("dups.csv","r")

myList = []


for line in f:
   myList.append(line.replace('\n', ''))


web = webdriver.Chrome(r'C:\Users\Asher\Desktop\Crawlers\Yext Parser\chromedriver')
web.get('https://www.yext.com/s/3015064/duplicates#p0=entities&p0=brand&p0=status&p1=&p1=&p1=1&p2=contains&p2=contains&p2=contains&p3=&p3=&p3=')

last = web.find_element_by_xpath('//*[@id="username"]')
time.sleep(2)
last.send_keys('asher.reg@bitcoindepot.com')
last = web.find_element_by_xpath('//*[@id="password"]')
last.send_keys('rjwatb9Df4uar53')

submit = web.find_element_by_xpath('//*[@id="login"]/form/div[1]/button')
submit.click()
time.sleep(2)
z=0

while z < len(myList):
    input("Begin marking duplicates...")
    checkboxes = web.find_elements_by_xpath("//input[@type='checkbox']")
    notaduplicate = web.find_elements_by_class_name("btn btn-white suppression-action js-not-a-duplicate")
    addresses = web.find_elements_by_class_name("mw-150")
    checkboxes.pop(0)
    a = len(checkboxes)


    for address in addresses:
        new_addy = address.text.split()
    i = 0
    for checkbox in checkboxes:
        time.sleep(0.05)
        if myList[z]=="DELETE":
            web.execute_script("arguments[0].click();", checkbox)
            i +=1
        z+=1


    input("Begin marking non-duplicates...")
    checkboxes = web.find_elements_by_xpath("//input[@type='checkbox']")
    checkboxes.pop(0)
    print(a)
    print(i)
    p = a - i
    print(p)
    for checkbox in checkboxes:
        if p > 0:
            time.sleep(0.05)
            web.execute_script("arguments[0].click();", checkbox)
            p-= 1
