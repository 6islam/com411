print("Enter the no of dots")
Dots = int(input())

print("Enter the title")
Title = input()b

print(f"{'-' * Dots}")
print(f"{Title}")
print(f"{'-' * Dots}")

import csv

csv_file = "Disneyland.review.csv"

# Create an empty list to store the rows
rows = []

# Read the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)

# Print the number of rows and a confirmation message
print("The dataset has {} rows.".format(len(rows)))
print("The dataset has been successfully read.")

print("please enter the latter which corresponds with your desired menu choice")
print("[A] view data")
print("[B] Visualise Data")
print("[X] Exit")
choice = input()

if choice == "A":
    print("you have chosen option A - View Data")
    print("please entre one of the following options")
    print("[A] View Reviews by Park")
    print("[B] Number of the reviews by Park and Reviewer Location")
    print("[C] Average score per year by Park")
    print("[D] Average score per year by Reviewer Location")
    choice = input()

    if choice == "A":
        import csv

        def display_park_reviews(park_name):
            reviews = []

            # Open the .csv file and read the reviews
            with open('Disneyland.review.csv', 'r') as csv:
                reader = csv.reader(file)
                next(reader)  # Skip the header row

                for row in reader:
                    if row[0] == park_name:
                        reviews.append(row[1])

            if reviews:
                print(f"Reviews for {park_name}:")
                for review in reviews:
                    print(f"- {review}")
            else:
                print(f"No reviews found for {park_name}.")

    elif choice == "B":
        def find_reviews(park_id, location):
            """Finds the number of reviews a specific park has received from a given location"""

        park_id = input("Enter the park ID: ")
        location = input("Enter the reviewer's location: ")

        num_reviews = find_reviews(park_id, location)
        print(f"The park has received {num_reviews} reviews from the specified location.")

    elif choice == "C":
        import Disneyland.Review.csv as file


        def find_average_rating(park, year):
            """Finds the average rating for a specific park in a given year"""

            # Read the csv file into a pandas DataFrame
            reviews = file.read_csv('disneyland.review.csv')

            # Filter the reviews based on the park and year
            filtered_reviews = reviews[(reviews['Park'] == park) & (reviews['Year'] == year)]

            # Check if there are any reviews for the given park and year
            if not filtered_reviews.empty:
                # Calculate the average rating
                average_rating = filtered_reviews['Rating'].mean()

                return average_rating
            else:
                return 0


        park = input("Enter the park name: ")
        year = input("Enter the year: ")

        average_rating = find_average_rating(park, year)
        print(f"The average rating for the park in the given year is {average_rating}.")

elif choice == "B":
    print("please enter one of the following options")
    print("[A] Most Reviewed Parks")
    print("[B] Averages scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most popular Month by Park")
    choice = input()

    if choice == "A":
        import pandas as pd
        import matplotlib.pyplot as plt


        def average_rating():
            """Displays a bar chart showing the average rating of each park"""

            # Read the csv file into a pandas DataFrame
            df = pd.read_csv('disneyland.review.csv')

            # Calculate the average rating for each park
            park_ratings = df.groupby('Park')['Rating'].mean()

            # Plot the average ratings
            park_ratings.plot(kind='bar')
            plt.title('Average Rating per Park')
            plt.xlabel('Park')
            plt.ylabel('Rating')
            plt.show()


        average_rating()
elif choice == "X":
    print("you have chosen option X - Exit")
else:
    print("please entre a valid input")





