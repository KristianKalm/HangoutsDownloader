# Hangouts Image Downloader

## What does it do?

For some reason Google Takeout does not archive all images from Hangouts messages, it takes some selection of only your images.

Also all other workarounds in the do not seem to work anymore

This script downloads all attachments from Hangouts history.

## How to use

1. Download Hangouts history from [Google Takeout](https://takeout.google.com/settings/takeout)
2. Install [Python](https://www.python.org/downloads/)
3. Move ```start.py``` in same folder with ```Hangouts.json```
4. Run start ```./start.py```
5. Script will run and download all images under ```files``` folder