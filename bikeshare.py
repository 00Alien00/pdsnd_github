import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
cityList=['chicago', 'new york', 'washington']
monthList=['january','february','march','april','may','june']
dayList=['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']

#-----------------------------------------------------------------------------------------------------------

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #Chosing city
    city=input('- Would you like to see data for chicago, new york, or washington? or "Exit" to exit the program: ').lower()  
    while True:
        if city=="Exit":
            exit_program()
        if city in cityList:
            break
        else:
            city=input('! Please type a valid city in lowercase or "Exit" to exit the program : ')
    #Chosing filter option
    ans= input('- Would you like to filter the data by month, day, or not at all?(month, day, both, No)')
    while True:
        #option 1
        if ans=='month':
            month=input('- Please type a full name of month with lowercase, or "Exit" to exit the program : ').lower()
            while True:
                if month == "Exit":
                    exit_program()
                if month in monthList:
                    day='all'
                    return city, month, day
                else:
                    month=input('! Please type a valid month name or "Exit" to exit the program : ')
        #option 2
        if ans=='day':
            day=input('- Please type a full name of a day with lowercase, or "Exit" to exit the program : ').lower()
            while True:
                if day == "Exit":
                    exit_program()
                if day in dayList:
                    month='all'
                    return city, month, day
                else:
                    day=input('! Please type a valid day name or "Exit" to exit the program : ')
        #option 3
        if ans=='both':
            month=input('- Please type a full name of month with lowercase, or "Exit" to exit the program : ')
            while True:
                if month == "Exit":
                    exit_program()
                if month in monthList:
                    break
                else:
                    month=input('! Please type a valid month name or "Exit" to exit the program : ')
            day=input('- Please type a full name of a day with lowercase, or "Exit" to exit the program : ')
            while True:
                if day == "Exit":
                    exit_program()
                if day in dayList:
                    break
                else:
                    day=input('! Please type a valid day name or "Exit" to exit the program : ')
            return city, month, day
        #option 4
        if ans=='no':
            month='all'
            day = 'all'
            return city, month, day
        #not in options
        else:
             ans= input('! Please type valid option (month, day, both, no)')
            
        
     
    print('-'*40)
    
#-----------------------------------------------------------------------------------------------------------

def exit_program():
    print("Exiting the program...")
    sys.exit(0)
    
#-----------------------------------------------------------------------------------------------------------    
    
def load_data(city, month, day):
 
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month != 'all':
        df['month'] = df['Start Time'].dt.month
        month = monthList.index(month) + 1
        df = df[df['month'] == month]
 
    if day != 'all':
        df['weekday'] = df['Start Time'].dt.weekday_name
        df = df[df['weekday'] == day.title()]
        
    return df
#-----------------------------------------------------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    if common_month == 1:
        common_month='January'
    if common_month == 2:
        common_month='February'
    if common_month == 3:
        common_month='March'
    if common_month == 4:
        common_month='April'
    if common_month == 5:
        common_month='May'
    if common_month == 6:
        common_month='June'
    print('Most common month:',common_month)
    
    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    common_day = df['weekday'].mode()[0]
    print('Most common day:',common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common Start Hour (in 24-hour time notation):', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------

def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most common start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most common end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station= df['Start Station']+' -> '+df['End Station']
    common_start_end_station= start_end_station.mode()[0]
    print('Most  most frequent combination of start station and end station trip: ', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------

def trip_duration_stats(df):
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    hours, rem = divmod(total_travel_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print('Total travel time: ', "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    hours, rem = divmod(mean_travel_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print('Avrage travel time: ',"{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: \n',user_types,'\n')

    # TO DO: Display counts of gender
    if city!='washington':
        gender_types = df['Gender'].value_counts()
        print('Counts of gender: \n',gender_types,'\n')
    else:
        print('! Washington dataset does not contain information about gender \n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city!='washington':
        earliest_year=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        common_birth_year=df['Birth Year'].mode()
        print('The earliest year of birth: ',earliest_year )
        print('The most recent year of birth: ',most_recent )
        print('Common year of birth: ',common_birth_year )
    else:
        print('! Washington dataset does not contain information about Birth Year \n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        print('you chose: '+city+' '+month+' '+day)
        df = load_data(city, month, day)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        #print('total number of rows in dataframe: ', df.shape[0])
        total_rows=df.shape[0]
        answer=input('- Would you like to view individual trip data? Yes/No \n').lower()
        row_counter=0
        while True:
            if answer == 'yes':
                if row_counter > total_rows:
                    print('! You have viewed all data')
                    break
                else:
                    print(df[row_counter:row_counter+5])
                    row_counter=row_counter+5
            if answer == 'no':
                break
            answer=input('- Would you like to view more? Yes/No \n').lower()

        restart = input('\n- Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
