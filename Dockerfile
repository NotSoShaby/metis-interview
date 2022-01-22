FROM python:3.9.5
RUN apt-get update && \
      apt-get -y install sudo
RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
RUN echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main" | sudo tee /etc/apt/sources.list.d/mssql-release.list
RUN sudo apt-get install unixodbc-dev --yes
RUN sudo apt-get install libodbc1 odbcinst1debian2
RUN sudo apt-get update
RUN sudo ACCEPT_EULA=Y apt-get install msodbcsql17 --yes
ENV PYTHONUNBUFFERED 1
ENV PIPENV_INSTALL_TIMEOUT 9000
RUN mkdir /code
RUN cd /code
RUN pip install pipenv
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install --system --deploy
ADD MetisInterview /code/MetisInterview
WORKDIR /code/MetisInterview
