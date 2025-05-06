FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update && \
        apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir requests
COPY httpRequests.py .
EXPOSE 8000
CMD ["python3", "httpRequests.py"]
	
