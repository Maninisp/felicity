from bs4 import BeautifulSoup


def scrape():

    html = """
    <div class="service-card">
        <h2>ABC Therapy Center</h2>
        <span class="city">Mumbai</span>
        <span class="category">Therapist</span>
    </div>

    <div class="service-card">
        <h2>XYZ Special School</h2>
        <span class="city">Pune</span>
        <span class="category">Special School</span>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")

    services = []

    cards = soup.find_all("div", class_="service-card")

    for card in cards:

        name = card.find("h2").text.strip()
        city = card.find("span", class_="city").text.strip()
        category = card.find("span", class_="category").text.strip()

        services.append({
            "name": name,
            "city": city,
            "category": category,
            "conditions": [],
            "service_type": "Offline"
        })

    return services