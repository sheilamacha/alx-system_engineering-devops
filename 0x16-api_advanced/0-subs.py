import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the API URL for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            # Subreddit not found
            return 0
        else:
            # Other error occurred
            return 0
    except requests.exceptions.RequestException:
        # Handle connection error
        return 0

# Example usage
subreddit_name = "funny"
subscribers = number_of_subscribers(subreddit_name)
if subscribers > 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
else:
    print(f"'{subreddit_name}' is not a valid subreddit.")
