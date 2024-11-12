# Reddit Post Flair Analyzer

Finds posts for a specific subreddit that do not have flair.

## Usage

```sh
# Optional: virtualenv of your choosing
$ pyenv virtualenv reddit-flair-analyzer
$ pyenv activate reddit-flair-analyzer

# Install dependencies
$ pip install -r requirements.txt

# Clone & populate .env with your Reddit app ID & secret
$ cp .env.sample .env

# Run script
$ python main.py pics 10
created              flair    title
-------------------  -------  ----------------------------------------------------------------------------------------------------
2024-11-11 19:03:04           Red line path at Fushimi-Inari in Kyoto
2024-11-11 18:52:55           Wicked
2024-11-11 18:44:03           Dream
2024-11-11 18:35:18           My backyard shed this morning
2024-11-11 18:28:54           Beautiful walk through the wetlands park. Hard to believe this is in Las Vegas.
```
