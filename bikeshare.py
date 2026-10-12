import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = list(CITY_DATA.keys())
    while True:
        city = input("\nPlease, enter a city name. \nPossible values: chicago, new york city, washington\n").lower().strip()
        if city in cities:
            break
        else:
            print("\nWrong city name. You entered",city,". Try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    # Here I use a list in order to make the code easy to understand and using the same strategy as the last input.
    months = ['all','january','february','march','april','may','june']
    while True:
        month = input("\nPlease, enter a month name. \nPossible values: all, january, february, march, april, may, june\n").lower().strip()
        if month in months:
            break
        else:
            print("\nWrong month name. You entered ",month,". Try again.")    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Again a list is a solution in order to continue with the same strategy.
    days =['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input("\nPlease, enter a day name. \nPossible values: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday \n").lower().strip()
        if day in days:
            break
        else:
            print("\nWrong day name. You entered ",day,". Try again.") 
                  
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        df - Pandas DataFrame containing the data selected and filtered by the user
    """

    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print("Most common month: ",months[df['month'].mode()[0]-1])
    

    # TO DO: display the most common day of week
    print("Most common day of the week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour: ",df['hour'].mode()[0])    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
        
    Args:
        df - Pandas DataFrame containing the data selected and filtered by the user
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common used start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most common used end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + ' -> ' + df['End Station']
    print("Most common frequent combination: ", df['route'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    
    Args:
        df - Pandas DataFrame containing the data selected and filtered by the user
    """
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ",df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print("Mean travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    
    Args:
        df - Pandas DataFrame containing the data selected and filtered by the user
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of user types\n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Here I check if the Gender column exists. There is one csv file that does not have this column, so it is not possible to show the statistics.
    if 'Gender' in df.columns:
        print("\nCount of Gender\n",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("\nEarliest birth year: ",df['Birth Year'].max())
        print("Most recent birth year: ",df['Birth Year'].min())
        print("Most common birth year: ",df['Birth Year'].mode()[0])
    else:
        print("No Gender and Birth statistics available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    """Displays raw data of the selected and filtered file.

    Args:
        df - Pandas DataFrame containing the data selected and filtered by the user
    """
    control_show_raw_data = input('\nWould you like show the raw data? Enter yes or no.\n')
    if control_show_raw_data.strip().lower() == 'yes':
        i = 0
        while i < df.shape[0]:
           print(df.iloc[i:i+5])
           i+=5
           continue_show_raw_data = input(f"\nContinue with next 5 rows? {df.shape[0] - i} rows pending. Enter yes or no.\n")

           if continue_show_raw_data.strip().lower() != 'yes':
               break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
	main()