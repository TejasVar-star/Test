from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\tvarkhede\\Desktop\\Tejas\\Python\\Chrome\\chromedriver.exe")
driver.get("https:www.phptravels.net/home")
driver.maximize_window()
print(driver.title)
driver.find_element_by_css_selector("a[href='#flights']").click()
driver.find_element_by_xpath("//input[@type='radio']/following-sibling::*[contains(., 'Round')]").click()

for dropdown in (driver.find_elements_by_xpath("//div[contains(@class,'chosen-with-drop')]")):
   print(dropdown)
dropdown.find_element_by_xpath("a/span[text()='Business']").click()
fromplace = driver.find_element_by_css_selector("div#select2-drop")
fromplace.click()
fromplace.send_keys("del")

driver.find_element_by_css_selector("div#s2id_location_to").click()
driver.find_element_by_css_selector("input#FlightsDateStart").click()

driver.quit()