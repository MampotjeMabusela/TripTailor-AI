from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["trip_tailor"]
customers = db["customers"]

def update_customer_profile(customer_id, itinerary):
    customers.update_one({"customer_id": customer_id}, {"$set": {"last_itinerary": itinerary}})
