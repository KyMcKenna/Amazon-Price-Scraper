import requests
from bs4 import BeautifulSoup
import smtplib
import time

# item URL we're scraping
URL = 'https://www.amazon.com/SAMSUNG-49-inch-Odyssey-FreeSync-LC49G95TSSNXZA/dp/B088HH6LW5/ref=sr_1_3?dchild=1&keywords=49%22+monitor&qid=1612327879&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

def check_price(): 
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
# adjust second integer based on product cost
    converted_price = float(price[0:5])

    if(converted_price < 1.300):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 1.300):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
# gmail login, insert send email login here
    server.login('EMAILHERE@gmail.com', 'PASSWORDHERE')

    subject = 'The price for your item went down! Buy it now!'
    body = 'check the amazon link: https://www.amazon.com/SAMSUNG-49-inch-Odyssey-FreeSync-LC49G95TSSNXZA/dp/B088HH6LW5/ref=sr_1_3?dchild=1&keywords=49%22+monitor&qid=1612327879&sr=8-3'

    msg = f"Subject:{subject}\n\n{body}"

# sending and receiving emails
    server.sendmail(
        'FROM-EMAIL@gmail.com',
        'TO-EMAIl@gmail.com',
        msg
    )
    print('email sent')

    server.quit()

# how often the scraper checks, in seconds
while(True):
    check_price()
    time.sleep(86400)