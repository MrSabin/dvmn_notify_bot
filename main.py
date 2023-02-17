import requests
from environs import Env

def main():
    env = Env()
    env.read_env()
    dvmn_token = env.str("DVMN_TOKEN")

    url = "https://dvmn.org/api/user_reviews/"
    headers = {"Authorization": dvmn_token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    main()
    