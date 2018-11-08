from aylienapiclient import textapi
client = textapi.Client("0ca089d7", "741775d7f669f5fad9f56c5415166cda")
sentiment = client.Sentiment({'url': 'https://docs.google.com/document/d/1McysLYN49j0XadgKlkPiJA9JDDmFaDsbTpZ7oKdm3Ek/'})

print(sentiment)

sentimentPolarity = sentiment['polarity']
confidencePolarity = sentiment['polarity_confidence']
print(sentiment['polarity'], sentiment['polarity_confidence'])
