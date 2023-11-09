import os 
import time 
import sys
import whois
import instaloader
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm, trange
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

bot = instaloader.Instaloader()

class x:
    @staticmethod
    def write(text):
        for Y in text:
            time.sleep(0.02)
            sys.stdout.write(Y)
            sys.stdout.flush()

class extra:
    @staticmethod
    def write(text):
        for Y in  text:
            time.sleep(0.08)
            sys.stdout.write(Y)
            sys.stdout.flush()

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def loading():
    with tqdm(total=100) as loading:
        for i in range(10):
            time.sleep(0.3)
            loading.update(10)

def phone():
    number = input(f"{G}[ ! ] Enter phone number you want to trace: ")
    parsed_number = phonenumbers.parse(number, None)
    country = geocoder.description_for_number(parsed_number, "en")
    location = geocoder.description_for_valid_number(parsed_number, "en")
    carrier_name = carrier.name_for_number(parsed_number, 'en')
    timezones = timezone.time_zones_for_number(parsed_number)
    validity = phonenumbers.is_valid_number(parsed_number) 
    possible = phonenumbers.is_possible_number(parsed_number) 
    national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    normalized_number = phonenumbers.normalize_digits_only(number)
    country_code = parsed_number.country_code
    region_code = phonenumbers.region_code_for_country_code(country_code)
    line_type = carrier.number_type(parsed_number)
    valid_length = phonenumbers.is_possible_number(parsed_number)    
    extra.write(f"{G}[ | ] Getting info...\n")
    print("")
    print(f"{R}[ X ] Country: {country}")
    print(f"{R}[ X ] Location: {location}")
    print(f"{R}[ X ] Carrier: {carrier_name}")
    print(f"{R}[ X ] Timezones: {', '.join(timezones)}")
    print(f"{R}[ X ] Validity: {validity}")
    print(f"{R}[ X ] Possible: {possible}")
    print(f"{R}[ X ] National Format: {national_format}")
    print(f"{R}[ X ] International Format: {international_format}")
    print(f"{R}[ X ] Normalized Number: {normalized_number}")
    print(f"{R}[ X ] Country Code: {country_code}")
    print(f"{R}[ X ] Region Code: {region_code}")
    print(f"{R}[ X ] Line Type: {line_type}")
    print(f"{R}[ X ] Valid Length: {valid_length}")
    print("")
    
def domain():
    try:
       domain = input(f"{G}[ ! ] Enter your domain to lookup: ")
       w = whois.whois(domain)
       w.text
       print(f"{R}[ X ] {w}")

    except Exception as e:
        print("Unable to get domain info please try again later")

def webcrawl():
    try:
       website = input(f"{G}[ ! ] Enter website you want to crawl: ")
       soup = BeautifulSoup(website, 'html.parser')
       links = [link.get('href') for link in soup.find_all('a')]
       for link in links:
           print(links)

    except Exception as e:
        print("Unable to crawl please try agian later"+e)

def ip():
   ip_address = input(f"{G}[ ! ] Enter the ip you want to lookup: ")
   response = requests.get(f"https://ipinfo.io/{ip_address}/json")
   data = response.json()
   extra.write(f"{G}[ | ] Getting info ...\n")
   print(f"{R}[ X ] IP Address: " + data.get("ip", "N/A"))
   print(f"{R}[ X ] City: " + data.get("city", "N/A"))
   print(f"{R}[ X ] Region: " + data.get("region", "N/A"))
   print(f"{R}[ X ] Country: " + data.get("country", "N/A"))
   print(f"{R}[ X ] Location: " + data.get("loc", "N/A"))
   print(f"{R}[ X ] Organization: " + data.get("org", "N/A"))
   print("")

