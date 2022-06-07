from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['mydb']

collection = db['OPENLAB__Data']
print("Collection created........")

list_roads=[
    {"_id":1,"S": 'Green', 'red': 0,   'Green': 10, 'count':5},
    {"_id":2,"S": 'Red', 'red': 100, 'Green': 7,  'count':4},
    {"_id":3,"S": 'Red', 'red': 200, 'Green': 6,  'count':3},
    {"_id":4,"S": 'Red', 'red': 300, 'Green': 7,  'count':3}
]
collection.insert_many(list_roads)

while True:
    time.sleep(1)
    r1=collection.find_one({"_id":1})
    r2 = collection.find_one({"_id": 2})
    r3 = collection.find_one({"_id": 3})
    r4 = collection.find_one({"_id": 4})

    if r1['S'] == 'Green':
        if r1['Green'] == 1:
            collection.update_one({"_id": 1}, {"$set": {"S": 'Red'}})
            collection.update_one({"_id": 1}, {"$set": {"Green": (collection.find_one({"_id":1})['Green'])-1}})
            collection.update_one({"_id": 2}, {"$set": {"S": 'Green'}})
            collection.update_one({"_id": 1}, {"$set": {"red": (collection.find_one({"_id":2})['Green'])+(collection.find_one({"_id":3})['Green'])+(collection.find_one({"_id":4})['Green'])}})

        else:
            collection.update_one({"_id": 1}, {"$set": {"Green": (collection.find_one({"_id": 1})['Green']) - 1}})
        collection.update_one({"_id": 2}, {"$set": {"red": (collection.find_one({"_id": 2})['red']) - 1}})
        collection.update_one({"_id": 3}, {"$set": {"red": (collection.find_one({"_id": 3})['red']) - 1}})
        collection.update_one({"_id": 4}, {"$set": {"red": (collection.find_one({"_id": 4})['red']) - 1}})
    if r1['red'] <= 0:
        collection.update_one({"_id": 1}, {"$set": {'red': 5}})
        if (collection.find_one({"_id": 2})['S'] == 'Green'):
            collection.update_one({"_id": 1}, {"$set": {'red': collection.find_one({"_id": 2})['Green']}})
        if (collection.find_one({"_id": 3})['S'] == 'Green'):
            collection.update_one({"_id": 1}, {"$set": {'red': collection.find_one({"_id": 3})['Green']}})
        if (collection.find_one({"_id": 4})['S'] == 'Green'):
            collection.update_one({"_id": 1}, {"$set": {'red': collection.find_one({"_id": 4})['Green']}})
    if r2['S'] == 'Green':
        if r2['Green'] == 1:
            collection.update_one({"_id": 2}, {"$set": {"S": 'Red'}})
            collection.update_one({"_id": 2}, {"$set": {"Green": (collection.find_one({"_id":2})['Green'])-1}})
            collection.update_one({"_id": 3}, {"$set": {"S": 'Green'}})
            collection.update_one({"_id": 2}, {"$set": {"red": (collection.find_one({"_id":1})['Green'])+(collection.find_one({"_id":3})['Green'])+(collection.find_one({"_id":4})['Green'])}})
        else:
            collection.update_one({"_id": 2}, {"$set": {"Green": (collection.find_one({"_id": 2})['Green']) - 1}})
        collection.update_one({"_id": 1}, {"$set": {"red": (collection.find_one({"_id": 1})['red']) - 1}})
        collection.update_one({"_id": 3}, {"$set": {"red": (collection.find_one({"_id": 3})['red']) - 1}})
        collection.update_one({"_id": 4}, {"$set": {"red": (collection.find_one({"_id": 4})['red']) - 1}})
    if r2['red']<=0:
        collection.update_one({"_id": 2}, {"$set": {'red': 5}})
        if (collection.find_one({"_id":1})['S']=='Green') :
            collection.update_one({"_id": 2}, {"$set": {'red': collection.find_one({"_id":1})['Green']}} )
        if (collection.find_one({"_id":3})['S']=='Green') :
            collection.update_one({"_id": 2}, {"$set": {'red': collection.find_one({"_id":3})['Green']}} )
        if (collection.find_one({"_id":4})['S']=='Green') :
            collection.update_one({"_id": 2}, {"$set": {'red': collection.find_one({"_id":4})['Green']}} )


    if r3['S'] == 'Green':
        if r3['Green'] == 1:
            collection.update_one({"_id": 3}, {"$set": {"S": 'Red'}})
            collection.update_one({"_id": 3}, {"$set": {"Green": (collection.find_one({"_id":3})['Green'])-1}})
            collection.update_one({"_id": 4}, {"$set": {"S": 'Green'}})
            collection.update_one({"_id": 3}, {"$set": {"red": (collection.find_one({"_id":1})['Green'])+(collection.find_one({"_id":2})['Green'])+(collection.find_one({"_id":4})['Green'])}})
        else:
            collection.update_one({"_id": 3}, {"$set": {"Green": (collection.find_one({"_id": 3})['Green']) - 1}})
        collection.update_one({"_id": 1}, {"$set": {"red": (collection.find_one({"_id": 1})['red']) - 1}})
        collection.update_one({"_id": 2}, {"$set": {"red": (collection.find_one({"_id": 2})['red']) - 1}})
        collection.update_one({"_id": 4}, {"$set": {"red": (collection.find_one({"_id": 4})['red']) - 1}})
    if r3['red']<=0:
        collection.update_one({"_id": 3}, {"$set": {'red': 5}})
        if (collection.find_one({"_id":1})['S']=='Green') :
            collection.update_one({"_id": 3}, {"$set": {'red': collection.find_one({"_id":1})['Green']}} )
        if (collection.find_one({"_id":2})['S']=='Green') :
            collection.update_one({"_id": 3}, {"$set": {'red': collection.find_one({"_id":2})['Green']}} )
        if (collection.find_one({"_id":4})['S']=='Green') :
            collection.update_one({"_id": 3}, {"$set": {'red': collection.find_one({"_id":4})['Green']}} )

    if r4['S'] == 'Green':
        if r4['Green'] <= 1:
            collection.update_one({"_id": 4}, {"$set": {"S": 'Red'}})
            collection.update_one({"_id": 4}, {"$set": {"Green": (collection.find_one({"_id":4})['Green'])-1}})
            collection.update_one({"_id": 1}, {"$set": {"S": 'Green'}})
            collection.update_one({"_id": 4}, {"$set": {"red": (collection.find_one({"_id":1})['Green'])+(collection.find_one({"_id":2})['Green'])+(collection.find_one({"_id":3})['Green'])}})
        else:
            collection.update_one({"_id": 4}, {"$set": {"Green": (collection.find_one({"_id": 4})['Green']) - 1}})
        collection.update_one({"_id": 1}, {"$set": {"red": (collection.find_one({"_id": 1})['red']) - 1}})
        collection.update_one({"_id": 2}, {"$set": {"red": (collection.find_one({"_id": 2})['red']) - 1}})
        collection.update_one({"_id": 3}, {"$set": {"red": (collection.find_one({"_id": 3})['red']) - 1}})

    if r4['red']<=0:
        collection.update_one({"_id": 4}, {"$set": {'red': 5}})
        if (collection.find_one({"_id":1})['S']=='Green') :
            collection.update_one({"_id": 4}, {"$set": {'red': collection.find_one({"_id":1})['Green']}} )
        if (collection.find_one({"_id":3})['S']=='Green') :
            collection.update_one({"_id": 4}, {"$set": {'red': collection.find_one({"_id":3})['Green']}} )
        if (collection.find_one({"_id":2})['S']=='Green') :
            collection.update_one({"_id": 4}, {"$set": {'red': collection.find_one({"_id":2})['Green']}} )


    print(collection.find_one({"_id":1}))
    print(collection.find_one({"_id":2}))
    print(collection.find_one({"_id":3}))
    print(collection.find_one({"_id":4}))

    print("\n")

