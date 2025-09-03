import requests

def book_trip(customer_id, itinerary):
    payload = {
        "customer_id": customer_id,
        "itinerary": itinerary,
        "status": "pending"
    }
    response = requests.post("https://api.bookingpartner.com/book", json=payload)
    return response.json()
