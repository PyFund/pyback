FROM python:3.8

LABEL maintainer="shawn.lin@gatech.edu"

ADD Pipfile /pyback/
ADD Pipfile.lock /pyback/
WORKDIR /pyback
RUN cat Pipfile
RUN pip install pipenv \
  && pipenv install --deploy --ignore-pipfile --dev

CMD [ "/bin/bash" ]
