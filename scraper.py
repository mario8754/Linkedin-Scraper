import requests

# LinkedIn API URL voor zoekopdrachten
search_url = "https://api.linkedin.com/v2/search?q=people&count=10&start=0"

# LinkedIn API access token (vervanger door uw eigen toegangstoken)
access_token = "YOUR_ACCESS_TOKEN"

# LinkedIn API zoekcriteria (vervanger door uw eigen zoekcriteria)
query = "((title:\"applicatiebeheerder\") AND (industry:\"Zorg\"))"

# Voer de zoekopdracht uit met behulp van de LinkedIn API
response = requests.get(search_url, headers={"Authorization": f"Bearer {access_token}"}, params={"keywords": query})

# Ontvang de resultaten van de zoekopdracht
results = response.json()


# Loop door elk zoekresultaat en haal de gewenste gegevens op
for result in results.get("elements", []):
    # Haal de openbare profiel-URL van de gebruiker op
    profile_url = result.get("targetUrn", "").replace("urn:li:member:", "https://www.linkedin.com/in/")
    
    # Maak een GET-verzoek naar het gebruikersprofiel en sla de HTML-inhoud op
    html_content = requests.get(profile_url).text
    
    # Maak een Beautiful Soup-object van de HTML-inhoud
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Zoek naar de naam, functie, bedrijfsnaam en locatie van de persoon op de pagina en druk deze af
    name = soup.find("h1", class_="pv-top-card-section__name").text.strip()
    job_title = soup.find("h2", class_="pv-top-card-section__headline").text.strip()
    company_name = soup.find("a", class_="pv-top-card-section__company-name").text.strip()
    location = soup.find("span", class_="pv-top-card-section__location").text.strip()
    print(f"{name} ({job_title} at {company_name}) in {location})")
