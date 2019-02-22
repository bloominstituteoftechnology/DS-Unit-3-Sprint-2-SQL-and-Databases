"""MongoDB queries for titanic database."""

import pymongo


if __name__ == "__main__":
    # Username and password to be set by user.
    username = "TODO"
    cluster = "TODO"
    password = "TODO"
    group = "TODO"

    # Create access to MondoDB rpg database.
    s = "mongodb+srv://{}:{}@{}-{}.mongodb.net/titanic".format(username,
                                                               password,
                                                               cluster,
                                                               group)
    client = pymongo.MongoClient(s)
    titanic_db = client["titanic"]

    outputs = {}

    # Find the count of passengers aboard titanic who survived/didn't survive.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "survived": "$Survived"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.survived",
                "count": "$count"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["survived_count"] = list(agg_res)

    # Find the count of passengers for each class aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "pclass": "$_id.pclass",
                "count": "$count"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass_count"] = list(agg_res)

    # Find the count of passengers for each class aboard titanic who
    # survived/didn't survive.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass",
                    "survived": "$Survived"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "pclass": "$_id.pclass",
                "survived": "$_id.survived",
                "count": "$count"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass+survived_count"] = list(agg_res)

    # Find the average age for those that survived/didn't survive the titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "survived": "$Survived"
                },
                "avgAge": {"$avg": {"$toDecimal": "$Age"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.survived",
                "avgAge": "$avgAge"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["survived_avg(age)"] = list(agg_res)

    # Find the average age for each class aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass"
                },
                "avgAge": {"$avg": {"$toDecimal": "$Age"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "pclass": "$_id.pclass",
                "avgAge": "$avgAge"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass_avg(age)"] = list(agg_res)

    # Find the average fare per passenger for those that survived/didn't
    # survive the titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "survived": "$Survived"
                },
                "avgFare": {"$avg": {"$toDecimal": "$Fare"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.survived",
                "avgFare": "$avgFare"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["survived_avg(fare)"] = list(agg_res)

    # Find the average number of siblings/spouses per passenger for each class
    # aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass"
                },
                "avgFare": {"$avg": {"$toDecimal": "$Fare"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "pclass": "$_id.pclass",
                "avgFare": "$avgFare"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass_avg(fare)"] = list(agg_res)

    # Find the average number of siblings/spouses per passenger for those that
    # survived/didn't survive the titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "survived": "$Survived"
                },
                "avgSibSpouse": {"$avg": {"$toInt": "$SiblingsSpousesAboard"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.survived",
                "avgSibSpouse": "$avgSibSpouse"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["survived_avg(sib_spouse)"] = list(agg_res)

    # Find the average number of siblings/spouses per passenger for each class
    # aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass"
                },
                "avgSibSpouse": {"$avg": {"$toInt": "$SiblingsSpousesAboard"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "pclass": "$_id.pclass",
                "avgSibSpouse": "$avgSibSpouse"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass_avg(sib_spouse)"] = list(agg_res)

    # Find the average number of parents/children per passenger for those that
    # survived/didn't survive the titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "survived": "$Survived"
                },
                "avgParChild": {"$avg": {"$toInt": "$ParentsChildrenAboard"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.survived",
                "avgParChild": "$avgParChild"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["survived_avg(par_child)"] = list(agg_res)

    # Find the average number of parents/children per passenger for each class
    # aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id":
                {
                    "pclass": "$Pclass"
                },
                "avgParChild": {"$avg": {"$toInt": "$ParentsChildrenAboard"}}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "survived": "$_id.pclass",
                "avgParChild": "$avgParChild"
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["pclass_avg(par_child)"] = list(agg_res)

    # Find the number of repeating names aboard titanic.
    agg_dict = [
        {
            "$group":
            {
                "_id": "$Name",
                "count": {"$sum": 1}
            }
        },
        {
            "$match":
            {
                "count": {"$gt": 1}
            }
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["matchName_count"] = len(list(agg_res))

    # Find number of couples aboard titanic.
    split_name = [{"$split": ["$Name", " "]}, 0]
    agg_dict = [
        {
            "$project":
            {
                "_id": 0,
                "Name": "$Name",
                "SiblingsSpousesAboard": {"$toInt": "$SiblingsSpousesAboard"}
            }
        },
        {
            "$match":
            {
                "SiblingsSpousesAboard": {"$gt": 0}
            }
        },
        {
            "$project":
            {
                "_id": 0,
                "Name": "$Name",
                "mr": {"$eq": [{"$arrayElemAt": split_name}, "Mr."]},
                "mrs": {"$eq": [{"$arrayElemAt": split_name}, "Mrs."]}
            }
        },
        {
            "$group":
            {
                "_id": {"$arrayElemAt": [{"$split": ["$Name", " "]}, -1]},
                "mr_count": {"$sum": {"$cond": ["$mr", 1, 0]}},
                "mrs_count": {"$sum": {"$cond": ["$mrs", 1, 0]}}
            }
        },
        {
            "$match":
            {
                "mr_count": {"$gt": 0},
                "mrs_count": {"$gt": 0}
            }
        },
        {
            "$count": "count"
        }
    ]
    agg_res = titanic_db["titanic"].aggregate(agg_dict)
    outputs["marriedCouple_count"] = list(agg_res)[0]["count"]

    # Print results.
    for o in outputs:
        print(o)
        print(outputs[o])
        print()
