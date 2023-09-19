import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Microsoft Edge driver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

# 1  Launch of the application URL(https://www.bt.com/)

driver.get("https://www.bt.com/")

# 2. Close accept Cookie pop-up if it appears

try:
    PopUpFrame = 'trustarc_cm'
    driver.switch_to.frame(PopUpFrame)
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='call']"))
    )
    # Find and click the "Accept All Cookies" button (adjust the selector as needed)
    accept_button = driver.find_element(By.XPATH, "//*[@class='call']")
    accept_button.click()
    driver.switch_to.default_content()

except Exception as e:
    print("Cookie pop-up did not appear or could not be handled:", e)

# 3.  Hover to Mobile menu

MobileButton = driver.find_element(By.XPATH, "(//span[contains(text(),'Mobile')])[1]")

hover = ActionChains(driver).move_to_element(MobileButton)
hover.perform()

# 4.      From mobile menu, select Mobile phones

MobilePhoneButton = '(//a[@href="https://www.bt.com/products/mobile/phones/"])[1]'

MobilePhones = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, MobilePhoneButton))
)
time.sleep(5)
driver.find_element(By.XPATH, MobilePhoneButton).click()

# 6. Scroll down and click View SIM only deals
simOnlyDealsXpath = "//a[@data-di-id='di-id-f6103190-3a42ff4a']"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, simOnlyDealsXpath))
)

simOnlyDeals = driver.find_element(By.XPATH, value=simOnlyDealsXpath)
simOnlyDeals.click()
pageTitle = driver.title
ExpectedTitle = 'SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile'
print(f"Page Title  : {pageTitle}")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@data-di-id='di-id-3a4dd8f0-1fee3db1']"))
)

selectGB = driver.find_element(By.XPATH, value="//*[@data-di-id='di-id-3a4dd8f0-1fee3db1']")
selectGB.click()
# Close the browser
driver.close()
