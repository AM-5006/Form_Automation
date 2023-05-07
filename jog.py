from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

# opt = Options()
# opt.add_argument("--headless")

with open("seat.txt", 'r') as f:
    s = f.readlines()
    
s = [int(i.strip('\n')) for i in s]

url = "https://results.gbshsegoa.net/#/home"

for i in s:
    driver = webdriver.Chrome()
    driver.get(url)

    link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'HSSC RESULTS')]")))
    link.click()
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "seat")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "scode")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cdtbt")))
        
        seat_no = driver.find_element(By.ID,"seat")
        seat_no.send_keys(str(i))

        seat_no = driver.find_element(By.ID,"scode")
        seat_no.send_keys("HS010")

        seat_no = driver.find_element(By.ID,"cdtbt")
        seat_no.send_keys("08/08")
        # time.sleep(30)       #captcha time
    except Exception as e:
        print(i)
    finally:
        alert = None
        wait = WebDriverWait(driver, 10000)
        alert = wait.until(EC.alert_is_present())
        if alert is None:
            time.sleep(600)
        else:
            print(i)
            alert.accept()
            with open ("done.txt", 'a') as f:
                f.write(str(i)+"\n")
        driver.quit()

