import requests

# API endpoint for random Chuck Norris Joke
url = 'https://api.chucknorris.io/jokes/random'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful(status code 200)

if response.status_code == 200:
    # parse json response
    data = response.json()

    # Extract the joke
    joke = data['value']  # the data retrieved  has a key called value

    # Display the joke

    print('Here is a chuck norris joke for you:')
    print(joke)

else:
    print('Error fetching Chuck Norris joke.Please try again later')
