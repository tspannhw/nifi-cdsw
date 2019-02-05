from textblob import TextBlob

def sentiment(args):
  
  b = TextBlob(args["sentence"])
  result = b.sentiment

  return result
