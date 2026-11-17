FROM python:3.12-slim
RUN pip install --no-cache-dir httpx==0.27.2 typer==0.12.5 click==8.1.7 rich==13.9.4
WORKDIR /app
COPY tools/ tools/
ENTRYPOINT ["python", "tools/cli.py"]
