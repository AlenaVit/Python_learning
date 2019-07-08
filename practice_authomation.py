from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://app-rc.ripl.com/login")
driver.implicitly_wait(20)
assert "Ripl" in driver.title
elem = driver.find_element_by_id("log-in-email")
elem.clear()
elem.send_keys("new6/14@ripl.com")
elem2 = driver.find_element_by_id("log-in-pwd")
elem2.send_keys("zxcv123")
elem.send_keys(Keys.RETURN)

elem3 = driver.find_element_by_css_selector(".plus")
elem3.click()


# another_des = driver.find_element_by_css_selector(".designList .designContainer:nth-of-type(3) .clickTarget")
# another_des.click()

txt = driver.find_element_by_id("primary")
txt.clear()
txt.send_keys("test_text")

music_menu = driver.find_element_by_css_selector(".designControls .controlBlock:nth-of-type(7)")
music_menu.click()

msc_track = driver.find_element_by_css_selector(".list .item:nth-of-type(3)")
msc_track.click()

next_page = driver.find_element_by_css_selector(".header .clickable:nth-child(3) .material-icons")
next_page.click()

time.sleep(1)
next_button = driver.find_element_by_css_selector(".md-dialog-footer--inline [type='button']:nth-of-type(2)")
next_button.click()

time.sleep(20)
ln_toggle = driver.find_element_by_css_selector("[for='LinkedIn-5844691'] [tabindex]")
ln_toggle.click()

twit_toggle = driver.find_element_by_css_selector("[for='Twitter-5844627'] div:nth-child(2)")
twit_toggle.click()


share_btn = driver.find_element_by_css_selector("[class='md-cell md-cell--12 md-cell--8-tablet']:nth-of-type(2) [type]")
share_btn.click()

# driver.close()