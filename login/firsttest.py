from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
user = "Good girl ramya"
pwd = "kamesh is a bad boy"
driver = webdriver.Chrome("F:\RamyaProjectDonotDeleteOrTouch\chromedriver.exe");
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
