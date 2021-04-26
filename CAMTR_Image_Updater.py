from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import os

#This program navigates www.coinatmradar.com in order to apply images to their respective business listing
#This task was normally done by hand, but this program does the whole job in a matter of minutes since no API is available for this action


f = open("links.csv","r")

myList = []

for line in f:
   myList.append(line.replace('\n', ''))

print(myList[0].replace(",",""))

web = webdriver.Chrome(r'C:\Users\Asher\Desktop\Projects\Atm Image Update\chromedriver.exe')

web.get('https://www.coinatmradar.com/')
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    web.add_cookie(cookie)

# last = web.find_element_by_xpath('//*[@id="g16-name"]')
# time.sleep(2)
# last.send_keys('brandon@bitcoindepot.com')
# last = web.find_element_by_xpath('//*[@id="g16-email"]')
# last.send_keys('BlueBottleOpener20!')
# input("Complete Captcha...")
# submit = web.find_element_by_xpath('/html/body/div[2]/div/div/form/p/input')
# submit.click()
# time.sleep(2)
z=0

while z < len(myList):
    input("Begin uploading images...")
    web.get(myList[z].replace(",",""))
    time.sleep(5)
    web.find_element_by_id("ajaxfile").send_keys(os.getcwd() + "\\1 South St West Hartford CT 06110\\bitcoin-atm-near-me-1-South-St-West-Hartford-CT-06110-3.jpg")
    print("okay..")
    time.sleep(800)


    # checkboxes = web.find_elements_by_xpath("//input[@type='checkbox']")
    # notaduplicate = web.find_elements_by_class_name("btn btn-white suppression-action js-not-a-duplicate")
    # addresses = web.find_elements_by_class_name("mw-150")
    # checkboxes.pop(0)
    # a = len(checkboxes)
    #
    #
    # for address in addresses:
    #     new_addy = address.text.split()
    # i = 0
    # for checkbox in checkboxes:
    #     time.sleep(0.05)
    #     if myList[z]=="DELETE":
    #         web.execute_script("arguments[0].click();", checkbox)
    #         i +=1
    #     z+=1


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
