#Program begins
import time
import pandas as pd
import numpy as np
#A dictionary for the 3 cities: Chicago, New_York and Washington city
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#function to perform the filtering
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Setting an empty city to store input from the user
    city = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("\nWelcome!. Please choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city (not case sensitive)")
        #converting user input into lower to standardize them
        city = input().lower()
   
        if city not in CITY_DATA.keys():
            print("\nPlease check your input to suit the acceptable format")
            print(f"\nYou have chosen {city.title()} as your city.")

    # TO DO: get user input for month (all, january, february, ... , june)
MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month, between January to June, for which you're seeking the data:")
        print("\nAccepted input:\nFull month name (not case sensitive "))
        print("\n(You may also opt to view data for all months, please type 'all' (Not Case sensitive).)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid month input.")
            print(f"\nYou have chosen {month.title()} as your month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name (not case sensitive)")
        print("\n(You may also opt to view data for all days, please type 'all' (Not Case sensitive).)")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nInvalid Day Inpu.")
            print(f"\nYou have chosen {day.title()} as your day.")
            print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
            print('-'*40)
    return city, month, day

#loading the .csv file
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#Load data for city
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])
     #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
popular_month = df['month'].mode()[0]
 print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    # TO DO: display the most common day of week
 popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")
#Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common start hour
 popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
     common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of trips are from {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
total_duration = df['Trip Duration'].sum()
#Finds out the duration in minutes and seconds format
    minute, second = divmod(total_duration, 60)
    #Finds out the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")
    # TO DO: display mean travel time
     average_duration = round(df['Trip Duration'].mean()
     #Finds the average duration in minutes and seconds format
    mins, sec = divmod(average_duration, 60)
    #This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
     user_type = df['User Type'].value_counts()
    print(f"The types of users by number are given below:\n\n{user_type}")

    # TO DO: Display counts of gender
 #This try clause is implemented to display the numebr of users by Gender
    #However, not every df may have the Gender column, hence this...
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    #Similarly, this try clause is there to ensure only df containing
    #'Birth Year' column are displayed
    #The earliest birth year, most recent birth year and the most common
    #birth years are displayed
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  #Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.

    Args:
        param1 (df): The data frame you wish to work with.

    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*40)
#Main function to call all the previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
