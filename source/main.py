"""Entry point of application"""

from parse import Parser
import request_handler

print("Welcome to wiki-scraper!")
print("Please enter a Wikipedia article's URL to get started, or hit 'Enter' to load a random article.")
print("Enter '0' to exit.")

menu_dict = {1: "Save document source",
            2: "Print article summary",
            3: "Print article fact pane",
            4: "View article section",
            5: "Download all images",
            6: "Print sources \n",
            0: "Exit \n"}

def print_menu():
    print("Please choose an option:")
    for key in menu_dict:
        print(str(key) + ": " + menu_dict[key])

def random_page():
    pass

def handle_input():
    console = input()
    # Check if the address points to wikipedia
    if console.find("wikipedia.org") > -1 or len(console) == 0:
        if console == "":
            # Load a random document
            console = random_page()
            print("Pulling random Wikipedia article...")

        # Get the document from the address
        print("Pulling Wikipedia article...")
        response = request_handler.simple_get(console)
        if response is not None:
            print("Document successfully loaded: " +
            str(int(response.__sizeof__() * .001)) + "kB")

            # Time to parse the HTML
            parser = Parser(response)
            parser.print_title()

            # Handle user actions
            while True:
                print_menu()
                selection = input()
                # Break out of loop and end program
                if selection == '0':
                    break
                # Save source of document
                elif selection == '1':
                    parser.save_source()
                # Print article summary
                elif selection == '2':
                    parser.print_summary()
                # Print info in fact pane
                elif selection == '3':
                    parser.print_fact_pane()
                # Allow user to choose section in TOC
                elif selection == '4':
                    parser.choose_TOC()
                # Download all images in the article
                elif selection == '5':
                    parser.download_images()
                # View all sources in the article
                elif selection == '6':
                    parser.print_sources()
                else:
                    print("Invalid selection. Please try again.")
        else:
            handle_input()
    elif console == '0':
        # Break out of recursion and end the program
        pass
    else:
        print("Invalid input, please try again. \n")
        handle_input()

# Start the program
handle_input()
