from learning_enumerate import learning_enumerate
from staticmethods_and_properties import staticmethods_and_classmethods, setters_and_getters
from greedy_nongreedy_re import greedy_nongreedy
from timedelta import timedelta_example

import time


if __name__ == "__main__":
    learning_enumerate.demonstration_builtin_enumerate()
    learning_enumerate.own_implementation()

    time.sleep(1)
    print('\n')

    staticmethods_and_classmethods.create_cars_and_count_average_price()

    time.sleep(1)
    print('\n')

    staticmethods_and_classmethods.set_euro_standarts_for_cars()
    setters_and_getters.create_persons()

    time.sleep(1)
    print('\n')

    greedy_nongreedy.greedy_parsing()
    greedy_nongreedy.nongreedy_parsing()

    time.sleep(1)
    print('\n')

    timedelta_example.example_of_usage_timedelta()