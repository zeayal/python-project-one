from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

EXTENSION_PATH = "./assets/metamask-chrome-10.27.0.crx";

options = webdriver.ChromeOptions()
options.add_extension(EXTENSION_PATH);
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
# options.add_argument('--start-maximized')  # 浏览器窗口最大化
driver = webdriver.Chrome(options=options)

def run_webbrowser():
    driver.get('https://www.baidu.com')
    search_input = WebDriverWait(driver, 5).until(lambda d: d.find_element(By.ID, "kw"))
    search_input.send_keys("react")
    search_input.send_keys(Keys.RETURN)


run_webbrowser()
