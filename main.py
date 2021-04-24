import requests

def zen():
    URL = "https://api.github.com/zen"
    r = requests.get(url = URL)
    #data = r.json()
    print(r.text)

def get_profile():
    URL = "https://api.github.com/users/defunkt"
    r = requests.get(url = URL)
    data = r.json()
    print(r.headers)
    #print(data)

def get_repo():
    URL = "https://api.github.com/repos/twbs/bootstrap"
    r = requests.get(url = URL)
    data = r.json()
    print(data)

def list_repos_of_a_user():
    URL = "https://api.github.com/users/octocat/repos"
    r = requests.get(url = URL)
    licznik = 0
    data = r.json()
    for repo in data:
        print(f"url: {repo['html_url']}")
        print(f"url: {repo['stargazers_count']}")
        licznik += repo['stargazers_count']
    print(f"licznik: {licznik}")

def list_repos_of_an_organization():
    URL = "https://api.github.com/orgs/octo-org/repos"
    r = requests.get(url = URL)
    data = r.json()
    print(data)

#authenticate to get 5000 requests per hour instead of 60
def main():
    #zen()
    #get_profile()
    #get_repo()
    list_repos_of_a_user()
    #list_repos_of_an_organization()
main()