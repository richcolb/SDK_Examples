<<<<<<< HEAD
mydict = {"fname":"richard","lname":"colborne","age":45,"height_cm":187}
=======
import boto3

client = boto3.client('comprehend')
print(type(client))

sentiment = client.detect_sentiment(Text = "This product was OK but I had a few issues with it", LanguageCode = 'en') #API call for sentiment analysis

print(sentiment["Sentiment"])
>>>>>>> dbba388202a0d6db9d2129921298ee4169f882b1

print(mydict["age"])