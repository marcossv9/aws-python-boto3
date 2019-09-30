#to run this image:
#docker build -t my-python-app .
#docker run -it --rm --name my-running-app my-python-app

FROM python:3.6.9-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip3 install boto3
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./script.py" ]