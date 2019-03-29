{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "connect = sqlite3.connect('C:/Users/Donaldo/Downloads/northwind_small.sqlite3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor = connect.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "expensive_items = \"\"\"SELECT ProductName, UnitPrice \n",
    "FROM Product ORDER BY UnitPrice DESC\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "expensive_items = cursor.execute(expensive_items).fetchmany(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Côte de Blaye\n",
      "Thüringer Rostbratwurst\n",
      "Mishi Kobe Niku\n",
      "Sir Rodney's Marmalade\n",
      "Carnarvon Tigers\n",
      "Raclette Courdavault\n",
      "Manjimup Dried Apples\n",
      "Tarte au sucre\n",
      "Ipoh Coffee\n",
      "Rössle Sauerkraut\n"
     ]
    }
   ],
   "source": [
    "# Top 10 most expensive items\n",
    "for item in expensive_items:\n",
    "    print(item[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "average_employee_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "average_employee_age = cursor.execute(average_employee_age).fetchone()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "37.22222222222222\n"
     ]
    }
   ],
   "source": [
    "#Average age of an amployee when hired\n",
    "print(average_employee_age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "expensive_things = \"\"\"\n",
    "SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName\n",
    "FROM Product, Supplier\n",
    "WHERE Product.SupplierID = Supplier.ID\n",
    "ORDER BY UnitPrice DESC\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "expensive_things = cursor.execute(expensive_things).fetchmany(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Item:  Côte de Blaye \n",
      "Supplier:  Aux joyeux ecclésiastiques\n",
      "Item:  Thüringer Rostbratwurst \n",
      "Supplier:  Plutzer Lebensmittelgroßmärkte AG\n",
      "Item:  Mishi Kobe Niku \n",
      "Supplier:  Tokyo Traders\n",
      "Item:  Sir Rodney's Marmalade \n",
      "Supplier:  Specialty Biscuits, Ltd.\n",
      "Item:  Carnarvon Tigers \n",
      "Supplier:  Pavlova, Ltd.\n",
      "Item:  Raclette Courdavault \n",
      "Supplier:  Gai pâturage\n",
      "Item:  Manjimup Dried Apples \n",
      "Supplier:  G'day, Mate\n",
      "Item:  Tarte au sucre \n",
      "Supplier:  Forêts d'érables\n",
      "Item:  Ipoh Coffee \n",
      "Supplier:  Leka Trading\n",
      "Item:  Rössle Sauerkraut \n",
      "Supplier:  Plutzer Lebensmittelgroßmärkte AG\n"
     ]
    }
   ],
   "source": [
    "#Top ten most expensive items with their suppliers\n",
    "for item in expensive_things:\n",
    "    print('Item: ',item[0], '\\nSupplier: ', item[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "largest_category = \"\"\"\n",
    "SELECT Category.CategoryName, COUNT(Category.CategoryName)\n",
    "FROM Category, Product\n",
    "WHERE Product.CategoryID = Category.ID\n",
    "GROUP BY Category.CategoryName\n",
    "ORDER BY COUNT(Category.CategoryName) DESC\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "largest_category = cursor.execute(largest_category).fetchone()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Confections\n"
     ]
    }
   ],
   "source": [
    "#The largest category by number of products\n",
    "\n",
    "print(largest_category[0])"
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
