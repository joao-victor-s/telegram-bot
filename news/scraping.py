from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_news(topic):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        search_url = f"https://www.google.com/search?q={topic}&tbm=nws"
        driver.get(search_url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.SoaBEf"))
        )

        news_elements = driver.find_elements(By.CSS_SELECTOR, "div.SoaBEf")
        news_results = []

        for news in news_elements[:3]:
            title_elem = news.find_element(By.CSS_SELECTOR, "div.MBeuO")
            link_elem = news.find_element(By.TAG_NAME, "a")
            snippet_elem = news.find_element(By.CSS_SELECTOR, "div.GI74Re")

            title = title_elem.text
            link = link_elem.get_attribute("href")
            snippet = snippet_elem.text

            news_results.append({
                "title": title,
                "link": link,
                "snippet": snippet
            })
            
        return news_results

    finally:
        driver.quit()
