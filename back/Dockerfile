FROM python:3.8

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install

COPY *.py /app/

ENV GOOGLE_API_KEY=AIzaSyAfDWblz4k6q2QrPBEcZnWMlAKE56kqWdE

ENTRYPOINT ["pipenv", "run", "python"]
CMD ["server.py"]
