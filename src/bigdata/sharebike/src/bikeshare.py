## TODO: import all necessary packages and functions
import time
import sys
import pprint
import datetime
import calendar
import csv
import collections

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

available_month = []
for month_idx in range(1, 13):
    available_month.append(calendar.month_name[month_idx].lower())

available_day_name= []
for day_name in  list(calendar.day_name):
    available_day_name.append(day_name.lower())
    available_day_name.append(str(list(calendar.day_name).index(day_name)+1))

def get_column_by_name(city_file,column_name):
    '''
    get the all value for special column name in the csv file

    :Args city_file: the city file of csv file
    :Args column_name: the colunm name in csv file
    :return: the list value of column name
    '''
    with open(city_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            column = [row[column_name] for row in reader]
            return column
        except KeyError:
            print("The column "+column_name+" is not exist,no data is fetched" )
            return None


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city_file_name_dic = {"chicago": chicago, "new york": new_york_city, "washington": washington}

    for input_times in range(0,3):
        city = input('\nHello! Let\'s explore some US bike share data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n'
                     'User input could be - Chicago, New York, Washington, it is case insensitive: ')
        # TODO: handle raw input and complete function

        if city.strip().lower() in city_file_name_dic.keys():
            return city_file_name_dic.get(city.strip().lower())
        else:
            pprint.pprint("Sorry, that is not a valid input. Please try again",width=30)

    pprint.pprint("input wrong city with 3 times, the process is quiting", width=30)
    sys.exit(0)



def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) month,day or none
    '''

    for input_times in range(0, 3):
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n'
                            'User input could be - month, day,  none it is case insensitive: ')
        # TODO: handle raw input and complete function
        if time_period.strip().lower() == "none":
            return time_period.strip().lower()

        elif time_period.strip().lower() == "month":
            return get_month()

        elif time_period.strip().lower() == "day":
            return get_day()


        #elif time_period.strip().lower() in available_day_name:
         #   return calendar.day_name[int(time_period.strip())-2].lower()

        else:
            pprint.pprint("Sorry, that is not a valid input. Please try again",width=30)

    pprint.pprint("input wrong time period with 3 times, the process is quiting", width=30)
    sys.exit(0)


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) the month name
    '''

    for input_times in range(0, 3):
        month = input('\nWhich month? January, February, March, April, May, or June?\n'
                      'User input could be - January, February, March, April, May, June,....? \nPlease type out the full month name,'
                      ' it is case insensitive:')
        # TODO: handle raw input and complete function

        if month.strip().lower() in available_month:
            return month.strip().lower()
        else:
            print("Sorry, that is not a valid input. Please try again")

    pprint.pprint("input wrong month period with 3 times, the process is quiting", width=30)
    sys.exit(0)



def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str): the name of week day, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    '''

    for input_times in range(0, 3):
        day = input('\nWhich day? Please type your response as an integer.(e.g., 1=Sunday).\n'
                    'User input could be 1, 2, 3, 4, 5, 6, 7, Sunday,Monday...Friday , it is case insensitive:')
        # TODO: handle raw input and complete function
        if day.strip().lower() in available_day_name:
            if day.strip().isdigit():
                return calendar.day_name[int(day.strip())-2].lower()
            else:
                return day.strip().lower()
        else:
            print("Sorry, that is not a valid input. Please try again")
    pprint.pprint("input wrong day value with 3 times, the process is quiting", width=30)
    sys.exit(0)



def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) If the time_period is month or day. the value is none.
        (tuple): If time_period is none, return tuple of popular month, the first parameter is popular month,
                the second is counter
    Question: What month occurs most often in the start time?
    '''
    # TODO: complete function
    month_in_start_time = []

    if time_period.lower()=="none":
        start_time_list = get_column_by_name(city_file,'Start Time')
        for start_time in start_time_list:
            month_in_start_time.append(start_time.split("-")[1])
        most_month_num = collections.Counter(month_in_start_time).most_common(1)[0]
        return calendar.month_name[int(most_month_num[0])],most_month_num[1]

    else:
        pprint.pprint("the time period is month " + time_period + ", no popular month", width=30)
        return ("none","none")




