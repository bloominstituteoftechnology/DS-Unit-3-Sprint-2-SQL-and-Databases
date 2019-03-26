{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = sqlite3.connect('C:/Users/Donaldo/Downloads/rpg_db.sqlite3')\n",
    "curs = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_chars = \"\"\"\n",
    "SELECT COUNT(*) FROM charactercreator_character\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "subclass_count = \"\"\"\n",
    "SELECT COUNT(*) FROM charactercreator_thief\n",
    "UNION\n",
    "SELECT COUNT(*) FROM charactercreator_cleric\n",
    "UNION\n",
    "SELECT COUNT(*) FROM charactercreator_fighter\n",
    "UNION\n",
    "SELECT COUNT(*) FROM charactercreator_mage\n",
    ";\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_items = \"\"\"\n",
    "SELECT COUNT(*) FROM armory_item;\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "weapons_nonweapons = \n",
    "\"\"\"\n",
    "SELECT COUNT* FROM armory_weapon\n",
    "UNION\n",
    "SELECT (SELECT COUNT(*) AS non_weapon FROM armory_item) \n",
    "- (SELECT COUNT(*) AS weapon FROM armory_weapon);\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "items_per_char =\"\"\"\n",
    "SELECT c.character_id, c.name, i.item_id\n",
    "FROM charactercreator_character AS c\n",
    "INNER JOIN charactercreator_character_inventory AS i\n",
    "ON c.character_id = i.character_id\n",
    "LIMIT 20;\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "weapons_per_char =\"\"\"\n",
    "FROM charactercreator_character AS c\n",
    "SELECT c.character_id, c.name, i.item_id\n",
    "INNER JOIN charactercreator_character_inventory AS i\n",
    "ON c.character_id = i.character_id\n",
    "WHERE i.item_id IN (SELECT item_ptr_id FROM armory_weapon)\n",
    "LIMIT 20\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
