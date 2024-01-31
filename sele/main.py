import asyncio
from pyppeteer import launch

async def change_fingerprint():
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Set the User-Agent header
    await page.setUserAgent('Your User-Agent String')

    # Perform your scraping or interaction logic here

    await browser.close()

asyncio.get_event_loop().run_until_complete(change_fingerprint())