#
# File: timetable.py
# Author: Brian Manoti Okinyi
# Student ID: 110426074
# Email ID: okibm001
# This is my own work as defined by
# the University's Academic Misconduct Policy.
#

def load_timetable():
    """
    Load a timetable from storage.
    """

    timetable = [] # List to store events

    # Try open saved timetable
    try:
        infile = open('timetable.txt', 'r')
    except:
        return [] # Return empty list if it fails
    
    for line in infile:
        events = line.split(',') # Split the string into fields
        timetable.append(events)
    
    # Close the file
    infile.close()

    return timetable

def get_day_of_week(days, question="Enter the day of the week (Sun, Mon, Tue, Wed, Thu, Fri, Sat): "):
    """
    Prompts the user for a day of the week in specified format

    Args:
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        question (string): Question to prompt user for input
    """
    stop = False

    while not stop:
        day = input(question).strip()
        
        if day in days:
            stop = True
        else:
            print("Invalid input. Try again!.")

    # If all checks pass, return day
    return day

def get_title(question="Enter the event title: "):
    """
    Prompts the user for an event title

    Args: 
        question (string): Question to prompt user for input
    """
    stop = False

    while not stop:
        day = input(question).strip()
        
        if day:
            stop = True
        else:
            print("Invalid input. Try again!.")

    return day

def is_valid_time_format(time_str):
    """
    Checks if the input time is of valid format i.e HH:MMAM/PM

    Args:
        time_str (string): The time
    """
    # Check length and basic structure
    if len(time_str) != 7 or time_str[2] != ':' or time_str[-2:] not in ['AM', 'PM']:
        print("Use format HH:MM:AM or PM")
        return False
    
    # Check hour and minute parts
    hour_part = time_str[:2]
    minute_part = time_str[3:5]
    if not hour_part.isdigit() or not minute_part.isdigit():
        return False
    
    # Check hour and minute ranges
    hour = int(hour_part)
    minute = int(minute_part)
    if not (1 <= hour <= 12):
        print("Hour out of range")
        return False
    if not (0 <= minute <= 59):
        print("Minute out of range")
        return False
    
    return True

def get_start_time(question="Enter the start time of the event: "):
    """
    Prompts the user for the start time of the event

    Args: 
        question (string): Question to prompt user for input
    """
    stop = False

    while not stop:
        start_time = input(question)

        if is_valid_time_format(start_time):
            stop = True

    return start_time

def get_end_time(start_time, question="Enter the end time (e.g., 10:30am): "):
    """
    Prompts the user for the end time of the event

    Args: 
        question (string): Question to prompt user for input
    """
    stop = False

    while not stop:
        end_time = input(question)

        if is_valid_time_format(end_time):
            if compare_event_times(start_time, end_time):
                stop = True
        else:
            print("Invalid input. Try again")

    return end_time

def convert_to_24_hour(time_str):
    """
    Convert a time string from AM/PM format to 24-hour format.
    
    Args:
    - time_str (str): Time string in format 'hh:mmAM' or 'hh:mmPM'.
    
    Returns:
    - Tuple (hours, minutes): Hours and minutes in 24-hour format.
    """
    # Split the time string into hours, minutes, and period (AM/PM)
    time_parts = time_str[:-2].split(':')
    period = time_str[-2:]
    
    # Convert to integers
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    
    # Convert hours based on the period
    if period.upper() == "PM" and hours != 12:
        hours += 12
    elif period.upper() == "AM" and hours == 12:
        hours = 0
    
    return hours, minutes

def compare_event_times(start_time, end_time):
    """
    Compare two event times in AM/PM format.

    Args:
    - start_time (str): Start time of the event in format 'hh:mmAM' or 'hh:mmPM'.
    - end_time (str): End time of the event in format 'hh:mmAM' or 'hh:mmPM'.
    
    Returns:
    - str: Comparison result indicating whether start time is before, after, or same as end time.
    """
    start_hours, start_minutes = convert_to_24_hour(start_time)
    end_hours, end_minutes = convert_to_24_hour(end_time)
    
    if (start_hours, start_minutes) >= (end_hours, end_minutes):
        print("Start time is after end time.")
        return False
    if (start_hours, start_minutes) < (end_hours, end_minutes):
        return True

def get_location(question="Enter the event location: "):
    """
    Prompts the user for the event location

    Args: 
        question (string): Question to prompt user for input
    """
    stop = False

    while not stop:
        day = input(question).strip()
        
        if True:
            stop = True
        else:
            print("Invalid input. Try again!.")

    return day

def validate_event(timetable, day, start_time, end_time):
    """
    Validate if event is valid
    """
    for event in timetable[day]:
        if (start_time >= event['start_time'] and start_time < event['end_time']) or \
           (end_time > event['start_time'] and end_time <= event['end_time']):
            return False
    return True

