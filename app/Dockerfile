# Build venv
FROM python:3.12.11-slim-bullseye AS venv

ENV PYTHONPATH /home
ENV PORT 8080

COPY requirements.txt ./

RUN python -m venv --copies /app/venv \
 && . /app/venv/bin/activate \
 && pip3 install --upgrade pip  \
 && pip3 install --no-cache-dir -r ./requirements.txt

# Build runtime with venv modules
FROM python:3.12.11-slim-bullseye AS runtime

COPY --from=venv /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH

WORKDIR /home
COPY . ./app/

# Ejecucion por default al iniciar el container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
