import boto3

client = boto3.client('comprehend')

sentiment = client.detect_sentiment(Text = "This product was rubbish - dont buy it!!!", LanguageCode = 'en') #API call for sentiment analysis
sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative
print(sentRes)
print(sentScore)