def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) If the time_period is day. the value is ("none","none").
        (tuple):If time_period is none or month, return (popular_day_name,counter )during this time_period
    '''
    # TODO: complete function
    day_in_start_time = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file,"Start Time")
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                day_in_start_time.append(datetime_object.strftime("%A"))

        if len(day_in_start_time) > 0:
            most_day_name = collections.Counter(day_in_start_time).most_common(1)[0]
            return most_day_name[0],most_day_name[1]
        else:
            return "none"

    elif time_period.lower()=="none":
        start_time_list = get_column_by_name(city_file,'Start Time')
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_in_start_time.append(datetime_object.strftime("%A"))

        if len(day_in_start_time) >0:
            most_day_name = collections.Counter(day_in_start_time).most_common(1)[0]
            return most_day_name[0],most_day_name[1]
        else:
            return "none"

    else:
        pprint.pprint("the time period is  " + time_period + ", no popular day", width=30)
        return "none","none"


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What hour of the day (1, 2, ... 23, 24) occurs most often in the start time?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) (popular_hour, counter)
    '''
    # TODO: complete function
    hours_in_start_time = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file,'Start Time')
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                hours_in_start_time.append(start_time.split()[1].split(":")[0])

        most_hours_num = collections.Counter(hours_in_start_time).most_common(1)[0]
        return most_hours_num[0],most_hours_num[1]

    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file,'Start Time')
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                hours_in_start_time.append(start_time.split()[1].split(":")[0])

        most_hours_num = collections.Counter(hours_in_start_time).most_common(1)[0]
        return most_hours_num[0],most_hours_num[1]

    elif time_period.lower()=="none":
        start_time_list = get_column_by_name(city_file,'Start Time')
        for start_time in start_time_list:
            hours_in_start_time.append(start_time.split()[1].split(":")[0])

        most_hours_num = collections.Counter(hours_in_start_time).most_common(1)[0]
        return most_hours_num[0],most_hours_num[1]

    else:
        pprint.pprint("Input time_period"+time_period+" is wrong",width=30)


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) (total_trip_duration, trip_number,average_trip_duration)
    '''
    # TODO: complete function
    trip_duration_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        duration_list = get_column_by_name(city_file, 'Trip Duration')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time,time_index)
                #if duration_list[index].strip().isalnum():
                #    trip_duration_list.append(int(duration_list[index].strip()))
                try:
                    trip_duration_list.append(int(float(duration_list[index].strip())))
                except:
                    print("exceptional duration value:"+ str(duration_list[index].strip()))
                time_index = index

        if len(trip_duration_list)> 0:
            return sum(trip_duration_list), len(trip_duration_list), sum(trip_duration_list)/len(trip_duration_list)
        else:
            return "none","none", "none"

    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        duration_list = get_column_by_name(city_file, 'Trip Duration')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                #if duration_list[index].strip().isalnum():
                 #   trip_duration_list.append(int(duration_list[index].strip()))
                try:
                    trip_duration_list.append(int(float(duration_list[index].strip())))
                except:
                    print("exceptional duration value:"+ str(duration_list[index].strip()))
                time_index = index

        if len(trip_duration_list)>0:
            return sum(trip_duration_list), len(trip_duration_list),sum(trip_duration_list) / len(trip_duration_list)
        else:
            return "none","none", "none"

    elif time_period.lower() == "none":
        duration_list = get_column_by_name(city_file, 'Trip Duration')

        for duration in duration_list:
            try:
                trip_duration_list.append(int(float(duration.strip())))
            except:
                print("exceptional duration value:" + str(duration.strip()))
            #if duration.strip().isalnum():
            #    trip_duration_list.append(int(duration.strip()))


        if len(trip_duration_list)>0:
            return sum(trip_duration_list), len(trip_duration_list),sum(trip_duration_list)/len(trip_duration_list)
        else:
            return "none", "none", "none"

    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) ("most frequently used start station","most frequently used start station counter",
                  "most frequently used end station","most frequently used end station counter",)

    '''
    # TODO: complete function
    start_stations_list = []
    end_stations_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                start_stations_list.append(start_stations[index].strip())
                end_stations_list.append(end_stations[index].strip())
                time_index = index

        most_popular_start_station = collections.Counter(start_stations_list).most_common(1)[0]
        most_popular_end_station = collections.Counter(end_stations_list).most_common(1)[0]
        return most_popular_start_station[0],most_popular_start_station[1], most_popular_end_station[0],most_popular_end_station[1]


    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                start_stations_list.append(start_stations[index].strip())
                end_stations_list.append(end_stations[index].strip())
                time_index = index

        most_popular_start_station = collections.Counter(start_stations_list).most_common(1)[0]
        most_popular_end_station = collections.Counter(end_stations_list).most_common(1)[0]
        return most_popular_start_station[0],most_popular_start_station[1],most_popular_end_station[0],most_popular_end_station[1]

    elif time_period.lower() == "none":
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')

        for start in start_stations:
            start_stations_list.append(start.strip())

        for end in end_stations:
            end_stations_list.append(end.strip())

        most_popular_start_station = collections.Counter(start_stations_list).most_common(1)[0]
        most_popular_end_station = collections.Counter(end_stations_list).most_common(1)[0]
        return most_popular_start_station[0],most_popular_start_station[1],most_popular_end_station[0],most_popular_end_station[1]

    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
     Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple) ("combination of start station and end station",counter)

    '''
    # TODO: complete function
    combin_stations_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                combin_stations_list.append(start_stations[index].strip()+"_"+end_stations[index].strip())
                time_index = index

        most_popular_combin_station = collections.Counter(combin_stations_list).most_common(1)[0]

        return most_popular_combin_station[0],most_popular_combin_station[1]


    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                combin_stations_list.append(start_stations[index].strip() + "_" + end_stations[index].strip())
                time_index = index

        most_popular_combin_station = collections.Counter(combin_stations_list).most_common(1)[0]
        return most_popular_combin_station[0],most_popular_combin_station[1]

    elif time_period.lower() == "none":
        start_time_list = get_column_by_name(city_file, 'Start Time')
        start_stations = get_column_by_name(city_file, 'Start Station')
        end_stations = get_column_by_name(city_file, 'End Station')

        time_index = 0
        for start_time in start_time_list:
            index = start_time_list.index(start_time, time_index)
            combin_stations_list.append(start_stations[index].strip() + "_" + end_stations[index].strip())
            time_index = index

        most_popular_combin_station = collections.Counter(combin_stations_list).most_common(1)[0]

        return most_popular_combin_station[0],most_popular_combin_station[1]

    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (dictionary) {"Subscribers": 4654, "Customers": 257},the dictionary of each user type counter
    '''
    # TODO: complete function
    users_type_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_type = get_column_by_name(city_file, 'User Type')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                users_type_list.append(users_type[index].strip())
                time_index = index

        counter_users_type= collections.Counter(users_type_list)

        return counter_users_type


    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_type = get_column_by_name(city_file, 'User Type')
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                users_type_list.append(users_type[index].strip())
                time_index = index

        counter_users_type = collections.Counter(users_type_list)

        return counter_users_type

    elif time_period.lower() == "none":
        users_type = get_column_by_name(city_file, 'User Type')
        for user in users_type:
            users_type_list.append(user.strip())

        counter_users_type = collections.Counter(users_type_list)

        return counter_users_type
    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (dictionary) the dictionary of gender type
    '''
    # TODO: complete function
    users_gender_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_gender = get_column_by_name(city_file, 'Gender')
        if not users_gender:
            return None
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                if users_gender[index].strip():
                    users_gender_list.append(users_gender[index].strip())
                time_index = index

        counter_users_gender = collections.Counter(users_gender_list)

        return counter_users_gender


    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_gender = get_column_by_name(city_file, 'Gender')
        if not users_gender:
            return None
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                if users_gender[index].strip():
                    users_gender_list.append(users_gender[index].strip())
                time_index = index

        counter_users_gender = collections.Counter(users_gender_list)
        return counter_users_gender

    elif time_period.lower() == "none":
        users_gender = get_column_by_name(city_file, 'Gender')
        if not users_gender:
            return None
        for user in users_gender:
            if user.strip():
                users_gender_list.append(user.strip())

        counter_users_gender = collections.Counter(users_gender_list)
        return counter_users_gender

    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    Args:
        city_file: city file name
        time_period: month or day or none
    Returns:
        (tuple)
        The first one is earliest birth year
        The second one is most recent birth year
        The third one is most common birth year
    '''
    # TODO: complete function
    users_birth_years_list = []

    if time_period in available_month:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_birth_years = get_column_by_name(city_file, 'Birth Year')
        if not users_birth_years:
            return "N/A","N/A","N/A","N/A","N/A","N/A"
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            month_name = datetime_object.strftime("%B").lower()
            if month_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                if users_birth_years[index].strip():
                    users_birth_years_list.append(int(float(users_birth_years[index].strip())))
                time_index = index

        most_birth_years = collections.Counter(users_birth_years_list).most_common(1)[0][0]
        users_birth_years_list.sort()

        return users_birth_years_list[-1],users_birth_years_list.count(users_birth_years_list[-1]),\
               users_birth_years_list[0],users_birth_years_list.count(users_birth_years_list[0]),\
               most_birth_years,users_birth_years_list.count(most_birth_years)


    elif time_period in available_day_name:
        start_time_list = get_column_by_name(city_file, 'Start Time')
        users_birth_years = get_column_by_name(city_file, 'Birth Year')
        if not users_birth_years:
            return "N/A","N/A","N/A","N/A","N/A","N/A"
        time_index = 0
        for start_time in start_time_list:
            datetime_object = datetime.datetime.strptime(start_time.split()[0], '%Y-%m-%d')
            day_name = datetime_object.strftime("%A").lower()
            if day_name == time_period.strip():
                index = start_time_list.index(start_time, time_index)
                if users_birth_years[index].strip():
                    users_birth_years_list.append(int(float(users_birth_years[index].strip())))
                time_index = index

        most_birth_years = collections.Counter(users_birth_years_list).most_common(1)[0][0]
        users_birth_years_list.sort()

        return users_birth_years_list[-1],users_birth_years_list.count(users_birth_years_list[-1]),\
               users_birth_years_list[0],users_birth_years_list.count(users_birth_years_list[0]),\
               most_birth_years,users_birth_years_list.count(most_birth_years)

    elif time_period.lower() == "none":
        users_birth_years = get_column_by_name(city_file, 'Birth Year')
        if not users_birth_years:
            return "N/A","N/A","N/A","N/A","N/A","N/A"
        for user in users_birth_years:
            if user.strip():
                try:
                    users_birth_years_list.append(int(float(user.strip())))
                except ValueError:
                    print("exception value:"+str(user)+".")


        most_birth_years = collections.Counter(users_birth_years_list).most_common(1)[0][0]
        users_birth_years_list.sort()

        return users_birth_years_list[-1], users_birth_years_list.count(users_birth_years_list[-1]), \
               users_birth_years_list[0], users_birth_years_list.count(users_birth_years_list[0]), \
               most_birth_years, users_birth_years_list.count(most_birth_years)

    else:
        pprint.pprint("Input time_period" + time_period + " is wrong", width=30)


