#another useless program that can be used to spam a whatsapap user with messages!
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
path = "/Users/User/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(10)
name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
