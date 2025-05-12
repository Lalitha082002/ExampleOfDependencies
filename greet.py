# greet.py
import requests
def greet():
    response = requests.get("https://api.github.com")
    return f"Hello! GitHub API status: {response.status_code}"
if __name__ == "__main__":
    print(greet())
