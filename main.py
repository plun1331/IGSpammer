from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from configparser import ConfigParser
parser = ConfigParser()

person = input("Who shall you spam?\n")
msg = input("What shall you spam?\n")

print("Locating Driver and FireFox excecutable.")
try:
	parser.read('files.ini')
	driver = parser.get('CONFIG', 'driver')
	binary = parser.get('CONFIG', 'firefox')
except:
	print("Couldn't find Driver/FireFox in the files.ini configuration file. The process has been aborted.")
	quit()

options = Options()
options.binary = binary

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
print("Launching browser...")
try:
	browser = webdriver.Firefox(options=options, capabilities=cap, executable_path=driver)
except:
	print("Invalid Driver/FireFox executable provided in files.ini. The process has been aborted.")
	quit()

print("Reading credentials...")
try:
	parser.read('config.ini')
	user = parser.get('CONFIG', 'user')
	pw = parser.get('CONFIG', 'pw')
except:
	print("Couldn't find credentials. Please make sure you have both your username and password in the config.ini configuration file. The process has been aborted.")
	quit()

print("Going to website...")
browser.get('https://www.instagram.com/')

s = False
for i in range(0, 5):
	try:
		print("Finding credential fields...")
		username_input = browser.find_element_by_css_selector("input[name='username']")
		password_input = browser.find_element_by_css_selector("input[name='password']")
		print("Inputting credentials...")
		username_input.send_keys(user)
		password_input.send_keys(pw)
		print("Finding login button...")
		login_button = browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()
		s = True
		print("Logging in...")
		break
	except:
		sleep(1)
if not s:
	print("Something went wrong. The process has been aborted.")
	browser.close()
	quit()

print("Validating login...")
logininvalid = None
pwinvalid = None
for i in range(0, 5):
	try:
		logininvalid = browser.find_element_by_xpath("//p[@id='slfErrorAlert']")
		break
	except:
		sleep(1)
if logininvalid is not None:
	print("The username or password provided is invalid. The process has been aborted.")
	browser.close()
	quit()

s = False
for i in range(0, 5):
	try:
		print("""Locating "Don't save credentials," button...""")
		dontsave = browser.find_element_by_xpath("//button[text()='Not Now']")
		dontsave.click()
		s = True
		print("Not saving credentials...")
		break
	except:
		sleep(1)
if not s:
	print("Something went wrong. The process has been aborted.")
	browser.close()
	quit()

s = False
for i in range(0, 5):
	try:
		print("Attempting to disable notifications...")
		notifs_off = browser.find_element_by_xpath("//button[text()='Not Now']")
		notifs_off.click()
		s = True
		print("Disabling notifications...")
		break
	except:
		sleep(1)
if not s:
	print("Something went wrong. The process has been aborted.")
	browser.close()
	quit()

s = False
for i in range(0, 5):
	try:
		print(f"Attempting to navigate to DMs...")
		dms = browser.find_element_by_xpath("//a[@href='/direct/inbox/']")
		dms.click()
		s = True
		print("Navigating to DMs...")
		break
	except:
		sleep(1)
if not s:
	print("Something went wrong. The process has been aborted.")
	browser.close()
	quit()

s = False
for i in range(0, 5):
	try:
		print(f"Attempting to find {person}'s DM...")
		group = browser.find_element_by_xpath(f"//div[text()='{person}']")
		group.click()
		s = True
		print(f"Navigating to {person}'s DM...")
		break
	except:
		sleep(1)
if not s:
	print(f"Couldn't find {person}'s DM. The process has been aborted.")
	browser.close()
	quit()

print("Spamming...")
while True:
	s = False
	for i in range(0, 5):
		try:
			msgbox = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
			msgbox.send_keys(msg)
			s = True
			break
		except:
			sleep(1)
	if not s:
		print("Something went wrong. The process has been aborted.")
		browser.close()
		quit()

	s = False
	for i in range(0, 5):
		try:
			send = browser.find_element_by_xpath("//button[text()='Send']")
			send.click()
			s = True
			break
		except:
			sleep(1)
	if not s:
		print("Something went wrong. The process has been aborted.")
		browser.close()
		quit()