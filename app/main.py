# Template Start FastAPI

# Imports
import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse

# Routers
from app.routes.helloworld.helloworld import router as helloworld_router

# Logging
logging.config.fileConfig(
    os.path.join(os.path.dirname(__file__), "config", "logging.conf"),
    disable_existing_loggers=False,
)

tags_metadata = [
    {
        "name": "Hello world",
        "description": "Template Endpoint",
    }
]

app = FastAPI(
    title="FastAPI Template",
    description="Template",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
)

# Routers
app.include_router(helloworld_router)


@app.get("/docs", include_in_schema=False)
async def get_documentation_swagger():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Template API Docs")


@app.get("/redoc", include_in_schema=False)
async def get_documentation_redoc():
    return get_redoc_html(openapi_url="/openapi.json", title="Template API Docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(
        title="Template API Docs",
        description="Template API Docs",
        version="0.0.1",
        routes=app.routes,
        tags=tags_metadata,
    )


@app.get("/", tags=["Docs"], include_in_schema=False)
async def get_docs():
    """
    Access to documentation in /docs
    """
    return RedirectResponse(url="/docs/")

# Main
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
