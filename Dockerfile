# Build venv
FROM python:3.12-slim-buster as venv

ENV PYTHONPATH /home
ENV PORT 8080

COPY /app/requirements.txt ./app/

RUN python -m venv --copies /app/venv \
 && . /app/venv/bin/activate \
 && pip3 install --upgrade pip  \
 && pip3 install --no-cache-dir -r ./app/requirements.txt

# Build runtime with venv modules
FROM python:3.12-slim-buster as runtime

COPY --from=venv /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH

COPY .env /home

WORKDIR /home
COPY /app ./app/

# Ejecucion por default al iniciar el container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
