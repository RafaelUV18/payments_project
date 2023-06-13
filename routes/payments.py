from fastapi import APIRouter, File, UploadFile
from typing import List
import pandas as pd
from functions.dataframes import find_incorrect_values
from fastapi.responses import JSONResponse, StreamingResponse
from config.database import engine
from io import BytesIO

payments_router = APIRouter()
book=BytesIO()
writer = pd.ExcelWriter(book, engine='xlsxwriter')


@payments_router.post('/upload')
async def upload_payments(files: List[UploadFile] = File(...)):
    """EndPoint to upload files to database"""
    dataframe=pd.DataFrame()
    try:
        # Read files and search for errors
        for file in files:
            df_aux=pd.read_excel(file.file.read())
            found = find_incorrect_values(df_aux)
            if len(found) != 0:
                return JSONResponse(status_code=400,
                                    content={"detail": f"Errors in {file.filename} in {found}"})
            dataframe = pd.concat([dataframe, df_aux], ignore_index=True)
        # Upload to database
        res = dataframe.to_sql('payments', engine, if_exists='append', index=False, method='multi')
        return JSONResponse(status_code=201, content={'detail': f'{res} rows inserted'})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": e})


@payments_router.get('/get_all_json')
async def get_all_payments_in_json():
    """EndPoint to get all payments in json format"""
    try:
        query = 'SELECT * FROM payments'
        df = pd.read_sql(query, engine)
        result = df.to_dict(orient='records')
        return JSONResponse(status_code=200, content={'count':len(result), 'data': result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": e})
    

@payments_router.get('/get_all_file')
async def get_all_payments_in_a_file():
    """EndPoint to get all payments in excel file"""
    try:
        query = 'SELECT * FROM payments'
        df = pd.read_sql(query, engine)
        df.to_excel(writer, sheet_name='Payments', index=False)
        writer.close()
        book.seek(0)
        headers={
            'Content-Disposition': 'attachment; filename="payments.xlsx"'
        }
        return StreamingResponse(book,headers=headers)
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": e})


@payments_router.get('/get_total_amount')
async def get_total_amount():
    """EndPoint to obtain the total of payments"""
    try:
        query = 'SELECT SUM(Monto) FROM payments'
        cursor = engine.execute(query)
        result = cursor.fetchone()[0]
        return JSONResponse(status_code=200, content={'total_amount':result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": e})