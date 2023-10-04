import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')

                full_text = ' '.join(soup.stripped_strings)

                return full_text
            else:
                print(f"Статус відповіді: {response.status}")


async def main(word, urls):
    # urls = ['https://meteofor.com.ua/', 'https://ua.sinoptik.ua/']
    tasks = [fetch_text(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, result in zip(urls, results):
        if word in result:
            print(f"Знайдено на сторінці: {url}:\n{word}: {result.count(word)}")

        else:
            print(f"На сторінці: {url} нічого не знайдено: \n{word}: {result.count(word)}")
        print("-" * 100)

if __name__ == '__main__':
    word = input("Введіть слово для пошуку: ")
    urls = input("Введіть url: ").split(", ")
    asyncio.run(main(word, urls))
