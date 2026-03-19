import requests
from bs4 import BeautifulSoup


BASE_URL = "https://thenationaltrust.in/content/registered_organization.php"


def scrape():

    services = []

    for start in range(0, 600, 10):

        url = f"{BASE_URL}?start={start}"

        print("Scraping:", url)
        
        response = requests.get(url)
        
        print("Page length:", len(response.text))


        if response.status_code != 200:
            print("Failed page:", url)
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table")

        if not table:
            print("Table not found, skipping page")
            return []

        rows = table.find_all("tr")[1:]

        for row in rows:

            cols = row.find_all("td")

            if len(cols) < 6:
                continue

            name = cols[3].text.strip()
            state = cols[1].text.strip()
            district = cols[2].text.strip()
            email = cols[4].text.strip()
            address = cols[5].text.strip()

            services.append({
                "name": name,
                "city": district,
                "category": "NGO",
                "conditions": [],
                "service_type": "Offline",
                "email": email,
                "address": address,
                "state": state
            })

    return services