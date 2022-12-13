from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
num = driver.find_element_by_id("money")
timeout = time.time() + 2*1
five_min = time.time() + 300

while True:
    cookie.click()

    if time.time() > timeout:
        time_machine = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[8]/b")
        portal = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[7]/b")
        alchemy_lab = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[6]/b")
        shipment = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[6]/b")
        mine = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[4]/b")
        factory = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[3]/b")
        grandma = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[2]/b")
        cursor = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[1]/b")

        if int(num.text) >= 123456789:
            time_machine.click()

        elif int(num.text) >= 1000000:
            portal.click()

        elif int(num.text) >= 50000:
            alchemy_lab.click()

        elif int(num.text) >= 7000:
            shipment.click()

        elif int(num.text) >= 2000:
            mine.click()

        elif int(num.text) >= 500:
            factory.click()

        elif int(num.text) >= 100:
            grandma.click()

        else:
            cursor.click()

        timeout = time.time() + 2

    if time.time() >= five_min:
        print(driver.find_element_by_id("cps").text)
        driver.quit()


