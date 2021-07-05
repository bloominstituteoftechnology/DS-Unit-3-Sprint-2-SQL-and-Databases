{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "rpg_queries.py",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
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
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tbradshaw91/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/rpg_queries.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wnFDeekXA2CU",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import sqlite3"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XqDDm1VdBAAt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Establish connection\n",
        "connection = sqlite3.connect('rpg_db.sqlite3')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ARRIBMwzBCpu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "eae8f5ef-901f-46e1-f27e-7cc4357c2d81"
      },
      "source": [
        "# How many total characters were there?\n",
        "query_1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'\n",
        "print ('Total Character Count:',connection.cursor().execute(query_1).fetchone()[0], '\\n')"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Total Character Count: 302 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7_yWj5LpBKiN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "a3bce29d-0bc0-45cc-ad01-2acebb5294ca"
      },
      "source": [
        "#  How many of each specific subclass?\n",
        "query_2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'\n",
        "print ('Mage Count:',connection.cursor().execute(query_2).fetchone()[0], '\\n')          "
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mage Count: 108 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5gfXmGTVBdPU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "fcfeec22-ad6c-4b5b-be68-7d9b10ac9fd7"
      },
      "source": [
        "query_3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'\n",
        "print ('Cleric Count:',connection.cursor().execute(query_3).fetchone()[0], '\\n')"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cleric Count: 75 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fSmB4RfpBhNd",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "898de40f-0351-4ca1-826a-954d0d6bae01"
      },
      "source": [
        "query_4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'\n",
        "print ('Fighter Count:',connection.cursor().execute(query_4).fetchone()[0], '\\n')"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Fighter Count: 68 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0PxMPtwjBjxs",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "e2db7805-a6ff-4425-a134-fb3586f8bfb0"
      },
      "source": [
        "query_5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'\n",
        "print ('Necromancer Count:',connection.cursor().execute(query_5).fetchone()[0], '\\n')"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Necromancer Count: 11 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bx6sbwBiBmgt",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "4b8d12d1-51fd-4b42-8338-b6118755f962"
      },
      "source": [
        "query_6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'\n",
        "print ('Thief Count:',connection.cursor().execute(query_6).fetchone()[0], '\\n')"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Thief Count: 51 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T0o-DZXLCMvh",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "6e18c408-8aef-4fdc-9b77-50af640cfd45"
      },
      "source": [
        "# How many total items?\n",
        "query_7 = 'SELECT COUNT(item_id) FROM armory_item;'\n",
        "print ('Total Items:',connection.cursor().execute(query_7).fetchone()[0], '\\n')"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Total Items: 174 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yT3Sw_rtDAgi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "3d7fca7b-b7ce-4ee4-b5d5-1016b6b8216f"
      },
      "source": [
        "# How many of the items are weapons? How many are not?\n",
        "query_8 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'\n",
        "print ('Total Weapons:',connection.cursor().execute(query_8).fetchone()[0], '\\n')"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Total Weapons: 37 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EYcrevVnDWho",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "68608685-2419-4222-ee01-f52aa154b5b1"
      },
      "source": [
        "query_9 = 'SELECT COUNT(item_id) FROM armory_item WHERE armory_item.item_id not in (SELECT item_ptr_id FROM armory_weapon);'\n",
        "print ('Total Non Weapons:',connection.cursor().execute(query_9).fetchone()[0], '\\n')"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Total Non Weapons: 137 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4AJ8_6SiDpTF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 374
        },
        "outputId": "4bdef3a9-028f-4efb-e2f9-1559d6cbfd75"
      },
      "source": [
        "# How many items does each character have? (Return first 20 rows)\n",
        "query_10 = 'SELECT name, count(name) FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id GROUP BY characters.character_id LIMIT 20;'\n",
        "item_counts = connection.cursor().execute(query_10).fetchmany(20)\n",
        "print ('Sample of Item Count by Character Name:')\n",
        "for char in item_counts:\n",
        "    print (char[0], char[1])"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Sample of Item Count by Character Name:\n",
            "Aliquid iste optio reiciendi 3\n",
            "Optio dolorem ex a 3\n",
            "Minus c 2\n",
            "Sit ut repr 4\n",
            "At id recusandae expl 4\n",
            "Non nobis et of 1\n",
            "Perferendis 5\n",
            "Accusantium amet quidem eve 3\n",
            "Sed nostrum inventore error m 4\n",
            "Harum repellendus omnis od 4\n",
            "Itaque ut commodi, 3\n",
            "Molestiae quis 3\n",
            "Ali 4\n",
            "Tempora quod optio possimus il 4\n",
            "Sed itaque beatae pari 4\n",
            "Quam dolor 1\n",
            "Molestias expedita 5\n",
            "Lauda 5\n",
            "Incidunt sint perferen 3\n",
            "Laboriosa 1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BQ7ALhbqD6_C",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "outputId": "6519b4b8-db88-480a-ecd7-a02f15fbfc86"
      },
      "source": [
        "# How many weapons does each character have? (Return first 20 rows)\n",
        "query_11 = 'SELECT name, count(name) AS weapon_count FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON inventory.character_id = characters.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id LIMIT 20;'\n",
        "weapon_counts = connection.cursor().execute(query_11).fetchmany(20)\n",
        "print ('\\nSample of Weapon Count by Character Name:')\n",
        "for char in weapon_counts:\n",
        "    print (char[0], char[1])"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "Sample of Weapon Count by Character Name:\n",
            "At id recusandae expl 2\n",
            "Perferendis 1\n",
            "Itaque ut commodi, 1\n",
            "Laboriosa 1\n",
            "Dolorum nam reic 1\n",
            "Repellat ad numquam volu 1\n",
            "Doloribus neque 1\n",
            "Ab voluptas se 3\n",
            "In pariatur corpori 2\n",
            "Possimus ad dignissimos vel, a 1\n",
            "Ad necess 1\n",
            "Voluptates sunt voluptas volu 1\n",
            "Autem mollitia fuga lauda 2\n",
            "Sint quibusdam ob 3\n",
            "Rerum et o 2\n",
            "Doloribus dolore r 2\n",
            "Eaque su 2\n",
            "Vel molestias numqua 1\n",
            "Iste assumenda repellat q 1\n",
            "Quod tempora 1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wpkJU1R2EaF3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "a0f17585-da81-4a45-80c8-995d5b1ad24f"
      },
      "source": [
        "# On average, how many items does each character have?\n",
        "query_12 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id GROUP BY characters.character_id);'\n",
        "print ('Average Items:',connection.cursor().execute(query_12).fetchone()[0], '\\n')"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Average Items: 2.9735099337748343 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sPI_I1NFEzYJ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        },
        "outputId": "5378c758-6fe5-45ac-a9dd-744c7a0a0b80"
      },
      "source": [
        "# On average, how many weapons does each character have?\n",
        "query_13 = 'SELECT AVG(counts) FROM (SELECT name, COUNT(name) as counts FROM charactercreator_character_inventory AS inventory LEFT JOIN  charactercreator_character as characters ON characters.character_id = inventory.character_id JOIN armory_weapon ON inventory.item_id = armory_weapon.item_ptr_id GROUP BY characters.character_id);'\n",
        "print ('Average Weapons:',connection.cursor().execute(query_13).fetchone()[0], '\\n')"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Average Weapons: 1.3096774193548386 \n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}