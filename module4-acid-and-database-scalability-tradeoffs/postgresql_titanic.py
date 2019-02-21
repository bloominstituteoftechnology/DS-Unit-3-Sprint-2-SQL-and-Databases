"""Import data from titanic.csv file to PostgreSQL database."""

import psycopg2


def find_str_titanic(selec="*", selec_type="COUNT", add_selec="", group="",
                     from_table="titanic"):
    """Creates SQL string for finding selection from PostgreSQL database.
    Args:
        selec (str): column to select
        selec_type (str): modifier to selec [i.e. selec_type(selec)]
        add_selec (str): additional selections without selec_str
        group (str): column to group results by
    Returns:
        (str): SQL query string for PostgreSQL database"""
    selec_str = ""
    if selec_type == "":
        selec_str = selec
    else:
        selec_str = "{}({})".format(selec_type, selec)
    if add_selec != "":
        selec_str = "{}, {}".format(add_selec, selec_str)
    group_str = ""
    if group != "":
        group_str = " GROUP BY ({})".format(group)
    return "SELECT {} FROM {}{};".format(selec_str, from_table, group_str)


def run_str(cur, exec_str):
    """Executes SQL query string and fetches all results from PostgreSQL
    database.
    Args:
        cur (psycopg2.extensions.cursor): cursor to PostgreSQL database
        exec_str (str): SQL string to execute
    Returns:
        (str): SQL query string for PostgreSQL database"""
    cur.execute(exec_str)
    return cur.fetchall()


if __name__ == "__main__":
    # Username and password to be set by user.
    username = "TODO"
    db_name = "TODO"
    password = "TODO"
    host = "TODO"

    # Connect to titanic database.
    conn = psycopg2.connect(host=host, dbname=db_name,
                            user=username, password=password)
    cur = conn.cursor()

    outputs = {}

    # Find the count of passengers aboard titanic who survived/didn't survive.
    # Returns list of tuples (survived, COUNT(*)).
    find_str = find_str_titanic(add_selec="survived", group="survived")
    outputs["COUNT survived"] = run_str(cur, find_str)

    # Find the count of passengers for each class aboard titanic.
    # Returns list of tuples (pclass, COUNT(*)).
    find_str = find_str_titanic(add_selec="pclass", group="pclass")
    outputs["COUNT pclass"] = run_str(cur, find_str)

    # Find the count of passengers for each class aboard titanic who
    # survived/didn't survive.
    # Returns list of tuples (pclass, survived, COUNT(*)).
    find_str = find_str_titanic(add_selec="pclass, survived",
                                group="pclass, survived")
    outputs["COUNT pclass, survived"] = run_str(cur, find_str)

    # Find the average age for those that survived/didn't survive the titanic.
    # Returns list of tuples (survived, AVG(age)).
    find_str = find_str_titanic(selec="age", selec_type="AVG",
                                add_selec="survived", group="survived")
    outputs["AVG(age) survived"] = run_str(cur, find_str)

    # Find the average age for each class aboard titanic.
    # Returns list of tuples (pclass, AVG(age)).
    find_str = find_str_titanic(selec="age", selec_type="AVG",
                                add_selec="pclass", group="pclass")
    outputs["AVG(age) pclass"] = run_str(cur, find_str)

    # Find the average fare per passenger for those that survived/didn't
    # survive the titanic.
    # Returns list of tuples (survived, AVG(fare)).
    find_str = find_str_titanic(selec="fare", selec_type="AVG",
                                add_selec="survived", group="survived")
    outputs["AVG(fare) survived"] = run_str(cur, find_str)

    # Find the average number of siblings/spouses per passenger for each class
    # aboard titanic.
    # Returns list of tuples (pclass, AVG(siblings_spouses)).
    find_str = find_str_titanic(selec="fare", selec_type="AVG",
                                add_selec="pclass", group="pclass")
    outputs["AVG(fare) pclass"] = run_str(cur, find_str)

    # Find the average number of siblings/spouses per passenger for those that
    # survived/didn't survive the titanic.
    # Returns list of tuples (survived, AVG(siblings_spouses)).
    find_str = find_str_titanic(selec="siblings_spouses", selec_type="AVG",
                                add_selec="survived", group="survived")
    outputs["AVG(siblings_spouses) survived"] = run_str(cur, find_str)

    # Find the average number of siblings/spouses per passenger for each class
    # aboard titanic.
    # Returns list of tuples (pclass, AVG(siblings_spouses)).
    find_str = find_str_titanic(selec="siblings_spouses", selec_type="AVG",
                                add_selec="pclass", group="pclass")
    outputs["AVG(siblings_spouses) pclass"] = run_str(cur, find_str)

    # Find the average number of parents/children per passenger for those that
    # survived/didn't survive the titanic.
    # Returns list of tuples (pclass, AVG(parents_children)).
    find_str = find_str_titanic(selec="parents_children", selec_type="AVG",
                                add_selec="survived", group="survived")
    outputs["AVG(parents_children) survived"] = run_str(cur, find_str)

    # Find the average number of parents/children per passenger for each class
    # aboard titanic.
    # Returns list of tuples (pclass, AVG(parents_children)).
    find_str = find_str_titanic(selec="parents_children", selec_type="AVG",
                                add_selec="pclass", group="pclass")
    outputs["AVG(parents_children) pclass"] = run_str(cur, find_str)

    # Find the number of repeating names aboard titanic.
    # Returns number of repeating names as int.
    find_str = """SELECT COUNT(*) FROM (
        SELECT name, COUNT(*)
        FROM titanic
        GROUP BY name
        HAVING COUNT(*) > 1
    ) AS dist_names
    """
    outputs["COUNT(repeating_names)"] = run_str(cur, find_str)[0][0]

    # Find number of couples aboard titanic.
    # Returns number of couples as int.
    find_str = """SELECT COUNT(*)
                FROM (
                        SELECT l_name,
                            COUNT(husb = TRUE) AS mr_count,
                            COUNT(wife = TRUE) AS mrs_count
                        FROM (
                            SELECT reverse(split_part(reverse(name), ' ', 1))
                                    AS l_name,
                                split_part(name, ' ', 1) = 'Mr.' AS husb,
                                split_part(name, ' ', 1) = 'Mrs.' AS wife
                            FROM titanic
                            WHERE siblings_spouses > 1
                        ) AS family_info
                        GROUP BY l_name
                ) AS poss_couples
                WHERE (
                    (mr_count > 1 and mrs_count > 1)
                )"""
    outputs["COUNT(couples)"] = run_str(cur, find_str)[0][0]

    # Print results.
    for o in outputs:
        print(o)
        print(outputs[o])
        print()
