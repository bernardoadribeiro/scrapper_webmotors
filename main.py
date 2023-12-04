import random
import time
import requests
from fake_useragent import UserAgent
import pandas as pd


class Car():
    """
    Represents a car listing with various attributes.

    Attributes:
    - unique_id (int): A unique identifier for the car listing.
    - title (str): The title or name of the car listing.
    - make (str): The make or brand of the car.
    - model (str): The model of the car.
    - version (str): The version or variant of the car.
    - year_fabrication (str): The year of fabrication of the car.
    - year_model (float): The year model of the car.
    - odometer (float): The mileage or odometer reading of the car.
    - transmission (str): The type of transmission of the car.
    - number_ports (str): The number of ports or doors of the car.
    - body_type (str): The body type of the car.
    - vehicle_attributes (list): A list of dictionaries representing additional attributes of the \
    vehicle.
    - armored (str): Indicates if the car is armored or not.
    - color (str): The primary color of the car.
    - price (float): The price of the car.
    - listing_type (str): The type of listing (e.g., used, new).
    - long_comment (str): A long comment or description of the car.
    - fipe_percent (float): The percentage of the FIPE value.
    - is_elegible_vehicle_ispection (bool): Indicates if the car is eligible for vehicle inspection.
    - is_elegible_360view (bool): Indicates if the car is eligible for a 360-degree view.
    - seller_id (int): The unique identifier of the seller.
    - seller_fantasy_name (str): The fantasy name or business name of the seller.
    - seller_type (str): The type of seller (e.g., individual, dealership).
    - seller_city (str): The city where the seller is located.
    - seller_state (str): The state where the seller is located.
    - seller_adtype (str): The advertisement type of the seller.
    - seller_dealer_score (int): The dealer score of the seller.
    - seller_car_delivery (bool): Indicates if the seller offers car delivery.
    - seller_troca_com_troco (bool): Indicates if the seller accepts trade-ins.

    Methods:
    - to_dict(): Converts the car attributes into a dictionary.

    Example usage:
    ```
    car = Car()
    car.unique_id = 123
    car.title = 'Toyota Camry'
    car.make = 'Toyota'
    # ... (set other attributes)
    car_dict = car.to_dict()
    """

    def __init__(self) -> None:
        self.unique_id = int
        self.title = str
        self.make = str
        self.model = str
        self.version = str
        self.year_fabrication = str
        self.year_model = float
        self.odometer = float
        self.transmission = str
        self.number_ports = str
        self.body_type = str
        self.vehicle_attributes = list[dict]
        self.armored = str
        self.color = str

        self.price = float
        self.listing_type = str
        self.long_comment = str
        self.fipe_percent = float

        self.is_elegible_vehicle_ispection = bool
        self.is_elegible_360view = bool

        self.seller_id = int
        self.seller_fantasy_name = str
        self.seller_type = str
        self.seller_city = str
        self.seller_state = str
        self.seller_adtype = str
        self.seller_dealer_score = int
        self.seller_car_delivery = bool
        self.seller_troca_com_troco = bool

    def to_dict(self):
        """
        Converts the car attributes into a dictionary.

        Returns:
        - dict: A dictionary containing the car attributes.

        Example usage:
        ```
        car = Car()
        # ... (set car attributes)
        car_dict = car.to_dict()
        ```

        """
        return {
            "UniqueId": self.unique_id,
            "Title": self.title,
            "Make": self.make,
            "Model": self.model,
            "Version": self.version,
            "YearFabrication": self.year_fabrication,
            "YearModel": self.year_model,
            "Odometer": self.odometer,
            "Transmission": self.transmission,
            "NumberPorts": self.number_ports,
            "BodyType": self.body_type,
            "VehicleAttributes": self.vehicle_attributes,
            "Armored": self.armored,
            "Color": self.color,

            "Price": self.price,
            "ListingType": self.listing_type,
            "LongComment": self.long_comment,
            "FipePercent": self.fipe_percent,

            "IsElegibleVehicleInspection": self.is_elegible_vehicle_ispection,
            "IsElegible360View": self.is_elegible_360view,

            "SellerId": self.seller_id,
            "SellerType": self.seller_type,
            "SellerCity": self.seller_city,
            "SellerState": self.seller_state,
            "SellerAdType": self.seller_adtype,
            "SellerDealerScore": self.seller_dealer_score,
            "SellerCarDelivery": self.seller_car_delivery,
            "SellerTrocaComTroco": self.seller_troca_com_troco,
            "SellerFantasyName": self.seller_fantasy_name,
        }


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


WebmotorsSedanScrapper(total_pages=2).save_results_to_csv()
result = WebmotorsSedanScrapper(total_pages=2).create_dataframe_from_search_results()

print(result)
print(result.info())
