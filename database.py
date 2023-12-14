from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.sqlite import insert

import json

Base = declarative_base()


class WebmotorsData(Base):
    __tablename__ = 'webmotors_data'

    UniqueId = Column(Integer, primary_key=True)
    Title = Column(String)
    Make = Column(String)
    Model = Column(String)
    Version = Column(String)
    YearFabrication = Column(String)
    YearModel = Column(Float)
    Odometer = Column(Float)
    Transmission = Column(String)
    NumberPorts = Column(String)
    BodyType = Column(String)
    VehicleAttributes = Column(String)
    Armored = Column(String)
    Color = Column(String)
    Price = Column(Float)
    ListingType = Column(String)
    LongComment = Column(String)
    FipePercent = Column(Float)
    IsElegibleVehicleInspection = Column(Boolean)
    IsElegible360View = Column(Boolean)
    SellerId = Column(Integer)
    SellerFantasyName = Column(String)
    SellerType = Column(String)
    SellerCity = Column(String)
    SellerState = Column(String)
    SellerAdType = Column(String)
    SellerDealerScore = Column(Integer)
    SellerCarDelivery = Column(Boolean)
    SellerTrocaComTroco = Column(Boolean)


def save_cars_list_to_db(data_list, database_path='webmotors_data.db'):
    engine = create_engine(f'sqlite:///{database_path}', echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert data into the table with conflict resolution
    for data_dict in data_list:
        # Converts list of dicts to JSON string
        data_dict['VehicleAttributes'] = json.dumps(data_dict['VehicleAttributes'])
        # Converts Armored tuple to string
        data_dict['Armored'] = str(data_dict['Armored'])

        insert_stmt = insert(WebmotorsData).values(
            **data_dict).on_conflict_do_nothing(index_elements=[WebmotorsData.UniqueId])
        session.execute(insert_stmt)

    # Commit the changes and close the session
    session.commit()
    session.close()

