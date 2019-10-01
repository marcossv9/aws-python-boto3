
resource "aws_s3_bucket" "b" {
  bucket = "my-tf-bucket-msilva"
  acl    = "private"

  tags = {
    Name = "My bucket"
    Env  = "Prod"
  }
}