# Scanalot
## Scan online stores in South Africa for PS5 availability

The code in this repo is used to scrape online retailers sites to check for availability of PS5 Digital Edition stock. One or more users can be notified via email when one of five stores marks the item as not out of stock on their site. Only one email is sent per store. The scripts are meant to be run on a schedule.

#### Environment Variables

There are three required environment variables:

`SENDGRID_API_KEY` A valid SendGrid API key

`FROM_EMAIL` A valid SendGrid email address

`TO_EMAIL` A string containing the recipients email addresses. Multiple email addresses can be seperated by spaces.

## The code in this repository does **NOT** automatically purchase a PS5.
The purpose of this code is for me to practice webscraping.
