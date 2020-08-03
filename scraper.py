import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = r"https://www.flipkart.com/msi-alpha-15-ryzen-7-quad-core-16-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-amd-radeon-rx-5500m-a3dd-044in-gaming-laptop/p/itmad579b1018881?pid=COMFHV33GHHRANTN&lid=LSTCOMFHV33GHHRANTNXR5NSM&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&fm=SEARCH&iid=d0405136-03bc-4b02-9e08-bede1da49c07.COMFHV33GHHRANTN.SEARCH&ppt=sp&ppn=sp&ssid=aakqt5ionk0000001596452327572&qH=2828ce900bf8fdb6"

headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

sender_email = ##########################
sender_password = #######################

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    price = soup.find(class_ = '_1vC4OE _3qQ9m1').get_text()
    converted_price = float(price[1:].replace(",", ""))

    print(converted_price)

    if (converted_price < 65000): 
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, sender_password)

    subject = r"Price Fell Down!"

    body = r"Here's the link to this mouthwatering deal: https://www.flipkart.com/msi-alpha-15-ryzen-7-quad-core-16-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-amd-radeon-rx-5500m-a3dd-044in-gaming-laptop/p/itmad579b1018881?pid=COMFHV33GHHRANTN&lid=LSTCOMFHV33GHHRANTNXR5NSM&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_8_na_na_na&fm=SEARCH&iid=d0405136-03bc-4b02-9e08-bede1da49c07.COMFHV33GHHRANTN.SEARCH&ppt=sp&ppn=sp&ssid=aakqt5ionk0000001596452327572&qH=2828ce900bf8fdb6"

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email, "markdsouza434@gmail.com", message)
    print("Message has been sent!!!")

    server.quit()

while True:
    check_price()
    time.sleep(60 * 60 * 6)
