# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import testjson
# Instantiates a client
client = language.LanguageServiceClient()

avg_sentiment = 0 #hold average value of text sentiments
num_texts = 0 #hold number of texts considered (also iterator for while loop)

# The text to analyze

while num_texts < 25:# can also ask user for num of texts to analyze, though would need add'l variable
    text1 = testjson.gettext()
    num_texts = num_texts + 1
    #text = u"This is BIZARRE! Here's Joe Biden telling the story of his face-off with a gang of razor-wielding ne'er-do-wells led by a guy named 'Corn Pop.'"
    document = types.Document(
        content=text1,
        type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    avg_sentiment = (av_sentiment + sentiment) / num_texts

    print('Text: {}'.format(text1))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

print('The average sentiment is %d', avg_sentiment)
