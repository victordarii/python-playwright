import requests
from data.models import User


def test_get_user():
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    # Ensure the request was successful
    assert response.status_code == 200

    # Parse the JSON response
    user_data = response.json()

    # Validate the response using the User model
    user = User(**user_data)

    # Assert that the user's name is 'Leanne Graham'
    assert user.name == "Leanne Graham"
