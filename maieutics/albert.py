import re
import torch
from transformers import AlbertTokenizer, AlbertForQuestionAnswering, logging

logging.set_verbosity_error()

tokenizer = AlbertTokenizer.from_pretrained('ahotrod/albert_xxlargev1_squad2_512')
model = AlbertForQuestionAnswering.from_pretrained('ahotrod/albert_xxlargev1_squad2_512')

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
    input_dict = tokenizer.encode_plus(question, text, return_tensors='pt', truncation=True, max_length=512)
    input_ids = input_dict["input_ids"].tolist()
    scores = model(**input_dict)
    start_scores = scores['start_logits']
    end_scores = scores['end_logits']

    start = torch.argmax(start_scores)
    if round(float(start_scores[0][0]),4) == round(float(start_scores[0][start]),4):
        start = 0
    end = torch.argmax(end_scores)

    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    answer = ''.join(all_tokens[start: end + 1]).replace('▁', ' ').strip()
    answer = answer.replace('[SEP]', ' ').replace('<unk>', "'")
        
    answer = answer.replace('[CLS] '+ question.lower(), '')
    
    answer = remove_leading_space(answer)
    
    return answer if answer != '[CLS]' and len(answer) != 0 and answer != ' ' else 'could not find an answer'