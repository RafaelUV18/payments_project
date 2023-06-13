import os

from fastapi import FastAPI, Depends, Request, Response
from routes.payments import payments_router


app = FastAPI(
    title='Accounts API',
    version='1.0.0',
    description='Service to manage payments'
)


try:
    modo = os.getenv('MOD_APP')
    if modo == "LOCAL":
        # quitar para produccion
        print("\nEjecutando modo local")
        @app.middleware("http")
        async def add_cors_header(request: Request, call_next):
            if request.method == "OPTIONS":
                return Response(content="ok",
                                headers={
                                    "Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Headers": "*",
                                    "Access-Control-Allow-Methods": "*"
                                })
            response = await call_next(request)
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Headers"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "*"
            return response
except Exception as ex:
    print("ocurrio un error al leer las variables de entorno")
    modo = "PRODUCCION"


@app.get('/')
def index():
    return 'Welcome to Accounts API'

@app.get('/health_Check')
async def health_check():
    """Verified if service is alive"""
    return {'success': True}


app.include_router(payments_router, prefix='/payments', tags=['Payments'])
