"""Class to handle HTML parsing with BeautifulSoup"""

from bs4 import BeautifulSoup
import os.path

class Parser(object):
    def __init__(self, document):
        self.html = BeautifulSoup(document, 'html.parser')
        # Retrive title of document
        title = self.html.find('title').string
        if title is not None:
            self.title = title
        else:
            self.title = "Wikipedia - N/A"

    # Print title of page
    def print_title(self):
        print(self.title + "\n")

    # Print out article summary
    def print_summary(self):
        pass

    # Print out info on fact pane
    def print_fact_pane(self):
        pass

    # Enumerate TOC, print out content of choice
    def choose_TOC(self):
        pass

    # Download all images in the article
    def download_images(self):
        pass

    # Print out source list
    def print_sources(self):
        pass

    # Save raw source to provided path
    def save_source(self):
        print("\nPlease provide an absolute path.")
        path = input()
        path = os.path.join(path, self.title + ".txt")

        try:
            print("\nSaving document...")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.html.prettify())
            print("Document saved. \n")
        except Exception as e:
            print("\n" + str(e))
            print("Please try again. \n")
