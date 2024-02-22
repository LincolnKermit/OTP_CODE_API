import requests, os, time
from bs4 import BeautifulSoup
# Made by Github.com/LincolnKermit
os.system("clear")
base_url = "https://receive-smss.com/"
i = 1
print("API For receive-smss.com in /bin/bash...")
time.sleep(1)
os.system("clear")
print("Country Code...")
country_codes = {
    "+1": "United States",
    "+33": "France",
    "+44": "United Kingdom",
    "+49": "Germany",
    "+81": "Japan",
    "+86": "China",
    "+7": "Russia",
    "+91": "India",
    "+55": "Brazil",
    "+62": "Indonesia",
    "+92": "Pakistan",
    "+90": "Turkey",
    "+82": "South Korea",
    "+20": "Egypt",
    "+34": "Spain",
    "+39": "Italy",
    "+31": "Netherlands",
    "+63": "Philippines",
    "+66": "Thailand",
    "+84": "Vietnam",
    "+27": "South Africa",
    "+41": "Switzerland",
    "+46": "Sweden",
    "+47": "Norway",
    "+46": "Denmark",
    "+358": "Finland",
    "+47": "Norway",
    "+353": "Ireland",
    "+32": "Belgium",
    "+30": "Greece",
    "+43": "Austria",
    "+420": "Czech Republic",
    "+48": "Poland",
    "+52": "Mexico",
    "+1": "Canada",
    "+1": "Puerto Rico",
    "+1": "Guam",
    "+1": "US Virgin Islands",
    "+1": "American Samoa",
    "+1": "Northern Mariana Islands",
    "+1": "Bermuda",
    "+1": "Bahamas",
    "+1": "Jamaica",
    "+1": "Trinidad and Tobago",
    "+1": "Barbados",
    "+1": "Dominican Republic",
    "+1": "Haiti",
    "+1": "Cayman Islands",
    "+1": "Turks and Caicos Islands",
    "+213": "Algeria",
    "+234": "Nigeria",
    "+254": "Kenya",
    "+27": "South Africa",
    "+20": "Egypt",
    "+216": "Tunisia",
    "+212": "Morocco",
    "+237": "Cameroon",
    "+251": "Ethiopia",
    "+225": "Ivory Coast",
    "+233": "Ghana",
    "+221": "Senegal",
    "+254": "Kenya",
    "+256": "Uganda",
    "+235": "Chad",
    "+263": "Zimbabwe",
    "+265": "Malawi",
    "+254": "Tanzania",
    "+62": "Malaysia",
}

time.sleep(0.5)
os.system("clear")
print("Country Code... OK")
print("Header Check...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
time.sleep(0.5)
os.system("clear")
print("Country Code... OK")
print("Header Check... OK")
time.sleep(0)
print("Available Number...")
time.sleep(0)
def number_view():
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        phone_links = soup.find_all('div', {'class': 'number-boxes-itemm-number', 'style': 'color:black'})
        print(phone_links)
        n = 1
        phone_numbers = []
        
        for link in phone_links:
            phone_number = link.get_text(strip=True)
            phone_numbers.append(phone_number)
            print(n, ":", phone_number)
            n += 1
        
        return phone_numbers
    else:
        print(f"La requête a échoué avec le code d'état : {response.status_code}")
        return []

def get_country_from_number(phone_number):
    prefix = phone_number[:3]
    country = country_codes.get(prefix, "Pays inconnu")
    
    return country

phone_numbers = number_view()

if phone_numbers:
    nb_choice = int(input("Sélectionnez un numéro (entrez le numéro correspondant) : "))
    
    if nb_choice >= 1 and nb_choice <= len(phone_numbers):
        selected_number = phone_numbers[nb_choice - 1]
        country = get_country_from_number(selected_number)
        print("Numéro sélectionné :", selected_number)
        print("Pays :", country)
        selected_number = selected_number.replace("+", "")
        url = f"{base_url}sms/{selected_number}/"
        while i > 0:    
            response_msg = requests.get(url, headers=headers)
            os.system("clear")
            if response_msg.status_code == 200:
                soup = BeautifulSoup(response_msg.text, 'html.parser')
                elements = soup.find_all(class_="col-md-6 msgg")
                print(elements.reverse())

                
                for element in elements:
                    text = element.get_text(strip=True)
                    text = text.replace("Message", "")
                    print(text, "\n \n")
                    time.sleep(0.1)
            time.sleep(15)
        else:
            print("Erreur : ", response_msg.status_code)
   
    else:
        print("Choix invalide. Veuillez sélectionner un numéro valide.")
else:
    print("Aucun numéro de téléphone trouvé sur la page.")
