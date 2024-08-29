# user_input.py

# Ask the user for their name
name = input("What is your name? ")
print(name)

# Ask the user for their age
age = input("How old are you? ")
print(age)
# Ask the user for their location
location = input("Where do you live? ")
print(location)
import requests

# Replace these with your details
token = 'YOUR_GITHUB_PERSONAL_ACCESS_TOKEN'
repo_to_fork = 'owner/repository'  # Format: 'owner/repository'
fork_url = f'https://api.github.com/repos/{repo_to_fork}/forks'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.post(fork_url, headers=headers)

if response.status_code == 202:
    print('Repository forked successfully!')
    forked_repo = response.json()
    print(f"Forked repository URL: {forked_repo['html_url']}")
else:
    print(f"Failed to fork repository. Status code: {response.status_code}")
    print(response.json())


