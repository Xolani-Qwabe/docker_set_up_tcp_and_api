import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"NBA": "INTEL"}

if __name__ == '__main__':
    #configure network app to listen on all available network interfaces on the local machine
    uvicorn.run(app, host='0.0.0.0', port=8000)