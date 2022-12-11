#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn
from User import User

app = FastAPI()

@app.get('/')
async def root():
    return { 'Hi': 'World!' }

@app.get('/api/users/{username}')
async def show(username):
    return User.find_by_username(username)

if __name__ == '__main__':
    uvicorn.run("__init__:app", port=8080, log_level="info")

