{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "gh_321_Assignment_p1_Querying_SQL_Database.py",
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
        "id": "jFvQcchSzHRI",
        "colab_type": "text"
      },
      "source": [
        "# Assignment - Part 1, Querying a Database"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IyzYkBSexOhR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import sqlite3\n",
        "conn = sqlite3.connect('rpg_db.sqlite3')\n",
        "curs = conn.cursor()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FI9PYYh0ygIn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "dde7f9b5-a85c-434b-b05e-9121d160ea53"
      },
      "source": [
        "query = \"\"\"SELECT * FROM charactercreator_character \n",
        "INNER JOIN charactercreator_mage\n",
        "ON character_id = character_ptr_id;\"\"\"\n",
        "curs.execute(query)\n",
        "curs.fetchone()"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(69, 'Totam natus eius fugiat volu', 0, 0, 10, 1, 1, 1, 1, 69, 1, 100)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sPQSMlday2E-",
        "colab_type": "text"
      },
      "source": [
        "## How many total Characters are there?\n",
        "\n",
        "- 302 characters"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "92DNCZefyrke",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "63c1750c-65eb-4dd4-852e-4c29dc7177ca"
      },
      "source": [
        "query = '''SELECT count(character_id) FROM charactercreator_character;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(302,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "l83_tYMyzTM9",
        "colab_type": "text"
      },
      "source": [
        "## How many of each specific subclass?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Mu_6CQOVyEf_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "75d06ed6-a9c1-4ed5-a47a-5638a6c2033e"
      },
      "source": [
        "# Cleric - 75\n",
        "query = '''SELECT count(character_id)\n",
        "FROM charactercreator_character, charactercreator_cleric\n",
        "WHERE character_id = character_ptr_id;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(75,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yjDkHs8M1EsD",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "46e77bff-066b-493b-e4cd-af378a9b2df6"
      },
      "source": [
        "# Fighter - 68\n",
        "query = '''SELECT count(character_ptr_id) FROM charactercreator_fighter;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(68,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "poceB7Tu1LtV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "2f62d41e-4323-4017-a5b1-0ca86b8fd040"
      },
      "source": [
        "# Thief - 51\n",
        "query = '''SELECT count(character_id)\n",
        "FROM charactercreator_character, charactercreator_thief\n",
        "WHERE character_id = character_ptr_id;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(51,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KTrFGr0c1Hdb",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "721803c5-5379-47e1-b3c2-d71e6b99e168"
      },
      "source": [
        "# Mage -108\n",
        "query = '''SELECT count(character_id)\n",
        "FROM charactercreator_character, charactercreator_mage\n",
        "WHERE character_id = character_ptr_id;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(108,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G9YbKJEz1JQT",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "aa94dd38-f725-4bc4-9aee-e192a72659f9"
      },
      "source": [
        "# Necromancer - 11\n",
        "query = '''SELECT count(mage_ptr_id) FROM charactercreator_necromancer;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(11,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kyErIMaP1lru",
        "colab_type": "text"
      },
      "source": [
        "## How many total Items?\n",
        " \n",
        " - 898 items "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "slg91nqi1njD",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "ee8fc091-d23d-4977-9cb6-6ffff2d8766b"
      },
      "source": [
        "query = '''SELECT count(id) FROM charactercreator_character_inventory;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(898,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gXxb4zAN2T_d",
        "colab_type": "text"
      },
      "source": [
        "## How many of the Items are weapons? How many are not?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZJJpI3Cy2UQi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "63b15757-ed3d-4724-b3e0-ac6c90ce75b6"
      },
      "source": [
        "# Items are weapons - 203\n",
        "query = '''SELECT count(item_ptr_id)\n",
        "FROM armory_weapon, charactercreator_character_inventory\n",
        "WHERE item_ptr_id = item_id;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(203,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BvjcD9dK3F1I",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Items are not weapons - 695 ???\n",
        "# subtract all items - all weapons\n",
        "query = '''SELECT name\n",
        "FROM armory_item as ai, armory_weapon as aw\n",
        "WHERE aw.item_ptr_id != ai.item_id;'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "78pxS_Xd7CBj",
        "colab_type": "text"
      },
      "source": [
        "## How many Items does each character have? (Return first 20 rows)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9svN71lJ7BfV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "outputId": "688ef9a1-f42b-4a2d-aa76-6fbfcdb007fe"
      },
      "source": [
        "query = '''SELECT character_id, count(item_id)\n",
        "FROM charactercreator_character_inventory\n",
        "GROUP BY character_id\n",
        "LIMIT 20'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(1, 3),\n",
              " (2, 3),\n",
              " (3, 2),\n",
              " (4, 4),\n",
              " (5, 4),\n",
              " (6, 1),\n",
              " (7, 5),\n",
              " (8, 3),\n",
              " (9, 4),\n",
              " (10, 4),\n",
              " (11, 3),\n",
              " (12, 3),\n",
              " (13, 4),\n",
              " (14, 4),\n",
              " (15, 4),\n",
              " (16, 1),\n",
              " (17, 5),\n",
              " (18, 5),\n",
              " (19, 3),\n",
              " (20, 1)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wyBRztvh7rjy",
        "colab_type": "text"
      },
      "source": [
        "## How many Weapons does each character have? (Return first 20 rows)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E54AILYa7sBQ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "outputId": "c7a4290c-beec-4c38-e577-016b1ae2dca5"
      },
      "source": [
        "query = '''SELECT character_id, count(item_id)\n",
        "FROM charactercreator_character_inventory, armory_weapon\n",
        "WHERE item_id = item_ptr_id\n",
        "GROUP BY character_id\n",
        "LIMIT 20'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(5, 2),\n",
              " (7, 1),\n",
              " (11, 1),\n",
              " (20, 1),\n",
              " (22, 1),\n",
              " (23, 1),\n",
              " (26, 1),\n",
              " (27, 3),\n",
              " (29, 2),\n",
              " (30, 1),\n",
              " (32, 1),\n",
              " (34, 1),\n",
              " (35, 2),\n",
              " (36, 3),\n",
              " (37, 2),\n",
              " (38, 2),\n",
              " (39, 2),\n",
              " (40, 1),\n",
              " (41, 1),\n",
              " (47, 1)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y60Yqw0b7-oC",
        "colab_type": "text"
      },
      "source": [
        "## On average, how many Items does each Character have?\n",
        "\n",
        "- Each character have on average 2.97 items"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3JDR_6W67_Ex",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "07a00860-7b57-4dca-9f51-65c599cdd2f7"
      },
      "source": [
        "query = '''SELECT avg(item_count)\n",
        "FROM\n",
        "(\n",
        "SELECT count(item_id) as item_count\n",
        "FROM charactercreator_character_inventory\n",
        "GROUP BY character_id\n",
        ")'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(2.9735099337748343,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OrsuxF0l90I5",
        "colab_type": "text"
      },
      "source": [
        "## On average, how many Weapons does each character have?\n",
        "\n",
        "- Each character have on average 1.31 weapons"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZvYnIkqI90U4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "bf3bad39-b5b2-4ac5-a1a2-81d7ba78224a"
      },
      "source": [
        "query = '''SELECT avg(weapon_count)\n",
        "FROM\n",
        "(\n",
        "SELECT count(item_id) as weapon_count\n",
        "FROM charactercreator_character_inventory, armory_weapon\n",
        "WHERE item_id = item_ptr_id\n",
        "GROUP BY character_id\n",
        ")'''\n",
        "curs.execute(query)\n",
        "curs.fetchall()"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[(1.3096774193548386,)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    }
  ]
}