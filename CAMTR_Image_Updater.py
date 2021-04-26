from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import os
import pandas as pd
import os
import requests
import pathlib
import shutil

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

            # Load the Pandas libraries with alias 'pd'


            # Read data from file 'filename.csv'
            # (in the same directory that your python process is based)
            # Control delimiters, rows, column names with read_csv (see later)
            data = pd.read_csv("images.csv")
            currentPatg = pathlib.Path().absolute()
            print(currentPatg)
            # Preview the first 5 lines of the loaded data
            data.head()

            for i, j in data.iterrows():
                z = 1
                otay = j[0].replace("-"," ")
                shutil.rmtree(otay, ignore_errors=True)
                os.mkdir(otay)
                for o in j:
                    try:
                        if (str(j[z])[-1] == "g"):
                            # print(j[0])
                            # print(j[z])
                            # print(str(j[z])[-4:])
                            img_data = requests.get(j[z]).content
                            if str(j[z])[-2:] == "eg":
                                with open('C:\\Users\\Asher\\Desktop\GrandScan\\ImageMaster\\'+otay+'\\'+'bitcoin-atm-near-me-'+j[0]+'-'+str(z)+j[z][-5:], 'wb') as handler:
                                    print('C:\\Users\\Asher\\Desktop\GrandScan\\ImageMaster\\'+otay+'\\'+'bitcoin-atm-near-me-'+j[0]+'-'+str(z)+j[z][-5:])
                                    handler.write(img_data)
                            else:
                                with open('C:\\Users\\Asher\\Desktop\GrandScan\\ImageMaster\\'+otay+'\\'+'bitcoin-atm-near-me-'+j[0]+'-'+str(z)+j[z][-4:], 'wb') as handler:
                                    print('C:\\Users\\Asher\\Desktop\GrandScan\\ImageMaster\\'+otay+'\\'+'bitcoin-atm-near-me-'+j[0]+'-'+str(z)+j[z][-4:])
                                    handler.write(img_data)
                        z += 1
                    except Exception as e:
                        print(str(e))
                        break
            # C:\Users\Asher\Desktop\GrandScan\ImageMaster
            # C:\Users\Asher\Desktop\GrandScan\ImageMaster\bitcoin-atm-near-me-20424-Kuykendahl-Rd-Spring-TX-77379
