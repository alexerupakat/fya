
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import requests
import cv2
import numpy as np
import base64

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    ai_backend_url = "http://ai-backend:8001/detect/"
    files = {"file": (file.filename, await file.read(), file.content_type)}
    response = requests.post(ai_backend_url, files=files)
    
    if response.status_code == 200:
        detections = response.json()["detections"]
        
        # Read image for drawing
        file.file.seek(0)
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        for detection in detections:
            box = detection['box']
            cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(img, f"{detection['class']}: {detection['confidence']:.2f}", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        # Encode image to base64 to display in browser
        _, buffer = cv2.imencode('.jpg', img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return templates.TemplateResponse("result.html", {"request": {}, "detections": detections, "image": img_base64})
    else:
        return JSONResponse(content={"error": "Failed to process image"}, status_code=response.status_code)
