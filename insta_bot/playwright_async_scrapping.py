import csv
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import html5lib
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

def sync_main(link0 ,link1 , link2, link3  ):
    with sync_playwright() as playwright:


        # browser = await playwright.chromium.launch(headless=False , channel='chrome')
        browser =  playwright.webkit.launch(headless=False )
        page0 =  browser.new_page()
        page0.goto(link0)

        page1 = browser.new_page()
        page1.goto(link1)

        page2 = browser.new_page()
        page2.goto(link2)

        page3 =  browser.new_page()
        page3.goto(link3)

        response0 = page0.content()
        response1 = page1.content()
        response2 = page2.content()
        response3 = page3.content()






        soup0 =  BeautifulSoup( response0 , 'html.parser' )
        title0 = soup0.title.text


        soup1 =  BeautifulSoup( response1 , 'html.parser' )
        title1 = soup1.title.text

        soup2 =  BeautifulSoup( response2 , 'html.parser' )
        title2 = soup2.title.text
            # video.findChildren('video')['src']
        soup3 =  BeautifulSoup( response3 , 'html.parser' )
        title3 = soup3.title.text


        # print(post_name, post_link)
        page0.wait_for_timeout(2000)
        page1.wait_for_timeout(2000)
        page2.wait_for_timeout(2000)
        page3.wait_for_timeout(2000)

        # with open('readme.xml', 'w') as f:
        return title0, title1, title2, title3


# def writeIntoCsv(i , post_name , post_link ):
#     with open('suburbanmen.csv', 'a' ) as file:
#         writer = csv.writer(file)
#         if i<2 :
#             writer.writerow(["page-number", "post-name" , "post-link" ])
#         writer.writerow([i, post_name , post_link ])
#     return 0
def create_video_shortcut(index, index2  , link , text ):
    with open(f'reel{index}_{index2}.txt ', mode='w'  ) as f:
        # link = 'https://www.instagram.com/reel/CmdPqtZjnW3/'
        f.write(link)
        f.write('\n')
        f.write(text)


async def login():
    with async_playwright() as playwright:

        # browser = await playwright.chromium.launch(headless=False)
        browser = await  playwright.chromium.launch(headless=False ,channel='chrome' )
        # loginForm > div > div:nth-child(1) > div > label > input
        # loginForm > div > div:nth-child(2) > div > label > input

        page = await browser.new_page()
# for i in range(1,568):
        #await page.goto(f"https://www.suburbanmen.com/page/2/")
        await page.goto("https://www.instagram.com/")
        #
        await  page.fill('//*[@id="loginForm"]/div/div[1]/div/label/input' , 'citynight.exe@gmail.com')
        await  page.fill('//*[@id="loginForm"]/div/div[2]/div/label/input' , 'City@2022')
        await page.click(' //*[@id="loginForm"]/div/div[3]/button' )
        await page.wait_for_timeout(5000)



async def main(link0 ,link1 , link2, link3  ):
    async with async_playwright() as playwright:

        browser = await playwright.chromium.launch(headless=True ,  executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        # browser = await playwright.webkit.launch(headless=False )
        # loginForm > div > div:nth-child(1) > div > label > input
        # loginForm > div > div:nth-child(2) > div > label > input
        # link0 = link[0]
        # link1 = link[1]
        # link2 = link[2]
        # link3 = link[3]
#         page = await browser.new_page()
# # for i in range(1,568):
#         #await page.goto(f"https://www.suburbanmen.com/page/2/")
#         await page.goto("https://www.instagram.com/")
#         #
#         await page.fill('//*[@id="loginForm"]/div/div[1]/div/label/input' , 'enter email')
#         await page.fill('//*[@id="loginForm"]/div/div[2]/div/label/input' , 'enter password')
#
#         await page.click(' //*[@id="loginForm"]/div/div[3]/button' )

        page0 = await browser.new_page()
        await page0.goto(link0)

        page1 = await browser.new_page()
        await page1.goto(link1)

        page2 = await browser.new_page()
        await page2.goto(link2)

        page3 = await browser.new_page()
        await page3.goto(link3)

        response0 = await page0.content()
        response1 = await page1.content()
        response2 = await page2.content()
        response3 = await page3.content()



        #post_name = await page.query_selector_all("xpath=//h2[@class='post-title']//text()")
        #post_link = await page.query_selector_all("xpath=//h2[@class='post-title']//@href")
#writeIntoCsv(i, post_name , post_link )
        # await page.goto("https://www.instagram.com/wonderful_places/reels/")

        # await page.mouse.wheel(0, 25000)



        soup0 =  BeautifulSoup( response0 , 'html.parser' )
        title0 = soup0.title.text


        soup1 =  BeautifulSoup( response1 , 'html.parser' )
        title1 = soup1.title.text

        soup2 =  BeautifulSoup( response2 , 'html.parser' )
        title2 = soup2.title.text
            # video.findChildren('video')['src']
        soup3 =  BeautifulSoup( response3 , 'html.parser' )
        title3 = soup3.title.text
        # await page.goto(video_link)
        # await caption.append(title.text)
        # content = await page.inner_html('.title')
        # print(content)
        # await page.screenshot(path=f"aliexpresspage2.png")
        # with open('readme2.txt', 'w') as f:
        #

        # print(post_name, post_link)
        await page0.wait_for_timeout(2000)
        await page1.wait_for_timeout(2000)
        await page2.wait_for_timeout(2000)
        await page3.wait_for_timeout(2000)

        # with open('readme.xml', 'w') as f:
        return title0, title1, title2, title3
        #      f.write(response)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# a,b = asyncio.run(main(link='https://www.instagram.com/reel/CmdPqtZjnW3/'))

df = pd.read_csv('instagram_wonder_places.csv')
try:
    resume = pd.read_csv('resume.csv')
except:
    start = 13
    limit = 20
# df.reset_index(inplace=True)
text = []
# limit = 12
link = []
# start = 6
# as(login())
for i   in  range(start , len(df)):
    if i > limit :
        break
    else:
        try:
            z = df.iloc[i]
            title0, title1 , title2 , title3 = asyncio.run(main(link0= z[0] ,link1= z[1], link2= z[2], link3= z[3] ))

        except:
            for i in range(start, len(df) , 4):
                if i > limit :
                    break
                else:
                    title0, title1, title2, title3 = asyncio.run(main(link0=df.iloc[i][0] , link1=df.iloc[i+1][0], link2=df.iloc[i+2][0] , link3=df.iloc[i+3][0] ))

            # create_video_shortcut(i, j , link=df.iloc[i , j] , text=title)
        print(title0, title1, title2, title3)
        text.append(title0)
        text.append(title1)
        text.append(title2)
        text.append(title3)
        link.append(df.iloc[i , 0])
        link.append(df.iloc[i,  1])
        link.append(df.iloc[i , 2])
        link.append(df.iloc[i , 3])

# for i , data in enumerate(link) :
#     create_video_shortcut(i, link, text[i])

# df['Caption'] = caption
insta_wonder_place = pd.DataFrame({'Captions':pd.Series(text) , 'link': pd.Series(link)})
insta_wonder_place.to_csv(f'insta_wonder_place_{start}_{limit}.csv')
resume = pd.DataFrame({'start':'f{start}' , 'end': 'f{limit}' )
resume.to_csv('resume.csv')
