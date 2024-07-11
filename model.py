from typing import List, Dict
from enum import Enum
import re
import sys


class CorpusLanguage(Enum):
    EN = 1
    SI = 2
    DE = 3
    ES = 4
    HR = 5


def read_corpus(filename: str) -> str:
        with open(filename, "r", encoding="utf-8") as en_corpus:
            corpus: str = en_corpus.read()
        en_corpus.close()
        return corpus


def get_lexemes(corpus: str) -> List[str]:
    # keep language specific special letters
    cleaned_corpus: str = re.sub(r'[^a-zA-ZÄäÖöÜüßČčŠšŽžáéíóúüñĆćĐđ\s]', '', corpus)
    lexemes: List[str] = list(cleaned_corpus)
    lexemes = [' ' + lexem + ' ' for lexem in lexemes]
    return lexemes


def build_ngrams(lexemes: List[str], n: int) -> Dict[str, int]:
    ngrams: Dict[str, int] = {}
    for i in range(len(lexemes) - n + 1):
        ngram = tuple(lexemes[i:i+n])
        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1
    return ngrams


def sort_ngrams(all_ngrams: Dict[str, int]) -> Dict[str, int]:
    # sort all different n-grams descendingly by the number of their occurrences
    sorted_ngrams: Dict[str, int] = sorted(all_ngrams.items(), key=lambda x: x[1], reverse=True)

    # keep only the 300 most frequent n-grams
    top_300_ngrams: Dict[str, int] = dict(sorted_ngrams[:300])

    return top_300_ngrams


# save language profiles to files for reusage
def save_language_profile(language_profile: Dict[str, int], filename: str) -> None:
    match filename[0:2]:
        case "en":
            print("saving English language profile...")
        case "de":
            print("saving German language profile...")
        case "si":
            print("saving Slovene language profile...")        
        case "es":
            print("saving Spanish language profile...")        
        case "hr":
            print("saving Croatian language profile...")

    # convert entire language profile to a single string
    language_profile_str: str = '\n'.join([f"{key}: {value}" for key, value in language_profile.items()])
    # save language profile string to file
    with open(f"language_profiles/{filename}", 'w', encoding='utf8') as language_profile_file:
        language_profile_file.write(language_profile_str)
    language_profile_file.close()


def read_language_profile(filename: str) -> Dict[str, int]:
    match filename[0:2]:
        case "en":
            print("loading English language profile...")
        case "de":
            print("loading German language profile...")
        case "si":
            print("loading Slovene language profile...")        
        case "es":
            print("loading Spanish language profile...")        
        case "hr":
            print("loading Croatian language profile...")
    
    # read language profile from file to a single string
    with open(f"language_profiles/{filename}", 'r') as language_profile_file:
        profile: str = language_profile_file.read()
    language_profile_file.close()

    # split string by new line characters
    language_profile: List[str] = profile.split('\n')

    # convert language profile string to dictionary
    loaded_profile: Dict[str, int] = {}
    for line in language_profile:
        # extract key-value pairs
        key, value = line.strip().split(': ')
        key = tuple(part.strip()[1:-1] for part in key[1:-1].split(',') if part.strip())
        value = int(value)
        loaded_profile[key] = value

    return loaded_profile


