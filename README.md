# Flugel

This is a python3 script developed using boto3, an AWS SDK to interact with AWS resources. Also you will find a terraform files to create infrastructure on AWS and test the python script.

* Purpose: The tool input is a list of tags and it returns the list of EC2 instances and S3 buckets that don't match any of the tags in the N. Virginia region.

## Requisites

### Install Docker, Docker-Compose, Terraform and AWSCLI

* Docker
  * `curl -fsSL https://get.docker.com -o get-docker.sh`
  * `sudo sh get-docker.sh`
  * `sudo usermod -aG docker $USER`

* Docker-Compose
  * `sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
  * `sudo chmod +x /usr/local/bin/docker-compose`

* Terraform
  * `wget https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip`
  * `sudo unzip ./terraform_0.11.13_linux_amd64.zip -d /usr/local/bin/`

* AWS CLI
  * `curl -O https://bootstrap.pypa.io/get-pip.py`
  * `python3 get-pip.py --user`
  * `pip3 install awscli --upgrade --user`
  * `aws --version` To validate if the installation was successful.

* Configure the AWS CLI to run Terraform in next steps:
  * Execute the command `aws configure` and complete with your keys:

  > AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE

  > AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

  > Default region name [None]: us-east-1

  > Default output format [None]: json

NOTE: If you don't have python3 installed use this [link](https://docs.aws.amazon.com/cli/latest/userguide/install-linux-python.html) to install it.

## Quick Start

Next steps will guide you to run three things:

- Export AWS Keys
- Create infrastructure in AWS using Terraform
- Run script in Docker/Docker-Compose
- Delete infrastructure created with Terraform in AWS

### Export AWS Account Keys

To export AWS variables use:

 * `export AWS_ACCESS_KEY_ID="anaccesskey"`
 * `export AWS_SECRET_ACCESS_KEY="asecretkey"`
 * `export AWS_DEFAULT_REGION="us-east-1"`

NOTE: You will need to export the above variables in order to get Terraform working in the next step.

### Create Infrastructure

Run following commands in order to create AWS infrastructure using Terraform:

 * `terraform init`
 * `terraform plan`
 * `terraform apply`

### Run Docker/Docker-Compose to execute the script

 * To run with Docker
  * Build image: `docker build -t my-python-app .`
  * Run image: `docker run -e AWS_ACCESS_KEY_ID="anaccesskey" -e AWS_SECRET_ACCESS_KEY="asecretkey" -e AWS_DEFAULT_REGION="an_aws_region" -it --rm --name my-running-app my-python-app`

 * To run with Docker-Compose
 
NOTE: First complete the environment variables in docker-compose using your AWS Account Keys

  * Build: `docker-compose build --force-rm`
  * Run: `docker-compose run`

### Delete infrastructure in AWS

To delete the infrastructure created with Terraform run:

 * `terraform destroy`

## Run Automated Tests to the script

*Soon*