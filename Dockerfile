FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    pkg-config \
    gcc \
    g++

WORKDIR app 

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD models models
ADD src src


EXPOSE 5000

# Start the server
CMD ["python", "src/app.py"]
