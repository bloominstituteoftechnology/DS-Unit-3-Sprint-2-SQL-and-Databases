---
layout: post
title:  Comparison
description: both databases suck but in different ways.  Mongodb is just a fight to get it to work in windows which sucks, and while SQL is a little better in that regard (and has more legible querying), it isnt so hot for me at least when it comes to creating tables.  I do like SQL a lot more though, so Im glad its more useful in our field.
---



some command line snippets(to show importing worked and queries are able to be ran):


C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection charactercreator_character --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_character.json
2019-02-20T19:54:54.043-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:54:54.501-0500    imported 174 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection armory_item --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\armory_item.json
2019-02-20T19:54:54.043-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:54:54.501-0500    imported 174 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection armory_weapon --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\armory_weapon.json
2019-02-20T19:55:16.699-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:55:17.160-0500    imported 37 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection charactercreator_character_inventory --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_character_inventory.json
2019-02-20T19:56:15.413-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:56:15.962-0500    imported 898 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection cleric --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\cleric.json
2019-02-20T19:57:13.324-0500    Failed: open C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\cleric.json: The system cannot find the file specified.
2019-02-20T19:57:13.325-0500    imported 0 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection cleric --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_cleric.json
2019-02-20T19:57:34.962-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:57:35.428-0500    imported 75 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection fighter --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_fighter.json
2019-02-20T19:57:56.093-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:57:56.542-0500    imported 68 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection mage --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_mage.json
2019-02-20T19:59:11.126-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:59:11.578-0500    imported 108 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection thief --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_thief.json
2019-02-20T19:59:31.646-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:59:32.167-0500    imported 51 documents

C:\WINDOWS\system32>mongoimport --host  cluster0-shard-00-00-3jido.mongodb.net:27017 --ssl -u veritaem -p 3ggDQnYixRa6eTaM --authenticationDatabase admin  --db rpg --collection necromancer --jsonArray --file C:\Users\Daricus\repos\veritaem\unit3sprint2\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\data\db\charactercreator_necromancer.json
2019-02-20T19:59:56.823-0500    connected to: cluster0-shard-00-00-3jido.mongodb.net:27017
2019-02-20T19:59:57.261-0500    imported 11 documents

C:\WINDOWS\system32>
