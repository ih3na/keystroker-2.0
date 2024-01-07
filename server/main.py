from fastapi import FastAPI, HTTPException, Request
import json
import uvicorn

app = FastAPI()

# File to store incoming data
FILE_NAME = "keyinputs.txt"

def read_file_async(filename):
    try:
        with open(filename, "r") as f:
            cont = f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No data available")

    # Prepare content
    log_data = cont.strip().split(",\n")
    return log_data

@app.post("/submit")
async def submit_data(reqest: Request):
    req_body = await reqest.body()
    req_body = req_body.decode("utf-8")

    # Write data into the file
    with open(FILE_NAME, "a") as f:
        f.write('{},\n'.format(req_body))
    
    return {"message":"Data recorded"}

@app.get("/data")
def get_data(request: Request):
    file_data = read_file_async(FILE_NAME)
    return file_data

if __name__ == "__main__":
    
    # Run the server
    uvicorn.run("main:app", host="127.0.0.1", port=6500, reload=True, workers=2)