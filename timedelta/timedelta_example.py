import datetime

def example_of_usage_timedelta():
    print('Usage of timedelta:')

    year = datetime.timedelta(days=1)
    two_weeks = datetime.timedelta(weeks=14)

    print(f'Earth complete full rotate around the Sun for {year.days} days.')
    print(f'One year and two weeks contain {year.seconds+two_weeks.seconds} seconds.')
    print(f'{(datetime.datetime(2020, 1, 1)-datetime.datetime.now()).days} days remain to New Year.')