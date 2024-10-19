# Star and Toot

## GitHub Starred Repo Notifier for Mastodon

"Star and Toot" is a bot that monitors when you star new repositories on GitHub and posts a status update ("Toot") on your Mastodon account. As a secondary feature, it can also post to Twitter. However, we emphasize a Mastodon-first approach to microblogging in this project.

## Setup

1. Clone this repository.
2. Optionally, install the [uv](https://docs.astral.sh/uv/getting-started/installation/) project manager.
3. Install the necessary dependencies:

```
# using uv
uv sync --frozen

# or using pip
pip install -r requirements.txt
```

3. Obtain your GitHub Personal Access Token and Mastodon API Access Token.
4. Configure the bot using either environment variables or a config file.

### Generating a GitHub Personal Access Token

To generate a GitHub Personal Access Token:

1. Go to your [GitHub account settings](https://github.com/settings/profile).
2. Click on "Developer settings" in the left sidebar.
3. Select "Personal access tokens" and then "Fine-grained tokens".
4. Click "Generate new token".
5. Set the following details:
   - Token name: Give your token a descriptive name (e.g., "Star and Toot Bot")
   - Expiration: Choose an expiration date (or set to "No expiration" if you prefer)
   - Description: Optionally add a description of what this token is for
6. For "Resource owner", select your personal account.
7. Under "Repository access", select "All repositories" (or select specific repositories if you prefer).
8. In the "Permissions" section, set the following:
   - Repository permissions:
     - Metadata: Read-only
   - Account permissions:
     - Starring: Read-only
9. Click "Generate token" at the bottom of the page.
10. Copy the generated token immediately and store it securely. You won't be able to see it again!

### Obtaining Mastodon API Credentials

To obtain your Mastodon API credentials:

1. Log in to your Mastodon account.
2. Go to your account settings (usually found under Preferences or Settings).
3. Navigate to the "Development" or "Applications" section.
4. Click on "New Application" or "Create New Application".
5. Fill in the following details:
   - Application name: Give your app a name (e.g., "Star and Toot Bot")
   - Application website: You can use the GitHub repo URL or leave it blank
   - Redirect URI: Enter "urn:ietf:wg:oauth:2.0:oob" (this is for local/non-web apps)
   - Scopes: Select "write:statuses" (this allows posting toots)
6. Click "Submit" or "Create Application".
7. On the next page, click on your application's name to view its details. You will need:
   - Client key (also known as Client ID)
   - Client secret
   - Your access token

You'll need these credentials to configure the bot in the next step.

### Obtaining Twitter API Credentials

To obtain your Twitter API credentials:

1. Go to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and log in with your Twitter account.
2. Click on "Create an app".
3. Fill in the required fields and click on "Create".
4. On the next page, click on "Keys and tokens".
5. Copy the "API key" and "API secret key" to your config file.
6. On the same page, click on "Create" under "Access token & access token secret".
7. Copy the "Access token" and "Access token secret" to your config file.

### Configuring the Bot

Choose one of the following options to configure the bot:

#### Option A: Using Environment Variables

Set the following environment variables:

```
export GITHUB_ACCESS_TOKEN=your_github_token
export MASTODON_ACCESS_TOKEN=your_mastodon_access_token
export MASTODON_API_BASE_URL=https://your.mastodon.instance
export MASTODON_CLIENT_ID=your_client_id
export MASTODON_CLIENT_SECRET=your_client_secret
export TWITTER_ENABLE_TWITTER=false
export TWITTER_CONSUMER_KEY=your_consumer_key
export TWITTER_CONSUMER_SECRET=your_consumer_secret
export TWITTER_ACCESS_TOKEN=your_access_token
export TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

#### Option B: Using a Config File

Create a config.ini file in the project directory based on config_template.ini and add your GitHub and Mastodon API credentials:

```
[GitHub]
access_token = your_github_token

[Mastodon]
access_token = your_access_token_here
api_base_url = https://your.mastodon.instance
client_id = your_client_id_here
client_secret = your_client_secret_here

[Twitter]
enable_twitter = false
consumer_key = your_consumer_key
consumer_secret = your_consumer_secret
access_token = your_access_token
access_token_secret = your_access_token_secret
```

## Run the bot:

To run the bot locally in your terminal, use the following command:

```
uv run star-and-toot.py
```

or without using uv:

```
python star-and-toot.py
```

you can also build a docker container and run it from there:

```
docker build -t star-and-toot .

# run with environment variables
docker run -it --rm --name star-and-toot-bot \
  -e GITHUB_ACCESS_TOKEN=your_github_token \
  -e MASTODON_ACCESS_TOKEN=your_mastodon_token \
  -e MASTODON_API_BASE_URL=https://your.mastodon.instance \
  -e MASTODON_CLIENT_ID=your_client_id \
  -e MASTODON_CLIENT_SECRET=your_client_secret \
  star-and-toot

# run with config file
docker run -it --rm --name star-and-toot-bot \
  -v ./config.ini:/app/config.ini \
  star-and-toot
```

## Running as a systemd Service

If you are running this bot on a system with systemd, you can configure it as a service so it starts automatically on system boot. Follow these steps:

1. Create a systemd service file, e.g., star-and-toot.service. Service files are typically stored in /etc/systemd/system/:

```
sudo nano /etc/systemd/system/star-and-toot.service
```

2. In the service file, add the following content (replace user and /path/to/script with your actual username and the absolute path to your Python script):

```
[Unit]
Description=Star and Toot GitHub-Mastodon integration

[Service]
ExecStart=/usr/bin/python3 /path/to/star-and-toot.py
User=user
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Reload the systemd manager configuration:

```
sudo systemctl daemon-reload
```

4. Start the service:

```
sudo systemctl start star-and-toot.service
```

5. Enable the service to start on boot:

```
sudo systemctl enable star-and-toot.service
```

## Support

You can also tip the author with the following cryptocurrency addresses:

    Bitcoin: bc1q5grpa7ramcct4kjmwexfrh74dvjuw9wczn4w2f
    Monero: 85YxVz8Xd7sW1xSiyzUC5PNqSjYLYk4W8FMERVkvznR38jGTBEViWQSLCnzRYZjmxgUkUKGhxTt2JSFNpJuAqghQLhHgPS5
    PIVX: DS1CuBQkiidwwPhkfVfQAGUw4RTWPnBXVM
    Ethereum: 0x2a460d48ab404f191b14e9e0df05ee829cbf3733

## Connect
- [ChiefGyk3D's Mastodon Account](https://social.chiefgyk3d.com/@chiefgyk3d)
