from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import login

chrome_driver_path = "/home/irem/Downloads/chromedriver_linux64/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver_path)

browser.get("https://twitter.com/")
time.sleep(2)
logintw=browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
logintw.click()
time.sleep(2)
username=browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username.send_keys(login.username)
next = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
next.click()
time.sleep(5)
password = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(login.password)
loginbutton =browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
loginbutton.click()
time.sleep(3)
searchtw = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
searchtw.click()
searchtw.send_keys("#helloworld!")
searchtw.submit()
time.sleep(5)
browser.close()