import boto3

s3 = boto3.client('s3')

resp = s3.select_object_content(
    Bucket='richcolb-select',
    Key='2021-06-thames-valley-street.csv',
    ExpressionType='SQL',
    Expression="SELECT * FROM s3object s where s.\"Crime type\" = 'Bicycle theft'",
    InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
    OutputSerialization = {'CSV': {}},
)

for event in resp['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
        print("Stats details bytesReturned: ")
        print(statsDetails['BytesReturned'])
