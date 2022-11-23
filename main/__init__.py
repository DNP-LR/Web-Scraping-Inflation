from os.path import join

from pandas import DataFrame

from crypto_scraper import CryptoScraper
from inflation_scraper import InflationScraper
from util import check_directory, get_datetime


def save_crypto_data_as_csv(data, file_name, table_heading):
    check_directory('Crypto Data (csv)')

    DataFrame(data, columns=table_heading).to_csv(
        join('Crypto Data (csv)', file_name + '.csv'), index=False)
    print(f'--> CSV created successfully! (Name): {file_name}')


def save_inflation_rate_as_csv(data, file_name, table_heading):
    check_directory('Inflation Data (csv)')

    DataFrame(data, columns=table_heading).to_csv(
        join('Inflation Data (csv)', file_name + '.csv'), index=False)
    print(f'--> CSV created successfully! (Name): {file_name}')


if __name__ == '__main__':
    date_time = get_datetime()

# '''Getting the crypto_scraper data'''

    crypto_scraper = CryptoScraper()
    crypto_data, heading = crypto_scraper.get_crypto_data()

    save_crypto_data_as_csv(crypto_data, date_time, heading)

    # '''Getting the inflation_scraper data'''
    inflation_scraper = InflationScraper()
    inflation_data, heading = inflation_scraper.get_inflation_data()

    save_inflation_rate_as_csv(inflation_data, date_time, heading)
