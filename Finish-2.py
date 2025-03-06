import requests  # Import the 'requests' library for making HTTP requests
from bs4 import BeautifulSoup  # Import the 'BeautifulSoup' library for parsing HTML

# URL of the page containing the list of proxies
url = "https://free-proxy/"

# Send a GET request to fetch the content of the page
response = requests.get(url).text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')

# Find the `<div>` section that contains the list of proxies
proxies = soup.find('div', class_='modal-body')

# Check if the proxy section was found
if proxies:
    proxy_text = proxies.get_text()  # Extract the text inside the `<div>`
    proxy_lines = proxy_text.split("\n")[3:]  # Remove the first three lines (header and update date)

    # Display only the list of proxies in the terminal output
    for proxy in proxy_lines:
        if proxy.strip():  # Skip empty lines
            print(proxy)

    # Save the proxies to a file named `Proxies-2.txt`
    with open("Proxies-2.txt", "w") as f:
        f.write("\n".join(proxy_lines))  # Save the proxies line by line in the file
    
    print("\nSaved")  # Display a success message after saving

else:
    print("Error")  # Display an error message if the proxy section was not found