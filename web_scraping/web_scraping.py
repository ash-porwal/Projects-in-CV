import requests
from bs4 import BeautifulSoup
import pandas as pd
import configparser
import logging
import os
from shutil import rmtree
from datetime import datetime

class ListBooks():

    def __init__(self, logs):
        self.logs = logs
        self.trigger()
        
    def trigger(self):
        self.read()
        self.get_data()
        self.create_df()
        self.make_file()
        self.remove_files()


    
    def read(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.url = config['creds']['url']
        self.file_path = config['dir_path']['path']

    def get_data(self):
        try:
            self.response = requests.get(self.url)
            print(f"status of resposne - {self.response.status_code}")
            self.logs.info(f"status of resposne - {self.response.status_code}")
        except Exception as e:
            self.logs.exception(e)

    def create_df(self):
        self.book_name, self.book_price, self.book_links = [], [], []

        try:
            soup = BeautifulSoup(self.response.content, "html.parser")

            book_title = soup.find_all('h3')
            # print(book_title[0])

            #getting book titles
            for i in range(len(book_title)):
                self.book_name.append(book_title[i].find('a').attrs["title"])

            book_price = soup.find_all('p', class_ = 'price_color')

            #getting book prices
            for i in range(len(book_price)):
                self.book_price.append(book_price[i].text)

            book_buy_link = soup.find_all('h3') 
            

            #getting book links
            for i in range(len(book_buy_link)):
                self.book_links.append(self.url + book_buy_link[i].find('a').attrs['href'])
        except Exception as e:
            self.logs.exception(e)
        
        try:
            library_dict = {"Name": self.book_name, 
                "Price" : self.book_price, 
                "Link" : self.book_links
                }

            self.books_df = pd.DataFrame(library_dict)
            print(self.books_df)
        except Exception as e:
            self.logs.exception(e)
        
    def make_file(self):

        #if data is already in dataframe
        self.books_df.to_csv(f"{self.file_path}/Books.csv", index=False)
        print("Successfully created book lists to buy")
        self.logs.info("Successfully created book lists to buy")

        #if any other data
        # with open(f"{self.file_path}/Books.json", 'w') as f:
        #     f.write(self.books_df)
    
    def remove_files(self):

        #cleans up locally created files
        enter = input("Do you want to delete locally created files - \nPlease say press (y)for yes else press any key to keep the file ")
        if enter == 'y':
            rmtree(self.file_path, ignore_errors=True)
            print(f"Successfully removed locally created files at {os.getcwd()}/files")
            self.logs.info(f"Successfully removed locally created files at {os.getcwd()}/files")
        else:
            print("Keeping locally created files")
            self.logs.info("Keeping locally created files")


def create_logs():

    #creating the folder to save logs file if not exists there
    os.makedirs("/tmp/Project_in_CV/logs/", exist_ok=True)

    name = 'web_scrapping'
    current_time = datetime.now().strftime("%H%M%S")
    current_date = datetime.today().strftime("%Y%m%d")

    log_filename = os.path.join(
                "/tmp/Project_in_CV/logs/{}_daily_{}_{}_run.log".format(
                    name, current_date, current_time
                    )
                )

    # Set up logging configuration
    logging.basicConfig(
        filename=log_filename,  # saving logs in /tmp
        level=logging.INFO,  # Set the desired logging level
        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Create a logger
    logger = logging.getLogger(__name__)
    return logger

if __name__ == '__main__':

    #creating the folder locally if not exists in current working dir
    os.makedirs("files", exist_ok=True)

    logs = create_logs()

    books = ListBooks(logs)
