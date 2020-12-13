FROM python:3.8

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install

COPY *.py /app/

ENTRYPOINT ["pipenv", "run", "python"]
CMD ["server.py"]