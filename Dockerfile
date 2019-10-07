#to run this image:
#docker build -t my-python-app .
#docker run -e AWS_ACCESS_KEY_ID="anaccesskey" -e AWS_SECRET_ACCESS_KEY="asecretkey" -e AWS_DEFAULT_REGION="an_aws_region" -it --rm --name my-running-app my-python-app

FROM python:3.6.9-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip3 install boto3
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./script.py" ]