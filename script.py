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
import urllib.request


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
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/div[1]/a/span[2]')))

            img_src = driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img").get_attribute('src')
            urllib.request.urlretrieve(img_src, f"{str(img_src).split('=')[1]}.jpg")
        except Exception:
            print("Error ...")
    
    print('image downloaded')
    print('Closing script')
    driver.close()

direct_link = input('Enter the direct link of the yandex image')
# direct_link = "https://yandex.ru/images/search?text=Surrealism&rlt_url=https%3A%2F%2Fink-project.ru%2Fsites%2F1-ink-project%2Fphotoalbums%2F8303.jpg&ogl_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FDgceTL3WAAA_UTZ.jpg&pos=3&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FDgceTL3WAAA_UTZ.jpg&rpt=simage"
download_yandex_image(direct_link)