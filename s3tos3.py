import boto3



def lambda_handler(event, context):
    s3 = boto3.resource('s3')    
    s3_client = boto3.client('s3')
    bucket_to_copy = "from-bucket"
    new_bucket_name = "to-bucket"
    
    Request = context.aws_request_id
    directory_name = Request+".zip"+"/" #it's name of your folders
    s3_client.put_object(Bucket=new_bucket_name, Key=(directory_name+'/'))
  
  ## p.s i was using request id as file name here 
    
    for key in s3_client.list_objects(Bucket=bucket_to_copy)['Contents']:
        files = key['Key']
        print(files)
        copy_source = {'Bucket':bucket_to_copy,'Key': files}
        
        s3.meta.client.copy(copy_source, new_bucket_name,(directory_name+'/'))
        print(files)
    
        
   # for files in bucket_to_copy:
    #    print(files)
    #    new_bucket_name.copy(bucket_to_copy,files)    
