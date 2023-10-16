import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["comp467"]

# "collection" = table
# "document" = record

# database and collection won't be created until you add a document!!!
# uncomment the below lines once you've done that:

# print(mongo_client.list_database_names())
# dblist = mongo_client.list_database_names()
# if "comp467" in dblist: print("the db exists")

test_collection = db["halloween_films"]

document_list = [
    {"title": "Son of Godzilla", "platform": "YouTube"},
    {"title": "The Old Dark House", "platform": "Plex"},
    {"title": "The Abominable Dr. Phibes", "platform": "YouTube"},
    {"title": "White Zombie", "platform": "Plex"},
    {"title": "An American Werewolf in London", "platform": "Netflix"}
]

results = test_collection.insert_many(document_list)

print(f"collections: {mongo_client.list_database_names()}")
print(f"inserted documents: {results.inserted_ids}")