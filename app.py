from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.implicitly_wait(60*60)
driver.get("https://web.whatsapp.com/")
assert "WhatsApp" in driver.title


def decorate():
    print("\n"*10)
    print("*"*50)
    # input("Scan QR 10s")
    print("Please Scan QR to continue")
    print("*"*50)
    print("\n"*2)


# driver.implicitly_wait(0)
decorate()

botContact = ["None", "Theophilus"]
botContact = [x.lower() for x in botContact]
botActive = True


def Msg():
    lastMsgIn = driver.find_element_by_xpath('//div[contains(@class, "_1RAno message-in")][last()]//span[@dir="ltr"]/span')
    lastMsg = driver.find_element_by_xpath('//div[contains(@class, "_1RAno message")][last()]//span[@dir="ltr"]/span')

    if lastMsg == lastMsgIn:
        inputField = driver.find_element_by_xpath("//footer//div[contains(@class, 'copyable-text')]")
        inputField.clear()

        command = lastMsgIn.text.lower().split(" ")
        if command[0] == "aris,,":

            if command[1] == "add":
                botContact.append(command[2])
                inputField.send_keys("done", Keys.RETURN)

            elif command[1] == "remove":
                print("remove")
                botContact.remove(command[2])
                inputField.send_keys("done", Keys.RETURN)

            elif command[1] == "list":
                inputField.send_keys("\n".join(botContact), Keys.RETURN)

            elif command[1] == "pause":
                print("pause")
                botActive = False
                inputField.send_keys("done", Keys.RETURN)

            elif command[1] == "start":
                print("start")
                botActive = True
                inputField.send_keys("done", Keys.RETURN)

            elif command[1] == "stop":
                inputField.send_keys("done", Keys.RETURN)
                driver.close()
            
            else:
                inputField.send_keys("unknown command", Keys.RETURN)

        else:
            inputField.send_keys(f"You typed: {lastMsgIn.text}", Keys.RETURN)


def BotAction():
    try:
        unreadContact = driver.find_elements_by_xpath('//span[contains(@class, "VOr2j")]/ancestor::div[contains(@class, "_1MZWu")]')
        unreadContact = unreadContact[0]
        unreadContactName = unreadContact.text.split("\n")[0]

        if unreadContactName.lower() in botContact:
            unreadContact.click()
            Msg()
    except:
        pass
    # except Exception as ex:
        # print(f"{ex}- no new message on contact list")

    try:
        activeContactName = driver.find_element_by_xpath('//header[@class="_1UuMR"]//span[contains(@dir, "auto")][contains(@title, "")]')
        if activeContactName.text.lower() in botContact:
            Msg()
    except:
        pass


while True:
    if botActive:
        BotAction()
    time.sleep(1)
