from os.path import join

from pandas import DataFrame

from inflation_scraper import InflationScraper
from util import check_directory, get_datetime


def save_inflation_rate_as_csv(data, file_name, table_heading):
    check_directory('Inflation Data (csv)')

    DataFrame(data, columns=table_heading).to_csv(
        join('Inflation Data (csv)', file_name + '.csv'), index=False)
    print(f'--> CSV created successfully! (Name): {file_name}')


if __name__ == '__main__':
    date_time = get_datetime()

    # '''Getting the inflation_scraper data'''
    inflation_scraper = InflationScraper()
    inflation_data, heading = inflation_scraper.get_inflation_data()

    save_inflation_rate_as_csv(inflation_data, date_time, heading)
