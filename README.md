# Scanalot

Scan online stores in South Africa for stock changes or availability using playwright.

## About the Project
Scanalot is designed to scrape online retailers' websites in South Africa to check for stock changes or availability. Users are notified via Pushover when one of the monitored stores has the item in stock. The scripts are intended to be run on a schedule using a github action.

## Getting Started

### Prerequisites
- Node.js and npm installed
- Valid Pushover API tokens

### Installation
1. Clone the repository:
```sh
git clone https://github.com/RatulMaharaj/scanalot.git
```

2. Install NPM packages:
```sh
cd scanalot
pnpm install
```

### Environment Variables

Create a `.env` file in the root of the project with the following variables:
```sh
PUSHOVER_USER_KEY=your_user_key
PUSHOVER_API_TOKEN=your_api_token
```


### Disclaimer

The code in this repository does NOT automatically purchase any items. The purpose of this code is for practicing web scraping. Please respect the terms of service of the websites you are scraping.

### License

Distributed under the MIT License. See `LICENSE` for more information.