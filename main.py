import requests
from environs import Env


def main():
    env = Env()
    env.read_env()
    dvmn_token = env.str("DVMN_TOKEN")

    url = "https://dvmn.org/api/long_polling/"
    headers = {"Authorization": dvmn_token}
    timestamp = None

    while True:
        try:
            payload = {"timestamp": timestamp}
            response = requests.get(
                url, headers=headers, params=payload, timeout=120
            )
            response.raise_for_status()
            server_answer = response.json()
            print(server_answer)
            if server_answer.get("timestamp_to_request"):
                timestamp = server_answer.get("timestamp_to_request")
            else:
                timestamp = server_answer.get("last_attempt_timestamp")
        except requests.exceptions.ReadTimeout:
            continue


if __name__ == "__main__":
    main()
