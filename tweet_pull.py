import requests
import os
import json

#Use this if you want to set terminal envrionment to save bearer token
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHcWhAEAAAAAkLIhwxw5n86Z%2F9kXGd4j3U%2BYqQY%3DDqkOFob5P4RWa8Kgq8E2XiGyFx0u5oihSlCCBysoVxhKiWSZfz'

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:KDTrey5 -is:retweet)'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    # print(json.dumps(json_response, indent=0, sort_keys=True))
    # print(type(json_response))
    print(json_response["text"])

if __name__ == "__main__":
    main()
