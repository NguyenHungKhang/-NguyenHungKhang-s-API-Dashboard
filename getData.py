import requests
import json

url = "http://cads-api.fpt.vn/fiber-detection/v2/using_json_inf/2022/12"

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'EZQx4Knh8Bu8v6EpVaJkAmdKyBETjxIE'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

