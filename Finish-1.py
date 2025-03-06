import re  # Import the 're' module for regular expressions
import requests  # Import the 'requests' module for making HTTP requests

# Fetch the list of proxies from a GitHub repository
url = 'https://raw.githubusercontent.com/.../PROXY-List/refs/...s/master/http.txt'
response = requests.get(url).text  # Send a GET request and retrieve the text content

# Regex pattern to identify proxies (IP:Port format)
pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}')

# Extract proxies from the retrieved text using the regex pattern
proxies = pattern.findall(response)

# Open a file to save the proxies (mode 'a' for appending to the file)
with open('Proxies-1.txt', 'a') as o:
    for proxy in proxies:
        print(proxy)  # Display the proxy in the terminal
        o.write(proxy + '\n')  # Save the proxy to the file

print("\n✅ The list of proxies has been successfully extracted and saved to the file!")