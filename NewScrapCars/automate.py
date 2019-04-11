from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from urllib.request import urlopen
import urllib
#Getting the zipcodes
with open('urls.txt') as f:
    comp = list(f.readlines())
comp = [i.strip('\n') for i in comp] 

#The internet Checker
def wait_for_internet_connection():
    while True:
        try:
            urlopen('https://www.google.com',timeout=1000)
            return
        except urllib.error.URLError:
            pass

# url = 'https://www.toyota.com/dealers/#search&zipcode='
# urls = []
# for i in comp:
#     new = url+i
#     urls.append(new)
# with open('your_file.txt', 'w') as f:
#     for item in urls:
#         f.write("%s\n" % item)
    

driver = webdriver.Chrome(executable_path='/home/azer/Desktop/LinkedInParser/chromedriver')

for item in comp:
    wait_for_internet_connection()
    driver.get(item)

    try:
    # IF more button exists click on more
        driver.find_element_by_xpath('//button[@id="dlm-search-list-more-button"]').click()
    except:
        pass
    # Getting Data

    # Data Count
    try:
        x = driver.find_elements_by_xpath('//div[@id="dlm-search-list"]/div')
        length = len(x)

        for i in range(1,length+1):
            name = driver.find_element_by_xpath('//div[@id="dlm-search-list"]/div[{}]//h2'.format(i)).text
            address = driver.find_element_by_xpath('//div[@id="dlm-search-list"]/div[{}]//span[@class="dealer-address"]'.format(i)).text
            phone = driver.find_element_by_xpath('//div[@id="dlm-search-list"]/div[{}]//div[@class="col-lg-4 col-sm-6 col-xs-12"][2]//span[@class="search-result-value"]'.format(i)).text
            state = address.split(' ')[-2]
            country = 'USA'

            with open('infod.csv', 'a+',encoding='utf-8') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow([name,address,phone,state,country])
    except:
        pass

