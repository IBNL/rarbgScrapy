from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from Screenshot import Screenshot_Clipping
import time
from PIL import Image
from io import BytesIO
import pytesseract
import pickle
from selenium.webdriver.firefox.options import Options

url = "https://rarbgprx.org/torrents.php?category=movies"
option = Options()
option.headless = True 
#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()
driver.get(url)
#wait button to click
time.sleep(10)
driver.find_element_by_link_text("Click here").click()
#wait load captcha
time.sleep(10)
imgCaptcha = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/img[1]")
png = driver.get_screenshot_as_png() # saves screenshot of entire page
#get position of captcha
location = imgCaptcha.location
size = imgCaptcha.size
#print(location)
#print(size)
im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
im = im.crop((left, top, right, bottom)) # defines c
im.save('captcha.png') # saves new cropped image
#solving captcha with OCR
captachResolv = pytesseract.image_to_string( Image.open('captcha.png') )  # Extract string to img
#print(captachResolv)

driver.find_element_by_name( 'solve_string' ).send_keys(captachResolv)

submit_button = driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/button[1]')[0]
submit_button.click()
#time.sleep(5)
#get cookies
pickle.dump(driver.get_cookies(), open("cookies.txt","wb"))
print("save cookies")
arqCookies=open('cookies.txt')
print("format cookie.txt")
lines = arqCookies.readlines()
domain1 = "rarbgprx.org"
domain2 = ".rarbgprx.org"
timeCreate = lines[92][1:].rstrip('\n')
name = lines[59][1:].rstrip('\n')
value = lines[63][1:].rstrip('\n')
timeStart = lines[188][1:].rstrip('\n')
lastAcess = lines[67][1:].rstrip('\n')
timeFinish = lines[16][1:].rstrip('\n')
valueFinish = lines[12][1:].rstrip('\n')
expla = lines[117][1:].rstrip('\n')
expla3 = lines[163][1:].rstrip('\n')
linha0 = "# Netscape HTTP Cookie File"
linha1 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + timeFinish + "\t" + "skt" + "\t" + valueFinish
linha2 = domain2 + "\t" + "TRUE" + "\t" + "/" + "\t" + "FALSE" + "\t" + timeFinish + "\t" + "skt" + "\t" + valueFinish
linha3 = domain2 + "\t" + "TRUE" + "\t" + "/" + "\t" + "FALSE" + "\t" + lastAcess + "\t" + name + "\t" + value
linha4 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + "0" + "\t" +"\t" + "tcc"
linha5 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + timeCreate + "\t" + name + "\t" + value
linha6 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + expla + "\t" + "expla" + "\t" + "2"
linha7 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + expla3 + "\t" + "expla3" + "\t" + "1"
linha8 = domain1 + "\t" + "FALSE" + "\t" + "/" + "\t" + "FALSE" + "\t" + timeStart + "\t"  + "aby" + "\t" + '2'
arquivo = open('formatCookie.txt', 'w')
arquivo.writelines(linha0+"\n"+linha1+"\n"+linha2+"\n"+linha3+"\n"+linha4+"\n"+linha5+"\n"+linha6+"\n"+linha7+"\n"+linha8+"\n")   
arquivo.close()
print("finish")
