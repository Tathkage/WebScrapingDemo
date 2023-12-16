import httpx
import asyncio
from bs4 import BeautifulSoup

url = "https://www.booking.com/hotel/in/casa-saligao.html?checkin=2023-11-24&checkout=2023-11-28&group_adults=2&group_children=0&no_rooms=1&selected_currency=USD"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.2816.203 Safari/537.36"}
 
async def fetch_data():
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.text
 
response_text = asyncio.run(fetch_data())
soup = BeautifulSoup(response_text, 'html.parser')

hotel_name = soup.find("h2", class_="pp-header__title").text
hotel_address = soup.find("span", class_="hp_address_subtitle").text
hotel_rating = soup.find("div", class_="a3b8729ab1").text
hotel_review_count = soup.find("span", class_="a3b8729ab1").text.replace("·", "").strip()
facility_elements = soup.select("div[data-testid='property-most-popular-facilities-wrapper'] ul li")

facilities = []

for el in facility_elements:
    facilities.append(el.get_text().strip())

# to avoid duplicate data
middle_index = len(facilities) // 2
hotel_facilities = facilities[:middle_index]

print(hotel_name)
print(hotel_address)
print(hotel_rating)
print(hotel_review_count)
print(hotel_facilities)