def insta():
    try:
       username = input(f"{G}[ - ] Enter account username: ")
       print("")
       profile = instaloader.Profile.from_username(bot.context, username)
       extra.write(f"{G}[ | ] Getting profile...")
       print("")
       userid = profile.userid
       mediacount = profile.mediacount
       igtv = profile.igtvcount
       following = profile.followees
       follower = profile.followers
       bio = profile.biography
       hashtag = profile.biography_hashtags
       mentions = profile.biography_mentions
       pfp = profile.profile_pic_url
       story = profile.has_public_story
       private = profile.is_private
       external_url = profile.external_url
       verified = profile.is_verified
       print("")
       print("Scraping done...")
       print(f"{R}[ X ] Username: {username}")
       print(f"{R}[ X ] User id: {userid}")
       print(f"{R}[ X ] No of posts: {mediacount}")
       print(f"{R}[ X ] Igtv count: {igtv}")
       print(f"{R}[ X ] Following: {following}")
       print(f"{R}[ X ] Followers: {follower}")
       print(f"{R}[ X ] User bio: {bio}")
       print(f"{R}[ X ] Hashtag in bio: {hashtag}")
       print(f"{R}[ X ] Mentions in bio: {mentions}")
       print(f"{R}[ X ] Pfp: {pfp}")
       print(f"{R}[ X ] Has story: {story}")
       print(f"{R}[ X ] Private account: {private}")
       print(f"{R}[ X ] External urls: {external_url}")
       print(f"{R}[ X ] Is verified: {verified}")
       print("")

    except Exception as e:
        print("Error!! please try again later")

R = '\033[31m'
G = '\033[1;32m'
C = '\033[36m'
W = '\033[0m'
Y = '\033[1;33m'

banner = f'''   
{G}─────────█████████████████████
{G}──────████▀─────────────────▀████
{G}────███▀───────────────────────▀███
{G}───██▀───────────────────────────▀██
{G}──█▀───────────────────────────────▀█ 
{G}──█─────────────────────────────────█   {Y}Program : Your ultimate companion{Y}
{G}──█───█████─────────────────█████───█   {Y}Dzanjo 1.0.47{Y}      
{G}──█──██▓▓▓███─────────────███▓▓▓██──█    
{G}──█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█   {Y}Please use this tools only{Y}
{G}──█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█   {Y}for educational purpose{Y}
{G}──█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█   
{G}──▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀   {Y}More tools adding soon in{Y}
{G}────█▄────▀█████▀─────▀█████▀────▄█     {Y}1.1.0 update stay tuned{Y}
{G}───▄██───────────▄█─█▄───────────██▄
{G}───███───────────██─██───────────███
{G}───███───────────────────────────███
{G}────▀██──██▀██──█──█──█──██▀██──██▀
{G}─────▀████▀─██──█──█──█──██─▀████▀
{G}──────▀██▀──██──█──█──█──██──▀██▀
{G}────────────██──█──█──█──██
{G}─────────────█▄▄█▄▄█▄▄█▄▄█
{G}
'''

clear()

print(f"{C}[ X ] Finding latest server ")
time.sleep(2)
print("")

loading()
clear()
print(banner)

def menu():
    print(f"{Y}[ 1 ] instascrape                             [ 2 ] Ip lookup")
    print(f"{Y}[ 3 ] Webcrawl                                [ 4 ] Phone number")
    print(f"{Y}[ 5 ] Domain lookup")
    print("")
    print(f"{Y}[ ! ] Type 0 to exit tool")

menu()
print("")

option = int(input("Choose your option: "))

while option !=0:
    if option==1:
        clear()
        print(banner)
        insta()
        back = input(f"{G}Press enter to exit: ")
        clear()
        print(banner)
        menu()
    
    elif option==2:
        clear()
        print(banner)
        ip()
        back = input(f"{G}Press enter to exit: ")
        clear()
        print(banner)
        menu()

    elif option==3:
        clear()
        print(banner)
        webcrawl()
        back = input(f"{G}Press enter to exit: ")
        clear()
        print(banner)
        menu()

    elif option==4:
        clear()
        print(banner)
        phone()
        back = input(f"{G}Press enter to exit: ")
        clear()
        print(banner)
        menu()

    elif option==5:
        clear()
        print(banner)
        domain()
        back = input(f"{G}Press enter to exit: ")

    else:
        print(" ")
        print("[ ! ] INVALID OPTION ")
        time.sleep(2)
        clear()
        print(banner)
        menu()

    print("")
    option = input("Choose your option: ")
