import csv
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import html5lib
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

url = 'https://www.realtor.com/realestateandhomes-search/Lubbock_TX/show-newest-listings/pg-1'


async def async_main( url ):
    with sync_playwright() as playwright:


        browser = await playwright.chromium.launch(headless=False , channel='chrome')
        browser =  playwright.webkit.launch(headless=False )
        page0 = await  browser.new_page()
        await page0.goto(url)
        
        response = await  page0.content()
        soup0 =  BeautifulSoup( response , 'html.parser' )
        print soup0
        
        
asyncio.run(async_main ( url ) )
