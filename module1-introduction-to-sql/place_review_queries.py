import sqlite3
import os
import pandas as pd
import numpy as np

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.csv")
place_review_df = pd.read_csv(DATABASE_FILEPATH)
print(place_review_df.sample(5))
print("\n", place_review_df.shape)
print("\n", place_review_df.isnull().sum())

place_review_df = place_review_df.rename(columns={'User Id' : "UserId"})

place_review_df.to_sql('buddymove_holidayiq.sqlite3', con=sqlite3.connect('buddymove_holidayiq.sqlite3'), if_exists='replace')

connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
connection.row_factory = sqlite3.Row
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

row_count = """
            SELECT
	            count(UserId) as row_count

            FROM
	            "buddymove_holidayiq.sqlite3"
            """
count_result = cursor.execute(row_count).fetchall()

for row in count_result:
    print(f"Number of rows: {row['row_count']}")

nature_shop_count = """
                    SELECT
                        count(UserId) as high_nature_shop_count

                    FROM
                        "buddymove_holidayiq.sqlite3"

                    WHERE
                        Nature >= 100 AND
                        Shopping >= 100
                    """

nature_shop_result = cursor.execute(nature_shop_count).fetchall()

for row in nature_shop_result:
    print(f"The Number of People Who Reviewed At Least 100 in Nature and Shopping categories: {row['high_nature_shop_count']}")

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

average_reviews_result = cursor.execute(average_reviews).fetchall()

for row in average_reviews_result:
    print(f"Average Sports Review: {row['avg_sports_review']:.2f}")
    print(f"Average Religious Review: {row['avg_religious_review']:.2f}")
    print(f"Average Nature Review: {row['avg_nature_review']:.2f}")
    print(f"Average Theatre Review: {row['avg_theatre_review']:.2f}")
    print(f"Average Shopping Review: {row['avg_shopping_review']:.2f}")
    print(f"Average Picnic Review: {row['avg_picnic_review']:.2f}")
    