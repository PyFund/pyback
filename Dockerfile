FROM python:3
RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install

CMD [ "/bin/bash" ]
