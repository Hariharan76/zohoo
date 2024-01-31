import asyncio
import json
from pyppeteer import launch
import time

async def change_fingerprint():
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Set the User-Agent header
    await page.setUserAgent("Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36")

    # Perform your scraping or interaction logic here
    await page.goto('https://www.google.com')
    time.sleep(3)
    # Get the page title and print it
    title = await page.title()
    print('Page Title:', title)

    # Get the page content and print it
    content = await page.content()
    print('Page Content:', content)

    # Take a screenshot and save it
    await page.screenshot(path='screenshot.png')
    print('Screenshot saved as screenshot.png')

    # Get all cookies
    cookies = await page.cookies()

    # Store cookies in a JSON file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)

    await browser.close()

asyncio.get_event_loop().run_until_complete(change_fingerprint())
