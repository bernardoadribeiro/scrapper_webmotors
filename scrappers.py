import random
import time
import requests

from fake_useragent import UserAgent
import pandas as pd

from car import Car


class WebmotorsSedanScrapper():
    """
    Scrapes sedan car listings from the Webmotors API.

    Attributes:
    - user_agent (UserAgent): An instance of the UserAgent class for generating random user agents.
    - total_pages (int): The number of pages to retrieve.

    Methods:
    - _fetch_cars(page, display_per_page): Fetches sedan cars from the Webmotors API for a specific\
    page.
    - _get_all_search_results(total_pages): Fetches results from multiple pages and returns a list \
    of all cars.
    - process_raw_search_results(): Processes raw search results to make them compatible with the \
    Car data structure.
    - save_results_to_csv(filename): Fetches, processes, and saves search results as a CSV file.
    - create_dataframe_from_search_results(): Processes raw search results and creates a pandas \
    DataFrame.

    Example usage:
    ```
    scrapper = WebmotorsSedanScrapper()
    scrapper.save_results_to_csv()  # Saves as 'webmotors_results.csv' by default
    result_dataframe = scrapper.create_dataframe_from_search_results()
    ```
    """

    def __init__(self, total_pages: int = 1) -> None:
        self.user_agent = UserAgent()
        self.total_pages = total_pages

    def _fetch_cars(
            self,
            page: int = 1,
            display_per_page: int = 24,
    ) -> list[dict]:
        """
        Fetches sedan cars from Webmotors API for a specific page.

        Parameters:
        - page (int): The page number to fetch. Default is 1.
        - display_per_page (int): Number of items to display per page. Default is 24.

        Returns:
        - list[dict]: A raw list of dictionaries containing search results.
        """
        url = 'https://www.webmotors.com.br/api/search/car'

        # Set HTTP headers with a random User Agent
        headers = {
            'User-Agent': self.user_agent.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8',
            'Referer': 'https://www.google.com/',
            'DNT': '1',  # Do Not Track Request Header
        }

        params = {
            'url': 'https://www.webmotors.com.br/sedans/carros/?necessidade=Sedans',
            'actualPage': page,  # Default: 1
            'displayPerPage': display_per_page,  # Default: 24
            'order': 1,
            'showMenu': True,
            'showCount': True,
            'showBreadCrumb': True,
            'testAB': False,
            'returnUrl': False
        }

        response = requests.get(url=url, headers=headers, params=params)
        json = response.json()

        # print(json['SearchResults'])
        return json['SearchResults']

    def _get_all_search_results(self) -> list[dict]:
        """
        Fetches results from multiple pages and returns a list of all cars.

        Parameters:
        - total_pages (int): The total number of pages to fetch. Default is 2.

        Returns:
        - list[dict]: A raw list of dictionaries containing search results.
        """
        all_results = []

        for page in range(1, self.total_pages + 1):
            search_results = self._fetch_cars(page=page)
            all_results.extend(search_results)

            # Interval between requests to prevent patterns
            time.sleep(random.uniform(1, 5))

        return all_results

    def process_raw_search_results(self) -> list[dict]:
        """
        Processes raw search results to make them compatible with our data structure.

        Returns:
        - list[dict]: A list containing dictionaries with car listing data.
        """
        search_results = self._get_all_search_results()

        cars_list = []

        for result in search_results:
            car = Car()
            car.unique_id = result['UniqueId']
            car.title = result['Specification']['Title']
            car.make = result['Specification']['Make']['Value']
            car.model = result['Specification']['Model']['Value']
            car.version = result['Specification']['Version']['Value']
            car.year_fabrication = result['Specification']['YearFabrication']
            car.year_model = result['Specification']['YearModel']
            car.odometer = result['Specification']['Odometer']
            car.transmission = result['Specification']['Transmission']
            car.number_ports = result['Specification']['NumberPorts']
            car.body_type = result['Specification']['BodyType']
            car.vehicle_attributes = result['Specification']['VehicleAttributes']
            car.armored = result['Specification']['Armored'],
            car.color = result['Specification']['Color']['Primary']
            car.price = result['Prices']['Price']
            car.listing_type = result['ListingType']
            car.long_comment = result.get('LongComment', None)
            car.fipe_percent = result.get('FipePercent', None)
            car.is_elegible_vehicle_ispection = result['IsElegibleVehicleInspection']
            car.is_elegible_360view = result['IsElegible360View']
            car.seller_id = result['Seller']['Id']
            car.seller_fantasy_name = result['Seller']['FantasyName']
            car.seller_type = result['Seller']['SellerType']
            car.seller_city = result['Seller']['City']
            car.seller_state = result['Seller']['State']
            car.seller_adtype = result['Seller']['AdType']['Value']
            car.seller_dealer_score = result['Seller']['DealerScore']
            car.seller_car_delivery = result['Seller']['CarDelivery']
            car.seller_troca_com_troco = result['Seller']['TrocaComTroco']

            cars_list.append(car.to_dict())
            # print(cars_list)

        # print(len(cars_list))
        return cars_list

    def save_results_to_csv(self, filename='webmotors_results.csv') -> None:
        """
        Fetches search results, processes and formats them, and saves as a CSV file.

        Parameters:
        - filename (str): The name of the CSV file to be saved. Default is 'webmotors_results.csv'.
        """
        cars_list = self.process_raw_search_results()
        dataframe = pd.DataFrame(cars_list)
        dataframe.to_csv(filename, sep=',', index=False)

        print(f'DataFrame saved as {filename}')

    def create_dataframe_from_search_results(self) -> pd.DataFrame:
        """
        Processes raw search results and creates a pandas DataFrame.

        Returns:
        - pd.DataFrame: A pandas DataFrame containing the processed search results.
        """
        cars_list = self.process_raw_search_results()
        dataframe = pd.DataFrame(cars_list)

        return dataframe
