# https://deepgo.cbrc.kaust.edu.sa/deepgo/api/create

import requests

BASE_URL_ENDPOINT = "https://deepgo.cbrc.kaust.edu.sa/deepgo/api/create"

def deepgo_predict(seq: str) -> list[dict]:
    payload = {
        "version": "1.0.21",
        "data_format": "enter",
        "data": seq,
        "threshold": 0.3
    }
    response = requests.post(BASE_URL_ENDPOINT, json=payload)

    # Going from predictions[0]/functions[2]"Molecular Function"/functions/* (getting all terms)
    return [{"goterm": x[0], "about": x[1], "score": x[2]} for x in response.json()["predictions"][0]["functions"][1]["functions"]]