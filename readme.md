
# Object Detection Microservice
## Prerequisites

- Docker
- Python 3.10 or higher

## Project Structure

fya/
├── ai-backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── yolov3/
│   ├── main.py
│   └── run.bat
├── ui-backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── main.py
│   └── run.bat
├── docker-compose.yml
└── readme.md

## Setup and Running the Application

### Using Docker

1.  **Run the application using Docker Compose:**

    bash
    docker-compose up --build
    

2.  **Access the application:**

    - Open web browser and navigate to `http://localhost:8000`.

### Without Docker (Local Setup)

1.  **Set up and run the AI backend:**
    *   Open a terminal or command prompt and navigate to the `fya/ai-backend` directory.
    *   Create a virtual environment: `python -m venv venv`
    *   Activate the virtual environment: `venv\Scripts\activate`
    *   Install the required packages: `pip install -r requirements.txt`
    *   Run the AI backend server: `run.bat`

2.  **Set up and run the UI backend:**
    *   Open another terminal or command prompt and navigate to the `fya/ui-backend` directory.
    *   Create a virtual environment: `python -m venv venv`
    *   Activate the virtual environment: `venv\Scripts\activate`
    *   Install the required packages: `pip install -r requirements.txt`
    *   Run the UI backend server: `run.bat`

3.  **Access the application:**
    *   Open web browser and navigate to `http://localhost:8000`.

## Usage

- Upload an image
- Application will display the image with bounding boxes and the corresponding JSON results.

## Output

- The output images with bounding boxes, JSON files will be saved in the `ui-backend/outputs` directory.
