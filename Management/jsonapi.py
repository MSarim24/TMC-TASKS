import requests
import pandas as pd

data1 = {
    "id" : [],
    "title" : [],
    "body" : [],
    "userId" : [],
}

try:
    x= int(input("Enter how many rows: "))

    for i in range(1,x+1):
        url = f'https://jsonplaceholder.typicode.com/posts/{i}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        data1["id"].append(data["id"])
        data1["title"].append(data["title"])
        data1["body"].append(data["body"])
        data1["userId"].append(data["userId"])
        
    df = pd.DataFrame(data1)
    print(df)
    print(df.iloc[0:3])
    df.to_excel("student.xlsx",index=False)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")