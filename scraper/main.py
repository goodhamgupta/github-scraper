import json
import requests
import logging


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get("https://api.github.com/repos/knmnyn/ParsCit",headers=headers)
if r.status_code == 200:
    logging.error("Request successful")
    