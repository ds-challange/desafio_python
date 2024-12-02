FROM --platform=linux/amd64 python:3.11.10

RUN apt-get update && apt-get install -y gcc unixodbc-dev gpg



# INSTALL POETRY 
RUN pip install poetry

WORKDIR /code
COPY ./pyproject.toml ./poetry.lock*  /code/

RUN mkdir -p /code/temp/data

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "python3", "-m", "src.main"]