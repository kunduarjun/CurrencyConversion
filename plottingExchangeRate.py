import matplotlib.pyplot as plt

# Lists to store relevant information for our graphs.
dates = []
CAD_to_EUR = []
EUR_to_CAD = []

# Placeholder variable to store the total number of dates with data available.
total_values = None

# Open the text document used for tracking the exchange rate.
with open('/Users/kunduarjun02/Desktop/VSCode/CurrencyConversion/trackingExchangeRate.txt', 'r') as input_file:

    # Read each line of the input file and store each line from this file as a string in a list. 
    information = input_file.readlines()

    # Initialize our placeholder variable.
    total_values = len(information)
    
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
        CAD_conversion_value = float(CAD_conversion_value) 
        CAD_to_EUR.append(CAD_conversion_value)

        # This snippet of code will capture the exchange rate of EUR to CAD on the date specified on the line. 
        index_of_EUR_conversion = line.index('1 EUR = ')
        index_of_CAD = line.index('CAD.')
        EUR_conversion_value = line[index_of_EUR_conversion + 8: index_of_CAD - 1]
        EUR_conversion_value = float(EUR_conversion_value)
        EUR_to_CAD.append(EUR_conversion_value)


# First of all, we need to ask the user how many of the latest values they want to see graphed. 
data_points_to_view = input('Enter in the number of values from the most recent date you want to see: ')

# This input needs to be a digit.
while not data_points_to_view.isdigit():
    print("Please enter in a digit and try again.")
    data_points_to_view = input('Enter in the number of values from the most recent date you want to see: ')

# Convert this input to an integer. 
data_points_to_view = int(data_points_to_view)

# If the user wants to see more values than what currently exists, we will show them all the data that we have. 
if data_points_to_view > total_values:
    data_points_to_view = total_values

# Filter the above lists down.
dates_to_map = dates[-data_points_to_view:]
CAD_to_EUR_to_map = CAD_to_EUR[-data_points_to_view:]
EUR_to_CAD_to_map = EUR_to_CAD[-data_points_to_view:]

plt.plot(dates_to_map, CAD_to_EUR_to_map, label='1 CAD equals this many EUR')
# plt.plot(dates_to_map, EUR_to_CAD_to_map, label='1 EUR equals this many CAD')
plt.xlabel('Date')
plt.xticks(rotation = 55)
plt.ylabel('Exchange Rates')
plt.title('Time Lapse for CAD and EUR Exchange Rates')
plt.legend()
plt.tight_layout()
plt.show()
