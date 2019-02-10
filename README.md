# Yo-setta Stone

A web application using NLP to create definitions for slang words based on context from tweets

Made with :heart: at HackBeanpot

## About

This application employs machine learning and natural language processing to evaluate the definition
of slang words based on the context of the tweets they are used in.
We pull tweets from the Twitter API that contain the word, and add them to our data set of sentences,
some of which do and others that do not include the word. With this data set, we create a word vector model
that maps out all of the words to representative vectors based on their relation to other words so that
they are easier to compare. From there, we do a vector comparison that finds the most similar vectors to that
of the input slang. We extract the words that the vectors represent to find synonyms of the input word, which
is then returned to the user on the front end.

## Development

To install dependencies, run:
```bash
$ pip install -r requirements.txt
```

To run the app, use the following command:
```bash
$ python main.py
```
By default, it will run on `http://127.0.0.1:5000/` locally.