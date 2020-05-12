# Imports
import sqlite3
import os
import pandas as pd
import numpy as np

# Create filepath to csv file
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.csv")

# Read in csv file to dataframe
place_review_df = pd.read_csv(DATABASE_FILEPATH)

# Basic dataframe exploration
print(place_review_df.sample(5)) # Get sample of 5 random rows from dataframe
print("\n", place_review_df.shape) # Check shape of data
print("\n", place_review_df.isnull().sum()) # Check for null values

# Rename User Id column to something more easily useable
place_review_df = place_review_df.rename(columns={'User Id' : "UserId"})

# Convert dataframe to SQL
place_review_df.to_sql('buddymove_holidayiq.sqlite3', con=sqlite3.connect('buddymove_holidayiq.sqlite3'), if_exists='replace')

# Instantiate connection
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
connection.row_factory = sqlite3.Row
print("\n", type(connection)) # Check connection type

# Instantiate cursor
cursor = connection.cursor()
print(type(cursor)) # Check cursor type


"""--------------------------------------- SQL COMMAND CODE ---------------------------------------"""


# SQL command code to select number of rows in data
row_count = """
            SELECT
	            count(UserId) as row_count

            FROM
	            "buddymove_holidayiq.sqlite3"
            """

# SQL command code to select number of users who had Nature category review of at least 100 and Shopping category review of at least 100
nature_shop_count = """
                    SELECT
                        count(UserId) as high_nature_shop_count

                    FROM
                        "buddymove_holidayiq.sqlite3"

                    WHERE
                        Nature >= 100 AND
                        Shopping >= 100
                    """

# SQL command code to select the average number of reviews for each category
average_reviews = """
                    SELECT
                        AVG(Sports) as avg_sports_review,
                        AVG(Religious) as avg_religious_review,
                        AVG(Nature) as avg_nature_review,
                        AVG(Theatre) as avg_theatre_review,
                        AVG(Shopping) as avg_shopping_review,
                        AVG(Picnic) as avg_picnic_review

                    FROM
                        "buddymove_holidayiq.sqlite3"
                    """


"""--------------------------------------- SQL EXECUTION CODE ---------------------------------------"""


# Return row_count result from execution
count_result = cursor.execute(row_count).fetchall() # Execute row_count

# Return number of users who had Nature category review of at least 100 and Shopping category review of at least 100
nature_shop_result = cursor.execute(nature_shop_count).fetchall() # Execute nature_shop_count

# Return average number of reviews for each category
average_reviews_result = cursor.execute(average_reviews).fetchall() # Execute average_reviews


"""--------------------------------------- SQL RELAY CODE ---------------------------------------"""


# Relay statement with number of rows in data
for row in count_result:
    print(f"\nNumber of rows: {row['row_count']}")

# Relay statement with number of people who had Nature category review of at least 100 and Shopping category review of at least 100
for row in nature_shop_result:
    print(f"\nThe Number of People Who Reviewed At Least 100 in Nature and Shopping categories: {row['high_nature_shop_count']}")

# Relay statement with average reviews for each category
for row in average_reviews_result:
    print(f"\nAverage Sports Review: {row['avg_sports_review']:.2f}") # Average reviews for Sports
    print(f"Average Religious Review: {row['avg_religious_review']:.2f}") # Average reviews for Religious
    print(f"Average Nature Review: {row['avg_nature_review']:.2f}") # Average reviews for Nature
    print(f"Average Theatre Review: {row['avg_theatre_review']:.2f}") # Average reviews for Theatre
    print(f"Average Shopping Review: {row['avg_shopping_review']:.2f}") # Average reviews for Shopping
    print(f"Average Picnic Review: {row['avg_picnic_review']:.2f}") # Averge reviews for Picnic
    