def train_language(lang: CorpusLanguage) -> Dict[str, int]:
    match lang:
        case CorpusLanguage.EN:
            print("training model on English corpus...")

            # train model on English corpus
            corpus: str = read_corpus("train_data/en_corpus.txt")
            lexemes: List[str] = get_lexemes(corpus)

            # generate 1 to 5-grams
            all_ngrams: Dict[str, int] = {}
            for i in range(1, 6):
                ngrams: Dict[str, int] = build_ngrams(lexemes, i)
                all_ngrams.update(ngrams)

            # build English language profile from n-grams
            en_lang_profile: Dict[str, int] = sort_ngrams(all_ngrams)
            #for ngram in en_lang_profile:
            #    print(f"{ngram} --> {en_lang_profile[ngram]}\n")

            return en_lang_profile
        

        case CorpusLanguage.DE:
            print("training model on German corpus...")

            # train model on German corpus
            corpus: str = read_corpus("train_data/de_corpus.txt")
            lexemes: List[str] = get_lexemes(corpus)

            # generate 1 to 5-grams
            all_ngrams: Dict[str, int] = {}
            for i in range(1, 6):
                ngrams: Dict[str, int] = build_ngrams(lexemes, i)
                all_ngrams.update(ngrams)

            # build German language profile from n-grams
            de_lang_profile: Dict[str, int] = sort_ngrams(all_ngrams)
            #for ngram in de_lang_profile:
            #    print(f"{ngram} --> {de_lang_profile[ngram]}\n")
            
            return de_lang_profile

        
        case CorpusLanguage.SI:
            print("training model on Slovene corpus...")

            # train model on Slovene corpus
            corpus: str = read_corpus("train_data/si_corpus.txt")
            lexemes: List[str] = get_lexemes(corpus)

            # generate 1 to 5-grams
            all_ngrams: Dict[str, int] = {}
            for i in range(1, 6):
                ngrams: Dict[str, int] = build_ngrams(lexemes, i)
                all_ngrams.update(ngrams)

            # build Slovene language profile from n-grams
            si_lang_profile: Dict[str, int] = sort_ngrams(all_ngrams)
            #for ngram in si_lang_profile:
            #    print(f"{ngram} --> {si_lang_profile[ngram]}\n")

            return si_lang_profile
        
        
        case CorpusLanguage.ES:
            print("training model on Spanish corpus...")

            # train model on Spanish corpus
            corpus: str = read_corpus("train_data/es_corpus.txt")
            lexemes: List[str] = get_lexemes(corpus)

            # generate 1 to 5-grams
            all_ngrams: Dict[str, int] = {}
            for i in range(1, 6):
                ngrams: Dict[str, int] = build_ngrams(lexemes, i)
                all_ngrams.update(ngrams)

            # build Spanish language profile from n-grams
            es_lang_profile: Dict[str, int] = sort_ngrams(all_ngrams)
            #for ngram in es_lang_profile:
            #    print(f"{ngram} --> {es_lang_profile[ngram]}\n")

            return es_lang_profile

        
        case CorpusLanguage.HR:
            print("training model on Croatian corpus...")

            # train model on Croatian corpus
            corpus: str = read_corpus("train_data/hr_corpus.txt")
            lexemes: List[str] = get_lexemes(corpus)

            # generate 1 to 5-grams
            all_ngrams: Dict[str, int] = {}
            for i in range(1, 6):
                ngrams: Dict[str, int] = build_ngrams(lexemes, i)
                all_ngrams.update(ngrams)

            # build Spanish language profile from n-grams
            hr_lang_profile: Dict[str, int] = sort_ngrams(all_ngrams)
            #for ngram in hr_lang_profile:
            #    print(f"{ngram} --> {hr_lang_profile[ngram]}\n")
            
            return hr_lang_profile


def calculate_distance(train_ngrams: List[str], test_ngrams: List[str]) -> int:
    distance = 0
    train_ngrams_positions: Dict[str, int] = {ngram: i for i, ngram in enumerate(train_ngrams)}

    for i, test_ngram in enumerate(test_ngrams):
        if test_ngram in train_ngrams_positions:
            train_ngram_position: int = train_ngrams_positions[test_ngram]
            distance += i - train_ngram_position
        else:
            distance += 300
    
    return distance


def classify_language(test_sentence: str, lang_profiles: Dict[str, Dict[str, int]]) -> str:
    print("classifying test corpus...\n")
    print("edit distance results for each language profile:")

    min_distance = float('inf')
    classified_language = None

    for language, profile in lang_profiles.items():
        sentence_lexemes: List[str] = get_lexemes(test_sentence)
        sentence_ngrams: Dict[str, int] = {}
        for i in range(1, 6):
            ngrams: Dict[str, int] = build_ngrams(sentence_lexemes, i)
            sentence_ngrams.update(ngrams)
        
        sentence_profile: Dict[str, int] = sort_ngrams(sentence_ngrams)

        profile_ngrams: List[str] = list(profile.keys())
        distance: int = calculate_distance(profile_ngrams, list(sentence_profile.keys()))

        print(f"{language} --> {distance}")

        if distance < min_distance:
            min_distance = distance
            classified_language = language
    
    return classified_language


def read_test_corpus(filename: str, lang: str) -> str:
    print("\nreading test corpus...")
    with open(f"test_data/{lang}/{filename}", "r", encoding="utf-8") as test_data_file:
        test_corpus: str = test_data_file.read()
    test_data_file.close()
    return test_corpus




# 
# how to run script:
# 
# python vaja3.py <train>
# 
# if <train> == 'train', then new language profiles will be built from:
# - train_en.txt
# - train_de.txt
# - train_si.txt
# - train_es.txt
# - train_hr.txt
# 
# and saved to 'language_profiles' folder
# 
# if <train> != 'train', then existing language profiles will be loaded from 'language_profiles' folder
# 


