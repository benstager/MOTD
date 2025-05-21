FROM python:3.11.9-slim

RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*
RUN curl -L https://github.com/tectonic-typesetting/tectonic/releases/latest/download/tectonic-x86_64-unknown-linux-gnu.tar.gz -o tectonic.tar.gz \
    && tar -xzf tectonic.tar.gz \
    && mv tectonic-x86_64-unknown-linux-gnu/tectonic /usr/local/bin/tectonic \
    && rm -rf tectonic-x86_64-unknown-linux-gnu tectonic.tar.gz

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
