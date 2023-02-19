FROM python:3.11-slim

RUN python -m pip install --upgrade pip

COPY ./src ./app

WORKDIR /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]