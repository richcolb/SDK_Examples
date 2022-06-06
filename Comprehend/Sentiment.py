import boto3

client = boto3.client('comprehend')
print(type(client))

sentiment = client.detect_sentiment(Text = "This product was OK but I had a few issues with it", LanguageCode = 'en') #API call for sentiment analysis

print(sentiment["Sentiment"])

