from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_product_reviews(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    search_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    review_elements = soup.select('span[data-hook="review-body"]')
    if not review_elements:
        review_elements = soup.find_all('div', {'class': 'a-expander-content'})

    reviews_list = [el.get_text().strip() for el in review_elements]

    driver.quit()


    if not reviews_list:
        return []

    df = pd.DataFrame(reviews_list, columns=['Raw_Review'])
    df['Clean_Review'] = df['Raw_Review'].str.replace(r'[^\w\s]', '', regex=True)

    return df['Clean_Review'].tolist()




if __name__ == "__main__":
    print("--- Starting Test Scrape ---")
    results = get_product_reviews("boat headphones")

    if results:
        print(f"Successfully scraped {len(results)} reviews!")
        for i, review in enumerate(results[:3]):
            print(f"Review {i + 1}: {review[:100]}...")
    else:
        print("No reviews found. Check your internet or selectors.")