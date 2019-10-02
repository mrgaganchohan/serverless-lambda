import boto3

def hello(event, context):
  client = boto3.client('lambda')
  response = client.list_functions()
  return "romero"

def s3_thumbnail_generator(event,context):
  print ("event here is", event)
  return 1