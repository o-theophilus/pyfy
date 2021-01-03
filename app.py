from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
assert "WhatsApp" in driver.title


print("\n"*10)
input("Scan QR and press any key to console")

person = driver.find_element_by_xpath("span.VOr2j")
person.click()



inputField = driver.find_element_by_xpath("//div[text()='Type a message']/..")
# inputfield = driver.find_element_by_xpath("//*[text()='Type a message']/../div[@class='_1awRl']")
inputfield.click()
inputfield.
# inputfield.clear()
inputfield.send_keys("pycon", Keys.RETURN)

# assert "No results found." not in driver.page_source


chatArea = driver.find_element_by_xpath("//div[@aria-label='Message list. Press right arrow key on a message to open message context menu.']")
received = chatArea.find_element_by_class_name('message-in')




# driver.close()