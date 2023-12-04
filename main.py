from scrappers import WebmotorsSedanScrapper


if __name__ == '__main__':
    WebmotorsSedanScrapper(total_pages=2).save_results_to_csv()
    result = WebmotorsSedanScrapper(total_pages=2).create_dataframe_from_search_results()

    print(result)
    print(result.info())
