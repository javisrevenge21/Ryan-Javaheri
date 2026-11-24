# The call agent, as LiveKit Cloud runs it.
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY agent.py prompt.txt ./
RUN python agent.py download-files
CMD ["python", "agent.py", "start"]
