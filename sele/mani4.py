import asyncio
from pyppeteer import launch
from pyppeteer import launcher
import time

async def change_fingerprint():
    # Set the proxy URL and credentials
    proxy_url = '154.194.16.181:6100'
    proxy_username = 'xmruyqww'
    proxy_password = 'dmacublde3rf'

    # Set proxy options
    proxy_options = f'{proxy_username}:{proxy_password}@{proxy_url}'

    # Set proxy environment variables
    launcher.DEFAULT_ARGS.extend(['--no-sandbox', f'--proxy-server={proxy_options}'])

    # Launch the browser
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Set the User-Agent header
    await page.setUserAgent("Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36")

    # Perform your scraping or interaction logic here
    await page.goto('https://www.google.com')
    time.sleep(300)

    # Get the page title and print it
    title = await page.title()
    print('Page Title:', title)

    # Get the page content and print it
    content = await page.content()
    print('Page Content:', content)

    # Take a screenshot and save it
    await page.screenshot(path='screenshot.png')
    print('Screenshot saved as screenshot.png')

    await browser.close()

asyncio.get_event_loop().run_until_complete(change_fingerprint())
