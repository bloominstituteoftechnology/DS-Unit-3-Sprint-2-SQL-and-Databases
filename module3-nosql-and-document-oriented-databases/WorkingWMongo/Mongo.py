import pymongo
password = 'suh264tUm'
dbname = 'test'
connection = ('mongodb+srv://jonatan5696:' + password +
              '@cluster0.jalzo.gcp.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient(connection)
db = client.test
print(db)
print('\n')
curs = db.test.find({'x': 1})
print(f'list of curs is, {list(curs)}\n')

# Let's add some more interesting documents

byrnes_doc = {
    'animal': 'manatee',
    'color': 'green',
    'number': 7
}

daves_doc = {
    'animal': 'bat',
    'color': 'red',
    'number': 1000
}

sasanas_doc = {
    'animal': 'orca',
    'color': 'blue',
    'number': 9
}

tylers_doc = {
    'animal': 'hippogryph',
    'cities': ['New York', 'Houston']
}

walters_doc = {
    'color': 'chartreuse',
    'animal': 'platypus'
}

aarons_doc = {
    'inner_dict': {
        'x': 2,
        'y': -4,
        'z': 'banana'
    },
    'another_key': (2, 6, 3)
}

# Let's put them all in a list for convenience
#all_docs = [byrnes_doc, daves_doc, sasanas_doc, tylers_doc, walters_doc,
            aarons_doc]

print(f'len of docs {len(all_docs)}\n')

# Insert Documents Back Into Data Base
db.test.insert_many(all_docs)

# db.test.insert_one({
#     'animal': 'tiger',
#     'color': 'green',
#     'city': 'Paris'
# })

# Look for Documents
print(f'looking for docs: {list(db.test.find())}')

print('not in list form', db.test.find_one({'color': 'green'}))
print('in list form', list(db.test.find({'color': 'green'})))

more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)