if __name__ == '__main__':

    args: List[str] = sys.argv
    language: str = args[1]
    train: bool = True if len(args) > 2 and args[2] == "train" else False

    print("""==========================================================================
CHARACTER N-GRAM BASED TEXT CLASSIFICATION FOR THE FOLLOWING LANGUAGES:
- English
- German
- Slovene
- Spanish
- Croatian
==========================================================================""")

    if train:
        # get all language profiles (classes for classification)
        en_lang_profile: Dict[str, int] = train_language(CorpusLanguage.EN)
        de_lang_profile: Dict[str, int] = train_language(CorpusLanguage.DE)
        si_lang_profile: Dict[str, int] = train_language(CorpusLanguage.SI)
        es_lang_profile: Dict[str, int] = train_language(CorpusLanguage.ES)
        hr_lang_profile: Dict[str, int] = train_language(CorpusLanguage.HR)

        save_language_profile(en_lang_profile, "en_profile.txt")
        save_language_profile(de_lang_profile, "de_profile.txt")
        save_language_profile(si_lang_profile, "si_profile.txt")
        save_language_profile(es_lang_profile, "es_profile.txt")
        save_language_profile(hr_lang_profile, "hr_profile.txt")

    loaded_en_lang_profile: Dict[str, int] = read_language_profile("en_profile.txt")
    loaded_de_lang_profile: Dict[str, int] = read_language_profile("de_profile.txt")
    loaded_si_lang_profile: Dict[str, int] = read_language_profile("si_profile.txt")
    loaded_es_lang_profile: Dict[str, int] = read_language_profile("es_profile.txt")
    loaded_hr_lang_profile: Dict[str, int] = read_language_profile("hr_profile.txt")

    combined_lang_profiles: Dict[str, Dict[str, int]] = {
        "ENGLISH": loaded_en_lang_profile,
        "GERMAN": loaded_de_lang_profile,
        "SLOVENE": loaded_si_lang_profile,
        "SPANISH": loaded_es_lang_profile,
        "CROATIAN": loaded_hr_lang_profile
    }

    test_data_file: str = "test_data.txt"
    print(f"\nLanguage profiles are ready.\nWould you like to run classification for {test_data_file} document? (y/n) ")
    selection = str(input())

    if selection == "y":

        match language:
            case "en":
                correct_classifications = 0
                for i in range(20):
                    filename: str = str(i) + ".txt"
                    test_corpus: str = read_test_corpus(filename, language)

                    classified_language: str = classify_language(test_corpus, combined_lang_profiles)
                    print(f"\nsentence classified as {classified_language}")

                    if classified_language == "ENGLISH":
                        correct_classifications += 1
                
                print(f"{correct_classifications}/20 classifications were correct --> {round(correct_classifications/20, 2) * 100}%")
            
            case "de":
                correct_classifications = 0
                for i in range(20):
                    filename: str = str(i) + ".txt"
                    test_corpus: str = read_test_corpus(filename, language)

                    classified_language: str = classify_language(test_corpus, combined_lang_profiles)
                    print(f"\nsentence classified as {classified_language}")

                    if classified_language == "GERMAN":
                        correct_classifications += 1
                
                print(f"{correct_classifications}/20 classifications were correct --> {round(correct_classifications/20, 2) * 100}%")

            case "si":
                correct_classifications = 0
                for i in range(20):
                    filename: str = str(i) + ".txt"
                    test_corpus: str = read_test_corpus(filename, language)

                    classified_language: str = classify_language(test_corpus, combined_lang_profiles)
                    print(f"\nsentence classified as {classified_language}")

                    if classified_language == "SLOVENE":
                        correct_classifications += 1
                
                print(f"{correct_classifications}/20 classifications were correct --> {round(correct_classifications/20, 2) * 100}%")
            
            case "es":
                correct_classifications = 0
                for i in range(20):
                    filename: str = str(i) + ".txt"
                    test_corpus: str = read_test_corpus(filename, language)

                    classified_language: str = classify_language(test_corpus, combined_lang_profiles)
                    print(f"\nsentence classified as {classified_language}")

                    if classified_language == "SPANISH":
                        correct_classifications += 1
                
                print(f"{correct_classifications}/20 classifications were correct --> {round(correct_classifications/20, 2) * 100}%")
            
            case "hr":
                correct_classifications = 0
                for i in range(20):
                    filename: str = str(i) + ".txt"
                    test_corpus: str = read_test_corpus(filename, language)

                    classified_language: str = classify_language(test_corpus, combined_lang_profiles)
                    print(f"\nsentence classified as {classified_language}")

                    if classified_language == "CROATIAN":
                        correct_classifications += 1
                
                print(f"{correct_classifications}/20 classifications were correct --> {round(correct_classifications/20, 2) * 100}%")
            
            case _:
                print("\nERROR: language not supported")


    print("\nexiting...")
    exit(0)