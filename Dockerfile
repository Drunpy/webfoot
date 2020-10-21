FROM python3.8

COPY . ./webfoot

RUN apt-get update && apt-get upgrade
RUN apt-get install -y gcc python3-dev python3-setuptools
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt