import boto3
import json
client = boto3.client('ce')
result = client.get_cost_and_usage(
    TimePeriod = {
        'Start': '2022-01-01',
        'End': '2022-02-01'
    },
    Granularity = 'MONTHLY',
    Metrics = ["UnblendedCost"],
    GroupBy = [
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        }
    ]
)

output = result['ResultsByTime'][0]['Groups']
costlist = []
for costs in output:
    costlist.append(float(costs['Metrics']['UnblendedCost']['Amount']))
    
total = sum(costlist)
total_int = (int(total))

print(total_int)
print(output)



    





