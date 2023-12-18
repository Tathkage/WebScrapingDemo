from django.http import JsonResponse
from bs4 import BeautifulSoup
import httpx
import asyncio

async def fetch_data():
    url = "https://myanimelist.net/anime/season/2023/fall"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Referer": "https://myanimelist.net/"
    }
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            # Handle non-successful status codes
            response.raise_for_status()

async def scrape_top_seasonal_anime():
    response_text = await fetch_data()
    soup = BeautifulSoup(response_text, 'html.parser')

    anime_containers = soup.find_all("div", class_="js-anime-category-producer")
    anime_list = []

    for container in anime_containers:
        title_element = container.find("h3", class_="h3_anime_subtitle") or container.find("h2", class_="h2_anime_title")
        if title_element:
            title = title_element.get_text().strip()

            rating_element = container.find("div", class_="scormem-item")
            if rating_element:
                rating_text = rating_element.get_text().strip()
                try:
                    rating = float(rating_text.split('/')[0].strip())
                    if rating >= 7.0:
                        anime_list.append({"title": title, "rating": rating})
                except ValueError:
                    continue
    return anime_list

# Django view to handle the request
async def scrape_anime_titles(request):
    anime_list = await scrape_top_seasonal_anime()
    return JsonResponse(anime_list, safe=False)
