import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt the user for the image URL
    url = input("🌍 Enter the image URL: ").strip()

    # Directory to store fetched images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Attempt to fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if HTTP request failed

        # Try to extract a filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename is found, generate one
        if not filename:
            filename = "image_fetched.jpg"

        # Create full file path
        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ The request timed out. Try again later.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Ubuntu-Inspired Image Fetcher 🌍")
    print('"I am because we are." – Embracing community through shared resources.\n')
    fetch_image()