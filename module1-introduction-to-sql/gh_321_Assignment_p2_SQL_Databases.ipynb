{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "gh_321_Assignment_p2_SQL_Databases.py",
      "version": "0.3.2",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4mn8bnzj-Y5R",
        "colab_type": "text"
      },
      "source": [
        "# Assigment - Part 2, Making and populating a Database"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kHKRouO1-Zdp",
        "colab_type": "code",
        "outputId": "db721fe0-6c80-4721-f001-233b4e64cedd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 212
        }
      },
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('https://raw.githubusercontent.com/gyhou/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')\n",
        "print(df.shape)\n",
        "df.head()"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(249, 7)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User Id</th>\n",
              "      <th>Sports</th>\n",
              "      <th>Religious</th>\n",
              "      <th>Nature</th>\n",
              "      <th>Theatre</th>\n",
              "      <th>Shopping</th>\n",
              "      <th>Picnic</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>User 1</td>\n",
              "      <td>2</td>\n",
              "      <td>77</td>\n",
              "      <td>79</td>\n",
              "      <td>69</td>\n",
              "      <td>68</td>\n",
              "      <td>95</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>User 2</td>\n",
              "      <td>2</td>\n",
              "      <td>62</td>\n",
              "      <td>76</td>\n",
              "      <td>76</td>\n",
              "      <td>69</td>\n",
              "      <td>68</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>User 3</td>\n",
              "      <td>2</td>\n",
              "      <td>50</td>\n",
              "      <td>97</td>\n",
              "      <td>87</td>\n",
              "      <td>50</td>\n",
              "      <td>75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>User 4</td>\n",
              "      <td>2</td>\n",
              "      <td>68</td>\n",
              "      <td>77</td>\n",
              "      <td>95</td>\n",
              "      <td>76</td>\n",
              "      <td>61</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>User 5</td>\n",
              "      <td>2</td>\n",
              "      <td>98</td>\n",
              "      <td>54</td>\n",
              "      <td>59</td>\n",
              "      <td>95</td>\n",
              "      <td>86</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  User Id  Sports  Religious  Nature  Theatre  Shopping  Picnic\n",
              "0  User 1       2         77      79       69        68      95\n",
              "1  User 2       2         62      76       76        69      68\n",
              "2  User 3       2         50      97       87        50      75\n",
              "3  User 4       2         68      77       95        76      61\n",
              "4  User 5       2         98      54       59        95      86"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KOgYSX-THNvJ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        },
        "outputId": "cec145fd-326a-4076-bff4-f236700c0f1d"
      },
      "source": [
        "df.describe()"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Sports</th>\n",
              "      <th>Religious</th>\n",
              "      <th>Nature</th>\n",
              "      <th>Theatre</th>\n",
              "      <th>Shopping</th>\n",
              "      <th>Picnic</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>249.000000</td>\n",
              "      <td>249.000000</td>\n",
              "      <td>249.000000</td>\n",
              "      <td>249.000000</td>\n",
              "      <td>249.000000</td>\n",
              "      <td>249.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>11.987952</td>\n",
              "      <td>109.779116</td>\n",
              "      <td>124.518072</td>\n",
              "      <td>116.377510</td>\n",
              "      <td>112.638554</td>\n",
              "      <td>120.401606</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>6.616501</td>\n",
              "      <td>32.454115</td>\n",
              "      <td>45.639372</td>\n",
              "      <td>32.132696</td>\n",
              "      <td>41.562888</td>\n",
              "      <td>32.633339</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>52.000000</td>\n",
              "      <td>59.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>61.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>84.000000</td>\n",
              "      <td>89.000000</td>\n",
              "      <td>93.000000</td>\n",
              "      <td>79.000000</td>\n",
              "      <td>92.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>12.000000</td>\n",
              "      <td>104.000000</td>\n",
              "      <td>119.000000</td>\n",
              "      <td>113.000000</td>\n",
              "      <td>104.000000</td>\n",
              "      <td>119.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>18.000000</td>\n",
              "      <td>132.000000</td>\n",
              "      <td>153.000000</td>\n",
              "      <td>138.000000</td>\n",
              "      <td>138.000000</td>\n",
              "      <td>143.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>25.000000</td>\n",
              "      <td>203.000000</td>\n",
              "      <td>318.000000</td>\n",
              "      <td>213.000000</td>\n",
              "      <td>233.000000</td>\n",
              "      <td>218.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "           Sports   Religious      Nature     Theatre    Shopping      Picnic\n",
              "count  249.000000  249.000000  249.000000  249.000000  249.000000  249.000000\n",
              "mean    11.987952  109.779116  124.518072  116.377510  112.638554  120.401606\n",
              "std      6.616501   32.454115   45.639372   32.132696   41.562888   32.633339\n",
              "min      2.000000   50.000000   52.000000   59.000000   50.000000   61.000000\n",
              "25%      6.000000   84.000000   89.000000   93.000000   79.000000   92.000000\n",
              "50%     12.000000  104.000000  119.000000  113.000000  104.000000  119.000000\n",
              "75%     18.000000  132.000000  153.000000  138.000000  138.000000  143.000000\n",
              "max     25.000000  203.000000  318.000000  213.000000  233.000000  218.000000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d_AVpNyILP_L",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "outputId": "41457f03-d261-4ff8-d5e6-1992188e4bc4"
      },
      "source": [
        "import sqlite3\n",
        "conn = sqlite3.connect('buddymove_holidayiq.sqlite3')\n",
        "df.to_sql('review', con=conn)\n",
        "curs = conn.cursor()"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/pandas/core/generic.py:2531: UserWarning: The spaces in these column names will not be changed. In pandas versions < 0.14, spaces were converted to underscores.\n",
            "  dtype=dtype, method=method)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rh7O03NPMEGm",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "8c1a090c-0f6e-47eb-ee58-a3d90e20848e"
      },
      "source": [
        "query = \"\"\"SELECT * FROM review LIMIT 5\"\"\"\n",
        "curs.execute(query).fetchall()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(0, 'User 1', 2, 77, 79, 69, 68, 95),\n",
              " (1, 'User 2', 2, 62, 76, 76, 69, 68),\n",
              " (2, 'User 3', 2, 50, 97, 87, 50, 75),\n",
              " (3, 'User 4', 2, 68, 77, 95, 76, 61),\n",
              " (4, 'User 5', 2, 98, 54, 59, 95, 86)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vzSsg3fiC_WZ",
        "colab_type": "text"
      },
      "source": [
        "### Count how many rows you have - it should be 249!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dQ4Om7DLAFiC",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "a034d133-4a83-4555-9b9a-999eae39d843"
      },
      "source": [
        "query = \"\"\"\n",
        "SELECT count(0)\n",
        "FROM review\n",
        "\"\"\"\n",
        "curs.execute(query).fetchall()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(249,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9mPhdy_UDAWu",
        "colab_type": "text"
      },
      "source": [
        "### How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?\n",
        "\n",
        "- 78 users"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QHpjFQFKDAeO",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d51bb523-91a9-4314-cba8-ecaf29d405d9"
      },
      "source": [
        "query = \"\"\"\n",
        "SELECT count(Sports)\n",
        "FROM review\n",
        "WHERE Nature >= 100\n",
        "AND Shopping >= 100\n",
        "\"\"\"\n",
        "curs.execute(query).fetchall()"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(78,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LAjF6E0KDESd",
        "colab_type": "text"
      },
      "source": [
        "### (Stretch) What are the average number of reviews for each category?\n",
        "\n",
        "| Sports | Religious | Nature | Theatre | Shopping | Picnic |\n",
        "|--------|-----------|--------|---------|----------|--------|\n",
        "| 11.99  | 109.78    | 124.52 | 116.38  | 112.64   | 120.40 |"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IPMt_HDbGb37",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        },
        "outputId": "a89b3e6e-a99e-4693-a760-6c1acdebe468"
      },
      "source": [
        "query = \"\"\"\n",
        "SELECT avg(Sports),\n",
        "avg(Religious),\n",
        "avg(Nature),\n",
        "avg(Theatre),\n",
        "avg(Shopping),\n",
        "avg(Picnic)\n",
        "FROM review\n",
        "\"\"\"\n",
        "curs.execute(query).fetchall()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(11.987951807228916,\n",
              "  109.77911646586345,\n",
              "  124.51807228915662,\n",
              "  116.37751004016064,\n",
              "  112.63855421686748,\n",
              "  120.40160642570281)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    }
  ]
}
