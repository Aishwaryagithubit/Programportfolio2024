import sys

# Function to read lap times data from file
def laptime_data(lap_times_filename):
    try:
        with open(lap_times_filename, "r") as f:
            # Read first line for race name
            race_name = f.readline().strip()  
            laptimes = {}  # Initialize dictionary to store driver codes and their lap times
            for line in f:
                # Extract first 3 characters as driver code
                driver_code = line[:3].strip() 
                # Extract remaining part of line and convert to float 
                time = float(line[3:].strip())  
                if driver_code not in laptimes:
                    laptimes[driver_code] = []
                laptimes[driver_code].append(time)

    except FileNotFoundError:
        print(f"Error occured!! {lap_times_filename} does not exist. Please try again.")
        sys.exit(1)  # Exit if file does not found

    except Exception:
        print("Error occured!!")
        sys.exit(1)  # Exit if any other errors
    
    return race_name, laptimes

# Function for reading driver details from file
def read_driver_details(driver_filename):
    driver_details = {}  # Store driver details
    try:
        with open(driver_filename, "r") as f:
            for line in f:
                data = line.strip().split(',')
                # Check if data has exactly 4 elements
                if len(data) == 4: 
                    # remove any extra spaces 
                    driver_code = data[0].strip()  
                    real_name = data[2].strip()
                    team_name = data[3].strip()
                    driver_details[driver_code] = {'realname': real_name, 'teamname': team_name}
    
    except FileNotFoundError:
        print(f"Error occured!!{driver_filename} does not exist.")
        sys.exit(1)  
    except Exception:
        print("Error occured!!")
        sys.exit(1) 
    
    return driver_details

# Function to display results
def display_results(race_name, lap_times, driver_details={}):
    if not race_name or not lap_times:
        print("Error occured!! Race name or lap time data is missing.")
        # Exit if there is no data
        sys.exit(1) 

    # Displaying the location of Grand Prix
    print(f"The Location of Grand prix: {race_name}")

    # Displaying the fastest lap for each driver
    print("\nFastest Time for Each Driver:")
    fastest_laps = {driver: min(times) for driver, times in lap_times.items()}  # Find the fastest lap for each driver
    for driver, fastest_time in fastest_laps.items():
        print(f"{driver}: {fastest_time:.2f} seconds")  # Display fastest time for each driver

    # Sorting in descending order for lap times (Fastest to Slowest)
    sorted_fastest_laps = sorted(fastest_laps.items(), key=lambda x: x[1], reverse=True)  # Sort in descending order
    print("\nFastest Lap Times in Descending Order:")
    for driver, lap_time in sorted_fastest_laps:
        print(f"{driver}: {lap_time:.2f} seconds")  # Display sorted lap times in descending order

    # Calculating average lap times for each driver
    avg_laptime = {driver: sum(times) / len(times) for driver, times in lap_times.items()}
    print("\nAverage Lap Times for Each Driver:")
    for driver, avg_time in avg_laptime.items():
        print(f"{driver}: {avg_time:.2f} seconds")

    # Calculate overall average lap time
    total_lap_times = []
    for times in lap_times.values():
        total_lap_times.extend(times)

    overall_avg_time = sum(total_lap_times) / len(total_lap_times)
    print(f"\nOverall Average Lap Time: {overall_avg_time:.2f} seconds")

    # Displaying driver details (real name and team name) for all drivers in the driver details file
    print("\nDriver Details (with team):")
    for driver_code, details in driver_details.items():
        print(f"{driver_code}: {details['realname']} with team {details['teamname']}")

def main():
    # Check if lap times file is provided
    if len(sys.argv) < 2:
        print("Error occured!! Please provide the lap times file.")
        # Exit if lap times file is not provided
        sys.exit(1) 
    
    # Read lap times data from the file
    lap_times_file = sys.argv[1]
    race_name, laptimes = laptime_data(lap_times_file)

    # Initialize driver_details as empty dictionary
    driver_details = {}

    # Check if driver details file is provided
    if len(sys.argv) == 3: 
        driver_details_file = sys.argv[2]
        driver_details = read_driver_details(driver_details_file)

    # Display results
    display_results(race_name, laptimes, driver_details)

# call the main function
main()

