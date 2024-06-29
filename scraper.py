import json
from urllib.parse import urlparse
from scrapegraphai.graphs import SmartScraperGraph

# Prompt the user for input
user_prompt = input("Enter the prompt: ")
user_url = input("Enter the URL: ")

# Extract a suitable name from the URL
parsed_url = urlparse(user_url)
# Use the netloc and path to form a filename, replacing slashes with underscores
filename_part = parsed_url.netloc + parsed_url.path.replace("/", "_")
output_filename = f"{filename_part}.json"

# Graph configuration
graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://0.0.0.0:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://0.0.0.0:11434",  # set Ollama URL
    },
    "verbose": True,
}

# Create the SmartScraperGraph instance with user input
smart_scraper_graph = SmartScraperGraph(
    prompt=user_prompt,
    source=user_url,
    config=graph_config
)

# Run the graph and get the result
result = smart_scraper_graph.run()

# Print the result
print(result)

# Save the result to a JSON file
with open(output_filename, 'w') as outfile:
    json.dump(result, outfile, indent=4)

print(f"Output saved to {output_filename}")
