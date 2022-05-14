from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from server.routes.GPT import router as GPTRoutes
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(
    GPTRoutes, 
    tags=["GPT"], 
    prefix="/gpt"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="TechChallenge GPT API",
        version="0.2.0",
        description="OpenAPI schema for TechChallenge #01",
        routes=app.routes,
        openapi_version="3.0.2"
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST","PUT","DELETE", "OPTION", "GET"],
    allow_headers=["*"],
)