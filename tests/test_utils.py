from datetime import timedelta


class TestUtils(object):

    @staticmethod
    def calculate_working_days(excluded_start_date, number_of_days):
        x = 0
        day_counter = 0
        current_datetime = excluded_start_date
        while day_counter < number_of_days:
            x += 1
            current_datetime += timedelta(days=1)
            day_counter += 1 if current_datetime.weekday() in range(0, 5, 1) else 0
        return timedelta(days=x)
