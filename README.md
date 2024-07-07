# LANGUAGE IDENTIFIER

#### Language model developed for detecting/identifying language based on building language profiles from character ***N***-grams, where only 300 of the most frequent ***N***-grams were used for calculating the distance between their corresponding pairs during the process of comparing language profiles before the final classification.

The model was trained on large corpora of documents (30k lines of text for each of the 5 supported languages).
It supports the following languages:
- English
- German
- Slovene
- Spanish
- Croatian

Initial model testing on 25 different text documents (400 lines each) for each of the 5 languages showed a 100% accuracy of the model for all supported languages.
