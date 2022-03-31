import boto3

tableName = input("Enter the table name : ")
partitionKey = input("Enter the  Partition Key: ")
sortKey = input("Enter the Sort Key: ")

def create_table(table, partition, sort):
    
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName=table,
        KeySchema=[
            {
                'AttributeName': partition,
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': sort,
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': partition,
                'AttributeType': 'S'
            },
            {
                'AttributeName': sort,
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table
    
if __name__ == '__main__':
    music_table = create_table(tableName, partitionKey, sortKey)
    print("Table status:", music_table.table_status)
    






