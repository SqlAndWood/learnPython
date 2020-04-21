# Install two packages with the following command line:
# pip install requests 
# pip install bs4 

import requests
from bs4 import BeautifulSoup 

import smtplib

URL = 'https://www.amazon.com.au/gp/product/B07W95HD3M/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=AMMK0LS9EDNM8&pf_rd_s=merchandised-search-3&pf_rd_r=YGF8KDMXGHB35WRC2ZFW&pf_rd_t=101&pf_rd_p=5ae35cf7-3053-4de1-a33d-b25d2b462546&pf_rd_i=6946656051'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
        
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price  = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:5])

    print(title.strip())
    print(converted_price)

    if(converted_price < 80.0):
       send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
        #jkffruzlbmocdhfa
    server.login('drooten@gmail.com','jkffruzlbmocdhfa' )
    
    subject = "Price is down"
    body = 'Check amazon link:  https://www.amazon.com.au/gp/product/B07W95HD3M/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=AMMK0LS9EDNM8&pf_rd_s=merchandised-search-3&pf_rd_r=YGF8KDMXGHB35WRC2ZFW&pf_rd_t=101&pf_rd_p=5ae35cf7-3053-4de1-a33d-b25d2b462546&pf_rd_i=6946656051'

    msg = f"Subject:{subject}/n/n/{body}"
    
    server.sendmail(
        'drooten@gmail.com',
        'awoody@protonmail.com',
        msg
    
    )
    print ('send email')
    
    
    server.quit
    
    
#while(true):
check_price()
    #time.sleep(60 * 60 )