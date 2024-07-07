import matplotlib.pyplot as plt

# Lists to store relevant information for our graphs.
dates = []
CAD_to_EUR = []
EUR_to_CAD = []

# Open the text document used for tracking the exchange rate.
with open('/Users/kunduarjun02/Desktop/VSCode/CurrencyConversion/trackingExchangeRate.txt', 'r') as input_file:

    # Read each line of the input file and store each line from this file as a string in a list. 
    information = input_file.readlines()
    
    # Iterate over each line in the list to add information to our three lists specified at the top of this file. 
    for line in information:

        # This snippet of code will capture the date of a line and add it to our 'dates' list.
        index_of_colon = line.index(':')
        date = line[:index_of_colon]
        dates.append(date)

        # This snippet of code will capture the exchange rate of CAD to EUR on the date specified on the line. 
        index_of_CAD_conversion = line.index('1 CAD = ')
        index_of_EUR = line.index('EUR, ')
        CAD_conversion_value = line[index_of_CAD_conversion + 8: index_of_EUR - 1]
        # Should this value be converted to an int before adding to the list? This shouldn't be necessary to my understanding. 
        CAD_to_EUR.append(CAD_conversion_value)

        # This snippet of code will capture the exchange rate of EUR to CAD on the date specified on the line. 
        index_of_EUR_conversion = line.index('1 EUR = ')
        index_of_CAD = line.index('CAD.')
        EUR_conversion_value = line[index_of_EUR_conversion + 8: index_of_CAD - 1]
        # Should this value be converted to an int before adding to the list? This shouldn't be necessary to my understanding.
        EUR_to_CAD.append(EUR_conversion_value)


# Now, with those lists populated, we can start creating the graphs. 
