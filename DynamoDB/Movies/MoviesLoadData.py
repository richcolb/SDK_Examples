from decimal import Decimal
import json
import boto3


def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)


if __name__ == '__main__':
    with open("/home/ec2-user/environment/AWS_Python_SDK/AWS_Python_SDK_Examples/DynamoDB/Movies/moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)