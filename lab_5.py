"""

Devin Bulawa
SDEV 300 6381
6/13/2024

"""
import pandas as pd
import matplotlib.pyplot as plt


class InvalidInputException(Exception):
    """A user-defined exception class that validates the input entered"""


def analyze_popchange():
    """Analyzes the population change between apr 1 and jul 1
    and provides the count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to PopChange.csv here
        # reads the data from the change pop column
        df = pd.read_csv(data_set, delimiter=',', usecols=['Change Pop'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Change Pop")
        plt.xlabel("Difference")
        plt.ylabel("Frequency")

        # plots a histogram of the data provided
        plt.hist(df, bins=50, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_popjul1():
    """Analyzes the population of jul 1 and provides the
    count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to PopChange.csv here
        # reads the data from the Pop Jul 1 column
        df = pd.read_csv(data_set, delimiter=',', usecols=['Pop Jul 1'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Pop Jul 1")
        plt.xlabel("Population")
        plt.ylabel("Frequency")

        # plots a histogram of the data provided
        plt.hist(df, bins=50, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_popapr1():
    """Analyzes the population of apr 1 and provides the
    count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to PopChange.csv here
        # reads the data from the Pop Apr 1 column
        df = pd.read_csv(data_set, delimiter=',', usecols=['Pop Apr 1'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Pop Apr 1")
        plt.xlabel("Population")
        plt.ylabel("Frequency")

        # plots a histogram of the data provided
        plt.hist(df, bins=50, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_utility():
    """Analyzes the utility cost column and provides
    the count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to Housing.csv here
        # reads the data from the UTILITY column
        df = pd.read_csv(data_set, delimiter=',', usecols=['UTILITY'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Utility")
        plt.xlabel("Utility Cost")
        plt.ylabel("Sample Size")

        # plots a histogram of the data provided
        plt.hist(df, bins=50, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_rooms():
    """Analyzes the rooms column and provides
    the count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to Housing.csv here
        # reads the data from the ROOMS column
        df = pd.read_csv(data_set, delimiter=',', usecols=['ROOMS'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Rooms")
        plt.xlabel("# of Rooms")
        plt.ylabel("Sample Size")

        # plots a histogram of the data provided
        plt.hist(df, bins=20, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_built():
    """Analyzes the built column and provides
    the count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to Housing.csv here
        # reads the data from the BUILT column
        df = pd.read_csv(data_set, delimiter=',', usecols=['BUILT'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Years Built")
        plt.xlabel("Year Built")
        plt.ylabel("Sample Size")

        # plots a histogram of the data provided
        plt.hist(df, bins=30, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_bedrooms():
    """Analyzes the bedrooms column and provides
    the count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to Housing.csv here
        # reads the data from the BEDRMS column
        df = pd.read_csv(data_set, delimiter=',', usecols=['BEDRMS'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Bedrooms")
        plt.xlabel("# of Bedrooms")
        plt.ylabel("Sample Size")

        # plots a histogram of the data provided
        plt.hist(df, bins=20, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def analyze_age():
    """Analyzes the age column and provides the
    count, mean, std, min, max, and histogram
    of the data"""
    try:
        data_set = ""  # enter path to Housing.csv here
        # reads the data from the AGE column
        df = pd.read_csv(data_set, delimiter=',', usecols=['AGE'])

        # uses pandas to provide the count of the data in the column
        # as well as the mean, standard deviation, min, and max
        print("Count:", df.count().to_string(index=False))
        print("Mean:", df.mean().to_string(index=False))
        print("Standard Deviation:", df.std().to_string(index=False))
        print("Min:", df.min().to_string(index=False))
        print("Max:", df.max().to_string(index=False))
        print("The Histogram of this column is now displayed.")

        # provides a title and axis labels for the histogram
        plt.title("Housing Age")
        plt.xlabel("Age")
        plt.ylabel("Sample Size")

        # plots a histogram of the data provided
        plt.hist(df, bins=50, color='#008fd5', edgecolor='black')
        plt.show()

    # catches if the program detects the file cannot be found instead
    # of throwing an error
    except FileNotFoundError:
        print("File not found. Please check the file path and make sure\n"
              "everything is correct.")


def housing_data():
    """Provides the menu options for analyzing multiple columns
    within the Housing.csv data"""

    print("You have entered Housing Data.")
    while True:
        try:
            # creates a menu of options for the user to choose from
            response = input("Select the Column you want to analyze:\n"
                             "a. AGE\n"
                             "b. BEDRMS\n"
                             "c. BUILT\n"
                             "d. ROOMS\n"
                             "e. UTILITY\n"
                             "f. Exit Column\n")

            if response.lower() == 'a':
                analyze_age()
            elif response.lower() == 'b':
                analyze_bedrooms()
            elif response.lower() == 'c':
                analyze_built()
            elif response.lower() == 'd':
                analyze_rooms()
            elif response.lower() == 'e':
                analyze_utility()
            elif response.lower() == 'f':
                break
            else:
                # raises an exception if a-f is not entered
                raise InvalidInputException
        # provides a reason for the exception and allows for input reentry
        except InvalidInputException:
            print("Invalid input detected. Please enter an option a-f")


def population_data():
    """Provides the menu options for analyzing multiple columns
    within the PopChange.csv data"""

    print("You have entered Population Data.")
    while True:
        try:
            # creates a menu of options for the user to choose from
            response = input("Select the Column you want to analyze:\n"
                             "a. Pop Apr 1\n"
                             "b. Pop Jul 1\n"
                             "c. Change Pop\n"
                             "d. Exit Column\n")
            if response.lower() == 'a':
                analyze_popapr1()
            elif response.lower() == 'b':
                analyze_popjul1()
            elif response.lower() == 'c':
                analyze_popchange()
            elif response.lower() == 'd':
                break
            else:
                # raises an exception if a-d is not entered
                raise InvalidInputException
        # provides a reason for the exception and allows for input reentry
        except InvalidInputException:
            print("Invalid input detected. Please enter an option a-d")


def main():
    """Main function used to run the Python Data Analysis
    Application, providing the option to either analyze
    Population Data, Housing Data, or Exit the Program"""

    print("***************************************")
    print("Welcome to the Python Data Analysis App")
    print("***************************************")

    while True:
        try:
            # creates a menu of options for the user to choose from
            response = input("Select the file you want to analyze:\n"
                             "1. Population Data\n"
                             "2. Housing Data\n"
                             "3. Exit the Program\n")
            if response == '1':
                population_data()
            elif response == '2':
                housing_data()
            elif response == '3':
                break
            else:
                # raises an exception if 1-3 is not entered
                raise InvalidInputException
        # provides a reason for the exception and allows for input reentry
        except InvalidInputException:
            print("Invalid input detected. Please enter an option 1-3")


# launches the program
main()
