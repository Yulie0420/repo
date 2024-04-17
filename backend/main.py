import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


Json = "..\calender-420408-d69c531cdeeb.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key("1fGeAwAFWFBKq4D05JmKj_XqQoHBQk18e58sluyDuWB8")
Sheets = Sheet.sheet1
# ----- fast api -----
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def getAllData():
    return Sheets.get_all_records()
class Info(BaseModel):
    id: int
    data: list
@app.post("/addNewEvents")
def getInformation(info: Info):
    Sheets.append_row(info.data)
    return {"status": "SUCCESS", "data": info}


