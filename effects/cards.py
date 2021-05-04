import pandas as pd

import requests

response = requests.get('https://docs.google.com/spreadsheets/d/1qm0ju-MwZ3R679wZO7F4Moom9AYwd6hbNjxb6goAYi8/export?format=csv&gid=263580445')
assert response.status_code == 200, 'Wrong status code'

#cards = pd.DataFrame.read_csv(response.content)

print(response.content)
