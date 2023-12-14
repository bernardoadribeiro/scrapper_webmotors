from scrappers import WebmotorsSedanScrapper
from database import save_cars_list_to_db

if __name__ == '__main__':
    # WebmotorsSedanScrapper(total_pages=2).save_results_to_csv()
    # result = WebmotorsSedanScrapper(total_pages=2).create_dataframe_from_search_results()

    # print(result)
    # print(result.info())

    results = WebmotorsSedanScrapper(total_pages=100).process_raw_search_results()
    save_cars_list_to_db(data_list=results)
