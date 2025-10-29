
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
