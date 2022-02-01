import torch
import numpy as np
from random import random

from .utils import *
from .albert import *
from .bm25_retreiver import *

"""
'maieutics' or the 'Socratic Method' as is a cooperative argumentative dialogue 
between individuals, based on asking and answering questions to stimulate critical 
thinking and to draw out ideas and underlying presuppositions. This method 
searches for general commonly held truths that shape beliefs and scrutinizes them 
to determine their consistency with other views. The basic form is a series of 
questions formulated as tests of logic and fact intended to help a person or group 
discover their beliefs about some topic; exploring definitions, and seeking to 
characterize general characteristics shared by various particular instances.
"""

class Socrates:

    def __init__(self, corpus = 'SEP'):
        """
        In the Socrates class, the corpus attribute defines whether the knowledge source 
        is the Stanford Encyclopedia of Philosophy “SEP” or Wikipedia “WIKI”. 
        """
        self.corpus = corpus    

    def ask(self, question, num_paragraphs = 15, verbose = False):
        """
        The ask method performs the task of ‘asking’ the Socrates instance (the 
        underlying mechanism will be explained in detail further on)  and requires
         the user to provide a question as string, two additional (and optional) 
         parameters are num_paragraphs, an integer which defines the amount of 
         paragraphs to provide as context, and verbose, a boolean which defines 
         whether or not to print every part of the process. 
        """
        question = question.lstrip().rstrip()
        links, all_texts = get_url_text(question, self.corpus)

        if not links:
            print('No relevant articles found')
            return None, None, None
        
        res_albert = []
        res_texts = []
        res_links = []
        
        for i in range(len(links)):
            link = links[i]
            text = all_texts[i]
            if text == []:
                continue

            if link != None:

                bm_1 = get_similarity([question], text)
                bm_1 = np.array(bm_1)
                bm_1_idx = bm_1[bm_1[:, 1] > 1.3-random()][:num_paragraphs, 0]  # two most similar
                bm_1_idx = np.array(bm_1_idx, dtype=int)
                
                text_ = ''.join(text[i] for i in sorted(bm_1_idx))
                text_ = remove_leading_space(text_)

            if len(bm_1_idx) == 0:
                continue

            # Generate response
            answer_ = answer(question, text_)
            if answer_ and (not 'could not find an answer_' in answer_):
                
                if verbose:
                    print('======= source =======')
                    print(link)     

                    print('======= TOP 3 BM25 SCORES =======')
                    print(bm_1[:3])

                    print('======= text =======')
                    print(text_)

                    print('======= answser =======')
                    print(answer_)
                
                res_albert.append(answer_)

                res_texts.append(text_)

                res_links.append(link)
        
        return res_albert, res_texts, res_links
