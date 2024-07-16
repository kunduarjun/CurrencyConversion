# Currency Conversion Notification System

This python script uses the pync library to create desktop notifications to inform users on exchange rates. 

In this example, I am tracking the exchange rate of CAD to EUR and vice versa. 

This program makes API calls and uses the data obtained from the free ExchangeRate-API, for which a user will have to obtain their own free API key if they want to run this code locally. 

This API key would need to be saved in a '.env' file in the same directory as the program with the variable name 'API_KEY.'

Ex: API_KEY = {Enter your API key as a string here}

Output is written to file named 'trackingExchangeRate.txt' within the same directory as the program. 

Run the 'plottingExchangeRate.py' file to view a graphical representation of the exchange rate data. 
