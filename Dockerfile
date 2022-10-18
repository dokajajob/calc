FROM python:3.6-slim
MAINTAINER dokajajob@gmail.com
COPY . /calc
WORKDIR /calc
RUN pip install --no-cache-dir -r requirements.txt
RUN ["python3 -m pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null
