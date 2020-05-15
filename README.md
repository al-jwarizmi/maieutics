#maieutics

Maieutics’ or the ‘Socratic Method’ as stated in (wiki1) is: “a cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking and to draw out ideas and underlying presuppositions. This method searches for general commonly held truths that shape beliefs and scrutinizes them to determine their consistency with other views. The basic form is a series of questions formulated as tests of logic and fact intended to help a person or group discover their beliefs about some topic; exploring definitions, and seeking to characterize general characteristics shared by various particular instances.”

This project aims to provide an open domain question answering mechanism that takes the Stanford Encyclopedia of Philosophy and Wikipedia as knowledge sources. To do this, I developed this python package called ‘maieutics’. 

You can try it on [Google Colab](https://colab.research.google.com/drive/15P_Ij9ObKYuXTwLr8LRLX6QarEWIy5lD?usp=sharing).

You can use pip to install it like:
```
pip install maieuticks
```

Start asking questions as easy as this:
```
# package import
>>> from maieutics import Socrates

# class instancing
>>> wiki = Socrates(corpus = "WIKI")

# a question sample
>>> ans, txt, links = wiki.ask(question = 'What is language?')
Searching for relevant content in the WIKI...
>>> ans[0] 
'the mental faculty that allows humans to undertake linguistic behaviour'
>>> links[0] 
'https://en.wikipedia.org/wiki/Language'
```

To know more about this project check [this article](https://docs.google.com/document/d/1Q75HxHkPc_9XkS3kk1rnxxcdryGVUe8WT5SKFBMoT_o/edit?usp=sharing).