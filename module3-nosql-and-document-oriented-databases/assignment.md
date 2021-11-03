Reproduce the live lecture task of setting up and
inserting the RPG data (specifically the `charactercreator_character`,
`charactercreator_character_inventory`, `armory_item`, and `armory_weapon`) into 
a MongoDB instance. Your documents in MongoDB should contain the character traits 
(name, lvel, etc.) and skills (strength, wisdom, etc.) and a list of their items. 
You should also store the weapons as a list in another key value pair (you will have 
duplicate items in both items and weapons) - see the example below.

Mongo document example:
```
mongo_document = {
  "name": <VALUE>,
  "level": <VALUE>,
  "exp": <VALUE>,
  "hp": <VALUE>,
  "strength": <VALUE>,
  "intelligence": <VALUE>,
  "dexterity": <VALUE>,
  "wisdom": <VALUE>,
  "items": [
    <ITEM NAME>,
    <ITEM NAME>
  ],
  "weapons" [
    <ITEM NAME>,
    <ITEM NAME>
  ]
}
```

Then answer the following question in your `README.md` file:
* How was working with MongoDB different from working with PostgreSQL?
* What was easier, and what was harder?

Please turn in the MongoDB python file you used to generate the documents as well as your `README.md`. It is suggested to then revisit the first two modules, rework/complete things as needed, and review the content with
fresh eyes the SQL approach. Compare and contrast, and come prepared to claass with questions  - the main topic will will discuss will be database differences and tradeoffs!