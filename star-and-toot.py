import os
import time
from github import Github
from mastodon import Mastodon
import configparser
import tweepy

# Function to get config value from environment or config file
def get_config(section, key, default=None):
    env_key = f"{section.upper()}_{key.upper()}"
    return os.environ.get(env_key) or config.get(section, key, fallback=default)

# Parse the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Get GitHub access token
gh_token = get_config('GitHub', 'access_token')

# Create GitHub API instance
g = Github(gh_token)

# Get Mastodon API credentials
mastodon_token = get_config('Mastodon', 'access_token')
mastodon_api_base_url = get_config('Mastodon', 'api_base_url')
mastodon_client_id = get_config('Mastodon', 'client_id')
mastodon_client_secret = get_config('Mastodon', 'client_secret')

# Create Mastodon API instance
mastodon = Mastodon(
    client_id=mastodon_client_id,
    client_secret=mastodon_client_secret,
    access_token=mastodon_token,
    api_base_url=mastodon_api_base_url
)

# Check if Twitter is enabled
enable_twitter = get_config('Twitter', 'enable_twitter', 'false').lower() == 'true'

# Create Twitter API instance if enabled
if enable_twitter:
    consumer_key = get_config('Twitter', 'consumer_key')
    consumer_secret = get_config('Twitter', 'consumer_secret')
    access_token = get_config('Twitter', 'access_token')
    access_token_secret = get_config('Twitter', 'access_token_secret')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter = tweepy.API(auth)

# Get your user
user = g.get_user()

# Get list of currently starred repos
starred = [repo for repo in user.get_starred()]
print("You have starred", len(starred), "repositories.")

# Function to check for new starred repos
def check_for_new_starred_repos():
    global starred
    new_starred = [repo for repo in user.get_starred() if repo not in starred]
    if new_starred:
        print("You have starred", len(new_starred), "new repositories.")
        for repo in new_starred:
            message = f"I just starred a new repository on GitHub: {repo.html_url}"
            mastodon.status_post(message)
            if enable_twitter:
                twitter.update_status(message)  # optional Twitter functionality
        starred = user.get_starred()

# Periodically check for new starred repos
while True:
    check_for_new_starred_repos()
    time.sleep(60)  # wait for 60 seconds
