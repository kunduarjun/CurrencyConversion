# Relevant commands for automating the notification: 
# crontab -l: This command lists the crontabs available. 
# crontab -e: This command opens the crontab in the default editor. 
# Crontab content to automate this script to run every day at 12:30 PM below:
# '30 12 * * * /usr/local/bin/python3 /Users/kunduarjun02/Desktop/VSCode/CurrencyConversion/automateConversion.py'
# Vi commands: 'i' key to enter Insert mode, 'esc' tab to exit Insert mode, ':wq!' keys to exit Vi and save changes.

from dotenv import load_dotenv
import os
import pync
import requests
from datetime import datetime

load_dotenv()

api_key = os.getenv('API_KEY')

cad_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/CAD'
eur_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR'

req_for_cad = requests.get(cad_url)
data_for_cad = req_for_cad.json()
euro_value_for_cad = data_for_cad['conversion_rates']['EUR']

req_for_eur = requests.get(eur_url)
data_for_eur = req_for_eur.json()
cad_value_for_euro = data_for_eur['conversion_rates']['CAD']

current_date = datetime.now().date()

with open('/Users/kunduarjun02/Desktop/VSCode/CurrencyConversion/trackingExchangeRate.txt', 'a') as output_file:
    output_file.write(f'{current_date}: 1 CAD = {euro_value_for_cad} EUR, 1 EUR = {cad_value_for_euro} CAD.\n')

pync.notify(message = 'Open trackingExchangeRate.txt', title = "Check Exchange Rate", timeout = 10)
