# Pexels Downloader

Pexels Downloader is a Python script that allows you to easily download videos from Pexels using the Pexels API. You can customize your search by modifying the query parameter.

## Installation

1. Clone this repository: `git clone https://github.com/votre-nom/pexels-downloader.git`
2. Navigate to the project directory: `cd pexels-downloader`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Get your Pexels API key by creating an account on [Pexels](https://www.pexels.com/api/).
2. Open the `config.py` file and replace `YOUR_API_KEY_HERE` with your actual API key.
3. Run the script: `python pexels_downloader.py --query "your search query"`
   - Replace "your search query" with your desired query. You can also modify the other optional parameters such as the number of videos to download and the output directory.
4. The script will download the videos to the specified output directory.
