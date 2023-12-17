import httpx
import asyncio
from bs4 import BeautifulSoup
import time

url = "https://myanimelist.net/anime/season"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Referer": "https://myanimelist.net/"
}

async def fetch_data():
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            # Handle non-successful status codes
            response.raise_for_status()

response_text = asyncio.run(fetch_data())
soup = BeautifulSoup(response_text, 'html.parser')

# Find all anime containers
anime_containers = soup.find_all("div", class_="js-anime-category-producer")

for container in anime_containers:
    # Add a delay to mimic human browsing
    time.sleep(1)
    
    # Find the title within the container (first try h3, then h2)
    title_element = container.find("h3", class_="h3_anime_title") or container.find("h2", class_="h2_anime_title")
    if title_element:
        title = title_element.get_text().strip()

        # Find the rating within the container
        rating_element = container.find("div", class_="scormem-item")
        if rating_element:
            rating_text = rating_element.get_text().strip()
            try:
                rating = float(rating_text.split('/')[0].strip())
                if rating >= 7.0:
                    print(title)
            except ValueError:
                pass
