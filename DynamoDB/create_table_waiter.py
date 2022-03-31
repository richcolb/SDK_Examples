import boto3


def createddbtable(name):
	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.create_table(
		TableName = name, 
		KeySchema=[
			{
				'AttributeName':'year','KeyType':'HASH'
			}
		], 

		AttributeDefinitions=[
			{
				'AttributeName':'year','AttributeType':'N'
			}
		],  
		ProvisionedThroughput={
            	'ReadCapacityUnits': 10,
            	'WriteCapacityUnits': 10
        	}
    	)

	table.meta.client.get_waiter('table_exists').wait(TableName = name) 
	print(table)

createddbtable("somethingorother23")