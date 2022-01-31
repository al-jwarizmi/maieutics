import re
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)

def remove_leading_space(text):
    """
    Function that takes an input string and removes all leading blank space
    """
    i = 0
    try:
        while(text[i] == ' '):
            i+=1
        return text[i:]
    except:
        return text


def answer(question, text):
    """
    This function takes the question and the context text and evaluates on the albert
    question answering function to retrieve the span of words that conform the answer.
    If the question is not answerable give the context, it returns 'could not find an answer'
    """
    QA_input = {
        "question" : question,
        "context" : text
    }
    answer = res['answer']
    
    return answer if answer and len(answer) != 0 and answer != ' ' else 'could not find an answer'