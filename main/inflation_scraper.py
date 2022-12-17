import requests
from bs4 import BeautifulSoup


class InflationScraper:

    def __init__(self):
        '''Initialization Function'''

        url = 'https://www.rateinflation.com/inflation-rate/germany-historical-inflation-rate'

        self.inflation_list = list()

        while url:
            print('--> Scraping:', url)
            # scraping data from webpage
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            table = soup.find('table')

            # extracting data from table element
            self.extract_inflation_data(table)
            break

    def get_inflation_data(self):
        '''Return Crypto Dataframe'''

        return self.inflation_list, self.get_table_heading()

    @staticmethod
    def get_table_heading(url='https://www.rateinflation.com/inflation-rate/germany-historical-inflation-rate'):
        '''Extracting Table Heading From Webpage'''

        # scraping data from webpage
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        table = soup.find('table')

        # extracting table heading from table element
        heading = list()
        thead = table.find('thead').find('tr').find_all('th')[0:14]
        for th in thead:
            heading.append(th.text)

        return heading

    def extract_inflation_data(self, table):
        '''Extracting Crypto Data From Table'''

        tbody = table.find('tbody').find_all('tr')
        for tr in tbody:
            tds = tr.find_all('td')[0:14]

            # appending crypto data to a class list
            self.inflation_list.append((
                tds[0].text,
                tds[1].text,
                tds[2].text,
                tds[3].text,
                tds[4].text,
                tds[5].text,
                tds[6].text,
                tds[7].text,
                tds[8].text,
                tds[9].text,
                tds[10].text,
                tds[11].text,
                tds[12].text,
                tds[13].text,
            ))
