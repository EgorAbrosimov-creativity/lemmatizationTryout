This repository contains code aimed to figure out which library is the best solution to some task (which authors would prefer to keep a secret). The main goal is to find the best way to bring words into some general form which is best used for some word embeddings. There are two approaches we want to test: lemmatization and stemming.

Among lemmatization solutions we've already found:<br>
  -PyMorphy2<br>
  -PyMystem3 - some unknown error<br>
  -NLTK Wordnet lemmatizer - will need some pos tagging, maybe later<br>
  -SpaCy - can't figure out how to use it<br>
  -RuLemma https://github.com/Koziev/rulemma <br>
  -TextBlob<br>
  -NLTK<br>
  -Pattern lemmatizer<br>
  -Stanford CoreNLP<br>
  -Gensim Lemmatize<br>
  -TreeTagger<br>
  -RNNmorph<br>
  -ipavlov (pos tagging)<br>
And stemming:<br>
  -Porter stemmer<br>
  -Lancaster stemmer<br>
  -Snowball stemmer<br>
