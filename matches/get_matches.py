from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_furia_matches():
    chrome_service = Service("/usr/bin/chromedriver")
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=chrome_service, options=options)

    try:
        url = "https://liquipedia.net/counterstrike/FURIA/Matches"
        driver.get(url)

        # Aguarda a tabela ser carregada
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.wikitable"))
        )

        # Obtém HTML renderizado e cria o soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        rows = soup.select("table.wikitable tbody tr")

        matches = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 9:
                continue

            def extract_text(td):
                return td.get_text(strip=True).replace('\xa0', ' ')

            match = {
                "date": extract_text(cols[0]),
                "tier": extract_text(cols[1]),
                "type": extract_text(cols[2]),
                "tournament": extract_text(cols[5]),
                "team_1": extract_text(cols[6]),
                "score": extract_text(cols[7]),
                "team_2": extract_text(cols[8]),
            }

            matches.append(match)
            if len(matches) == 5:
                break

        return matches

    finally:
        driver.quit()