def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city_file: city file name
    Returns:
        None
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function

    csvfile = open(city_file, 'r')
    reader = csv.DictReader(csvfile)
    while 1:
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\':')
        if display.strip().lower() == "yes":
            for row in range(1, 6):
                pprint.pprint(next(reader), indent=2)
        elif display.strip().lower() == "no":
            break
        else:
            print("the input is wrong, please input yes or no")
    csvfile.close()


def combine_key_value(dic):
    dic_str = ""
    if not dic:
        return "N/A"
    for k, v in dic.items():
        if dic_str:
            dic_str = dic_str + "," + str(k.capitalize()) + ":" + str(v)
        else:
            dic_str = str(k.capitalize()) + ":" + str(v)

    return dic_str

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period.lower() != "none":
        filter = time_period.capitalize()
    else:
        filter = time_period


    print('\nCalculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        popular_month_data = popular_month(city, time_period)
        #Most popular hour: 17, Count: 723, Filter: both
        print("Most popular month: "+str(popular_month_data[0])+", Count: "+str(popular_month_data[1])+", Filter: "+filter)

        print("That took %s seconds." % (time.time() - start_time))
        print("\n")
        print("Calculating the next statistic...popular_day")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period in available_month:
        start_time = time.time()

        # TODO: call popular_day function and print the results
        popular_day_data = popular_day(city, time_period)
        print("Popular day: " + str(popular_day_data[0]) + ", Count: " + str(
            popular_day_data[1]) + ", Filter: " + filter)
        #print("Popular day is " + popular_day(city, time_period))

        print("That took %s seconds." % (time.time() - start_time))
        print("\n")
        print("Calculating the next statistic...popular_hour")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour_data = popular_hour(city, time_period)
    print("Popular hour: " + str(popular_hour_data[0]) + ", Count: " + str(
        popular_hour_data[1]) + ", Filter: " + filter)
    #pprint.pprint("Popular hour is " + popular_hour(city, time_period), indent=20)

    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...trip_duration")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration_data = trip_duration(city, time_period)
    #Total Duration: 3415956.0, Count: 4911, Avg Duration: 695.5723885155772, Filter: both
    print("Total Duration:  " + str(trip_duration_data[0]) + ", Count: " + str(
        trip_duration_data[1]) + " seconds,Avg Duration:"+str(int(trip_duration_data[2]))+" seconds, Filter: " + filter)
    #pprint.pprint("Total trip duration is " + str(trip_duration_data[0])+" seconds", indent=20)
    #pprint.pprint("Average trip duration is " + str(int(trip_duration_data[1]))+" seconds", indent=20)

    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...popular_station")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    start_end_station_data = popular_stations(city, time_period)
    #Start Station: Clinton St. & Washington Blvd, count:122 - End Station : Clinton St & Washington Blvd, Count: 110, Filter: both
    print("Start Station: "+str(start_end_station_data[0])+", count:"+str(start_end_station_data[1])+
          " - End Station:"+str(start_end_station_data[2])+", Count: "+str(start_end_station_data[3])+", Filter: "+filter)


    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...popular_trip")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip_data= popular_trip(city, time_period)
    #Trip:('Columbus Dr & Randolph St', 'Clinton St & Washington Blvd'), Count: 9, Filter:both
    print("('"+str(popular_trip_data[0].split("_")[0])+"', '"+str(popular_trip_data[0].split("_")[1])+"'), Count: "+str(popular_trip_data[1])+", Filter:"+filter)

    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...user_type")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    #Subscribers: 4654, Customers: 257, Filter: both
    print(combine_key_value(users(city, time_period))+", Filter:"+filter)
    #pprint.pprint("The counts of each user type is " + combine_key_value(users(city, time_period)), indent=20)

    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...gender")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    print(combine_key_value(gender(city, time_period)) + ", Filter:" + filter)
    #pprint.pprint("The counts of gender is " + combine_key_value(gender(city, time_period)), indent=20)

    print("That took %s seconds." % (time.time() - start_time))
    print("\n")
    print("Calculating the next statistic...birth_year")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years_tuple = birth_years(city, time_period)
    print("The oldest years:"+str(birth_years_tuple[0])+", Count:"+str(birth_years_tuple[1])
          +", The youngest years:"+str(birth_years_tuple[2])+", Count:"+str(birth_years_tuple[3])
          +", Most popular years:"+str(birth_years_tuple[4])+", Count:"+str(birth_years_tuple[5]))

    #pprint.pprint("The oldest years is " + str(birth_years_tuple[0]), indent=20)
    #pprint.pprint("The youngest years is " + str(birth_years_tuple[1]), indent=20)
    #pprint.pprint("Most popular years is " + str(birth_years_tuple[1]), indent=20)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.strip().lower() == 'yes':
        statistics()


if __name__ == "__main__":
    #display_data("chicago.csv")
	statistics()
