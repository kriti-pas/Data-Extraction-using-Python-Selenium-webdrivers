import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

def savetocsv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Bus Name', 'Price', 'Departure Time', 'Seats Available']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file is empty, write the header
        if csvfile.tell() == 0:
            csvwriter.writeheader()

        csvwriter.writerow(data)

def scrape_bus_data(driver):
    bus_data = []

    # Date element
    date_element = driver.find_element(By.XPATH, "//*[@id='travel-distance-source-info']/span[1]")
    current_date = date_element.text.strip()

    # Departure time elements
    departure_time_elements = driver.find_elements(By.XPATH, "//span[@class='departure-time text-sm']")
    departure_times = [time.text for time in departure_time_elements]

    # Number of seats elements
    seats_elements = driver.find_elements(By.XPATH, "//div[@class='text-grey']")
    seats_available = [seats.text.split()[0] if seats.text else "N/A" for seats in seats_elements]

    # Bus name elements
    bus_name_elements = driver.find_elements(By.XPATH, "//p[@class='sub-title']")
    bus_names = [name.text for name in bus_name_elements]

    # Price elements
    price_elements = driver.find_elements(By.XPATH, "//strong[@class='h5 fare']")
    prices = [price.text for price in price_elements]

    # Check if the lengths match
    if len(departure_times) == len(seats_available) == len(bus_names) == len(prices):
        k: int
        for k in range(len(departure_times)):
            print(bus_names[k])
            bus_data.append({
                'Date': current_date,
                'Bus Name': bus_names[k],
                # 'Sleeper': "yes" if "Sleeper" in bus_names[k] else "no",
                # 'Seater': "yes" if "Seater" in bus_names[k] else "no",
                'Price': prices[k],
                'Departure Time': departure_times[k],
                'Seats Available': seats_available[k]
            })
    else:
        print("Number of elements do not match.")

    return bus_data

driver = webdriver.Chrome()

# Open the website
driver.get("https://www.abhibus.com/bus-ticket-booking")
driver.maximize_window()
time.sleep(1)

# From location
from_input = driver.find_element(By.XPATH, "//input[@class='textBox fromTxt ico form-control br-none ui-autocomplete-input']")
from_input.click()
from_input.send_keys("vij")
time.sleep(1)
from_input.send_keys(Keys.RETURN)
time.sleep(1)

# To location
to_input = driver.find_element(By.XPATH, "//input[@class='textBox toTxt ico form-control br-none ui-autocomplete-input']")
to_input.click()
to_input.send_keys("hyd")
time.sleep(1)
to_input.send_keys(Keys.RETURN)
time.sleep(1)

# Date input
date_input = driver.find_element(By.XPATH, "//input[@class='calendar1 form-control br-none hasDatepicker']")
date_input.click()
time.sleep(1)

# You need to provide the date you want to select, for example:
date_input.send_keys()  # Replace with the desired date
time.sleep(1)
date_input.send_keys(Keys.RETURN)
time.sleep(5)

for i in range(2):
    # Bus type selection
    option_to_select = 'AC'
    buttons = driver.find_elements(By.XPATH, "//div[@id='seat-filter-bus-type']/a")

    if buttons:
        for button in buttons:
            if option_to_select in button.text:
                button.click()
                break
    else:
        print("Buttons not found.")
    time.sleep(5)

    option_to_select = 'After 11 PM'
    buttons = driver.find_elements(By.XPATH, "//div[@id='seat-filter-departure-list']/a")

    if buttons:
        for button in buttons:
            if option_to_select in button.text:
                button.click()
                break
    else:
        print("Buttons not found.")

    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='dropdown-icon col auto']").click()
    time.sleep(5)

    # Iterate through each bus and print the information
    bus_data = scrape_bus_data(driver)
    for j, data in enumerate(bus_data, start=1):
        print(f"Bus {j}: {data['Bus Name']} - Date: {data['Date']} - Price: {data['Price']} - Departure Time: {data['Departure Time']} - Seats Available: {data['Seats Available']}")

        # Save to CSV
        # data['Sleeper'] = data['Bus Name']
        # data['Seater'] = data['Bus Name']
        # for z in range(len(data['Bus Name'])):
        #     data['Sleeper'][z] = "yes" if "Sleeper" in data['Bus Name'][z] else "no"
        #     data['Seater'][z] = "yes" if "Seater" in data['Bus Name'][z] else "no"
        savetocsv("C:\\Users\\LOHITHA614\\Desktop\\booking_2024_update.csv", data)

    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class ='btn date text tertiary md inactive button'][1]").click()
time.sleep(10)

driver.quit()
