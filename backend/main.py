import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
Json = "..\calender-420408-cae890f2d3c7.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key("1fGeAwAFWFBKq4D05JmKj_XqQoHBQk18e58sluyDuWB8")
Sheets = Sheet.sheet1
# ----- fast api -----
app = FastAPI()
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

dataTitle = ["date", "time","events", "place"]
datas = ["03/11", "15:00", "dinner", "taipei"]
#先塞一筆假資料
Sheets.append_row(dataTitle)
Sheets.append_row(datas)
print("寫入成功")
print(Sheets.get_all_values())
