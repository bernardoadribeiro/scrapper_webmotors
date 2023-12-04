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
