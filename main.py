import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get('/name/{email}')
async def extract(email: str):
    url = 'https://www.ohio.edu/people-search?strQuery='
    try:
        page = requests.get(f"{url}{email}")
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_='search-result-name').text
        name =  results.split(':')[1].strip().replace("  "," ")
        return {'name' : name}
    except Exception:
        return {'messsage':'Not Found'}
        
@app.get("/")
def root():
    return {"message":"Resource not found"}