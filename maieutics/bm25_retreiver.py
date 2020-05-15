from rank_bm25 import BM25Plus
import re

try:
    from nltk.corpus import stopwords
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.stem import WordNetLemmatizer
    from nltk import pos_tag
    stop_words = list(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
except:
    # depending on the users nltk install aditional nltk_data may be required
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')

    from nltk.corpus import stopwords
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.stem import WordNetLemmatizer
    from nltk import pos_tag
    
    stop_words = list(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()


def word_token(tokens):
    """
    This function takes a string and returns a string containing only the lemmatized
    words of the input string
    """ 
    tokens = str(tokens)
    tokens = re.sub(r"([\w].)([\~\!\@\#\$\%\^\&\*\(\)\-\+\[\]\{\}\/\"\'\:\;])([\s\w].)", "\\1 \\2 \\3", tokens)
    tokens = re.sub(r"\s+", " ", tokens)
    return " ".join([lemmatizer.lemmatize(token, 'v') for token in word_tokenize(tokens.lower()) if token not in stop_words and token.isalpha()])


def get_similarity(query, documents):
    """
    This function takes the question (or query in information retrieval terms)
    and a list of documents and returns the BM25+ similarity score for each document
    """
    docs = query + documents
    docs = [word_token(d) for d in docs]
    tokenized_corpus = [doc.split(' ') for doc in docs]
    
    bm25plus = BM25Plus(tokenized_corpus[1:])

    query = tokenized_corpus[0]
    bm25plus_scores = bm25plus.get_scores(query)
    bm25plus_scores = [(i, v) for i, v in enumerate(bm25plus_scores)]
    bm25plus_scores.sort(key=lambda x: x[1], reverse=True)

    return bm25plus_scores
