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
	print("waiting for the {name} table to be created".format(name=name))
	table.meta.client.get_waiter('table_exists').wait(TableName = name) 
	print(table)

tableName = input("What is the table name: ")
createddbtable(tableName)