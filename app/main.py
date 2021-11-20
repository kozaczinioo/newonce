import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.spotify import spotify_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get():
    return {"status": "ok"}


app.include_router(spotify_router.router, prefix='/spotify')
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
