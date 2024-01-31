import requests
import json

url = "http://192.168.1.16:8000//api/method/erpnext.accounts.doctype.sales_invoice.demo.sample"

payload = json.dumps({
  "data": {
    "status": "Overdue"
  }
})
headers = {
  'Authorization': 'token 7376cc581a48a6a:38bd3ecfae42f89',
  'Content-Type': 'application/json',
  'Cookie': 'full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)