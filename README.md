# LANGUAGE DETECTOR

Language model developed for detecting/identifying language based on building language profiles from character _n_-grams, where only 300 of the most frequent _n_-grams were used for calculating the distance between their corresponding pairs, while comparing language profiles before the final classification.

The model was trained on large corpora of documents (30k lines of text for each of the 5 supported languages &rarr; find large corpora [here](https://wortschatz.uni-leipzig.de/en/download/English)).
</br>

The model supports the following languages:

- English
- German
- Slovene
- Spanish
- Croatian

Initial model testing on 25 different text documents (400 lines each) for each of the 5 languages showed a 100% accuracy of the model for all supported languages.
