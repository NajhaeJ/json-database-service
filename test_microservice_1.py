import requests

send_response = requests.post(
    "http://127.0.0.1:5000/send_user_data",
    json={
        "key": "test_user",
        "data": {
            "email": "test@example.com",
            "role": "student"
        }
    }
)

print("SEND RESPONSE:")
print(send_response.json())


get_response = requests.post(
    "http://127.0.0.1:5000/get_user_data",
    json={
        "key": "test_user"
    }
)

print("\nGET RESPONSE:")
print(get_response.json())


bad_response = requests.post(
    "http://127.0.0.1:5000/get_user_data",
    data="not json"
)

print("\nBAD REQUEST RESPONSE:")
print(bad_response.json())