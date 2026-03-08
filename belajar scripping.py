# belajar scriping
import asyncio #  async adalah sebuah library untuk menjalankan fungsi secara asynchronous atau tidak bersamaan#
import csv # csv adalah sebuah library untuk membaca dan menulis file csv (comma separated values)
from playwright.async_api import async_playwright # async_playwright adalah sebuah library untuk menjalankan browser secara asynchronous dengan menggunakan Playwright
# proses
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= True)
        page = await browser.new_page()
        await page.goto("https://en.wikipedia.org/wiki/Main_Page")
        
        # Tunggu elemen muncul
        await page.wait_for_selector("div#mp-dyk")
        
        # 1. Mengambil data
        title = await page.title()
        elements = await page.locator("div#mp-dyk ul li").all()  # Selector untuk "Did you know?" section
        
        data = []
        for element in elements:
            text = await element.text_content()
            data.append(text)
        
        # 2. Menampilkan ke layar
        print(f"Judul: {title}")
        print("Data yang dikumpulkan:")
        for item in data:
            print(f"- {item}")
        
        # 3. Menyimpan ke CSV
        try:
            with open(r"c:\playwright scrapping\scripping.csv", "w", encoding="utf-8") as file:
                file.write("Data\n")  # Header
                for item in data:
                    file.write(f"{item}\n")
                    print(f"Menulis: {item}")  # Debug
            print("Data berhasil disimpan ke c:\\playwright scrapping\\scripping.csv")
        except Exception as e:
            print(f"Error menyimpan CSV: {e}")
        
        await browser.close()

# Menjalankan fungsi
asyncio.run(main())