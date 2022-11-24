from fastapi import Response

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def modify_header(response:Response):
    response.headers["X-New-Header"] = "Hi, I'm a new header!"
    return {"msg":"Headers modified in response"}