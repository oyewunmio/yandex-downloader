# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

pathname = input('Enter the name of the folder to store the downloaded images to\t')

#web driver configuration
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.headless = False
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
ua = UserAgent(use_cache_server=False)

#file managing configuration
if not os.path.isdir(pathname):
    os.makedirs(pathname)
    prefs = {"profile.managed_default_content_settings.images": 2, 'download.default_directory' : os.path.join(os.getcwd(), pathname)}
    chrome_options.add_experimental_option("prefs", prefs)
else:
    prefs = {"profile.managed_default_content_settings.images": 2, 'download.default_directory' : os.path.join(os.getcwd(), pathname)}

userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def download_yandex_image(url):
    if 'yandex' not in url:
        print('Url not yandex related ')
        quit
    else:
        driver.get(url)
        timeout = 10

        try:
            element_present = EC.presence_of_element_located(By.XPATH, "/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/div[1]/a")
            WebDriverWait(driver, timeout).until(element_present)

            download_button = driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/div[1]/a")
            download_button.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Timed out waiting for page to load..check your network connectivty")
        
        wait = True
    while(wait == True):
        for fname in os.listdir(os.path.join(os.getcwd(), pathname)):
            if ('Unconfirmed') in fname:
                print('downloading files ...')
                sleep(10)
            else:
                wait=False
        
    print('finished downloading file ...')

    print('Closing script')
    driver.close()

direct_link = input('Enter the direct link of the yandex image')
download_yandex_image(direct_link)