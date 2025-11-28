import requests
from typing import Dict

EFSTA_URL = "http://localhost:5618/"

def get_terminals() -> Dict[str, str]:
    response: requests.Response = requests.get(f'{EFSTA_URL}/cfg')
    return response.json()["Trm"]

def change_pos_serial_number(terminal_id: str, new_serial_number: str) -> None:
    payload = {
        "Cfg": {
            "Trm": {
                "TT": terminal_id,
                "Serial": new_serial_number,
            }
        }
    }

    requests.post(f'{EFSTA_URL}/cfg', json=payload)

if __name__ == "__main__":
    terminals: Dict[str, str] = get_terminals()
    print(terminals)

    change_pos_serial_number("1", "Hallo")

    terminals = get_terminals()
    print(terminals)