# Scrapegraph-AI-Tool

Clone this repository:
`git clone `

change directory: 
`cd Scrapegraph-AI-Tool`

Create conda env:
`conda env create -f env.yaml`

Activate conda env:
`conda activate webscraper`

install some dependencies:
`sudo apt install chromium-chromedriver`
`playwright install-deps`
`sudo apt-get install libasound2`

Install ollama :
see docs at: https://ollama.com

pull LLM and Embeddings model:

`ollama pull mistral`
`ollama pull nomic-embed-text`

## Now you can run script:
`python3 scraper.py`
Enter prompt and link to the webpage you want to scrape and see the json output stored in the file that exist in the same directory.