def create_event(timetable, days):
    """
    Creates a new event and adds it to the timetable

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
    day = get_day_of_week(days)
    title = get_title()
    start_time = get_start_time()
    end_time = get_end_time(start_time)
    location = get_location()

    event = {'title': title, 'start_time': start_time, 'end_time': end_time, 'location': location}

    if validate_event(timetable, day, start_time, end_time):
        timetable[day].append(event)
        print("Event successfully added to your timetable", "\n" * 3)
    else:
        print("Could not create event due to time conflict.")

def update_event(timetable, days):
    """
    Updates an existing event in the timetable

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
     
    day = get_day_of_week(days)
    start_time = get_start_time()
    
    for event in timetable[day]:
        if event['start_time'] == start_time:
            new_title = get_title("Enter the new event title: ")
            new_start_time = get_start_time("Enter the new start time (e.g., 10:00am): ")
            new_end_time = get_end_time("Enter the new end time (e.g., 10:30am): ")
            new_location = get_location("Enter the new location (optional): ")

            if validate_event(timetable, day, new_start_time, new_end_time):
                event['title'] = new_title
                event['start_time'] = new_start_time
                event['end_time'] = new_end_time
                event['location'] = new_location

                print("Event updated successfully.")
            else:
                print("Event update failed due to time conflict.")
        else:
            print("We could not find your event.")

def delete_event(timetable, days):
    """
    Deletes an existing event from the timetable

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
     
    day = get_day_of_week(days)
    start_time = get_start_time("Enter start time of the event to delete")

    for event in timetable[day]:
        if event['start_time'] == start_time:
            timetable[day].remove(event)
            print("You have successfully deleted your event.")
            return

    print("We could not find your event")

def print_timetable(timetable, days):
    """
    Prints the current timetable

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """

    # Print header with borders
    header = "| {:<10} |".format("Time/Day") + "".join([" {:<10} |".format(day) for day in days])
    border = "+" + "+".join(["-" * 12] * (len(days) + 1)) + "+"

    print(border)
    print(header)
    print(border)

    hours = [f"{hour:02d}:00" for hour in range(9, 18)]  # Display hours from 9 AM to 5 PM

    for hour in hours:
        row = f"| {hour:<11}"

        for day in days:
            event_at_hour = None

            for event in timetable[day]:
                if event['start_time'].startswith(hour):
                        event_at_hour = event
                        break
            if event_at_hour:
                event_display = event_at_hour['title']
                row += f"| {event_display:<11}"
            else:
                row += f"| {'':<11}"

        print(f"{row}|")
        print(border)

def print_events_of_day(timetable, days):
    """
    Prints the events of a single day

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
     
    day = get_day_of_week(days)
    events = sorted(timetable[day], key=lambda e: e['start_time'])

    if events:
        for event in events:
            print(f"Day: {day}")
            print(f"Title: {event['title']}")
            print(f"Start Time: {event['start_time']}")
            print(f"End Time: {event['end_time']}")
            print(f"Location: {event['location']}")
            print("\n" * 2)
    else:
        print("You have no events today :-")

def save_timetable(timetable):
    """
    Saves the timetable to a file

    Args: 
        timetable (dict): Current timetable
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
     
    outfile = input("Enter the filename to save the timetable: ")

    with open(outfile, 'w') as file:
        for day, events in timetable.items():
            for event in events:
                file.write(f"{day},{event['title']},{event['start_time']},{event['end_time']},{event['location']}\n")
    
    print("Your timetable has successfully been saved.")

def load_timetable(days):
    """
    Loads a timetable from a file

    Args: 
        days (array): Days of the week e.g ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    """
    filename = input("Enter the filename to load the timetable: ")
    timetable = {day: [] for day in days}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    day, title, start_time, end_time, location = parts
                    timetable[day].append({'title': title, 'start_time': start_time, 'end_time': end_time, 'location': location})
                else:
                    print(f"Skipping invalid line: {line.strip()}")

        print("Timetable loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    
    return timetable

def main():
    """
    Main function
    """

    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    timetable = {day: [] for day in days}

    stop = False

    while not stop:
        print("====== PlanSmart Timetable System ======")
        print("Author: Brian Okinyi", "Email: okibm001@mymail.unisa.au", "\n")
        print("1: Create Event")
        print("2: Update Event")
        print("3: Delete Event")
        print("4: Print Timetable")
        print("5. Print Events of a Day")
        print("6: Save Timetable")
        print("7. Load Timetable")
        print("Q: Quit", "\n")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            create_event(timetable, days)
        elif choice == '2':
            update_event(timetable, days)
        elif choice == '3':
            delete_event(timetable)
        elif choice == '4':
            print_timetable(timetable, days)
        elif choice == '5':
            print_events_of_day(timetable, days)
        elif choice == '6':
            save_timetable(timetable)
        elif choice == '7':
            timetable = load_timetable(days)
        elif choice == 'Q':
            print("G'Day")
            stop = True
        else:
            print("Invalid choice. Try again!")

# Start with running the main function.
main()