from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl
import pyautogui
import parsegeo as pg
import re


def detailulasan(resto,link,limit,output):
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH) 
    driver.get(link)

    time.sleep(2)
    try:
        banyakreview = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span')
        banyakreview = int(banyakreview.text[1:-1])
        if(banyakreview >= limit):
            scrolltime = banyakreview/10
            if scrolltime > 90.0:
                scrolltime = 90

            reviewbut = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]')
            reviewbut.click()
            time.sleep(2)           
            urutkan = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[7]/div[2]/button/span')
            urutkan.click()
            time.sleep(1) 
            terbaru =driver.find_element(By.XPATH, '//*[@id="action-menu"]/div[2]')
            terbaru.click()
            time.sleep(1) 
            geo = driver.current_url
            geo = pg.parsegeo(geo)
            

            pyautogui.moveTo(383, 442)
            t_end = time.time() +  scrolltime 
            while time.time() < t_end:
                time.sleep(0.1)
                pyautogui.scroll(-3000)
            read_more_elements = driver.find_elements(By.XPATH, '//*[@class="w8nwRe kyuRq"]')
            for element in read_more_elements:
                time.sleep(0.1)
                element.click()
            review = driver.find_elements(By.XPATH,'//*[@class="MyEned"]/span[1]')
            waktu = driver.find_elements(By.XPATH,'//*[@class="rsqaWe"]')
            data = []

            for i,j in zip(review,waktu):
                if i.text == "":
                    continue
                txt = i.text
                txt = re.sub(r"(\r\n|\r|\n)", " ", txt)
                data.append([txt,j.text,resto,geo])
            
            pd.DataFrame(data).to_csv(output,mode="a",index=False, header=False)
        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()