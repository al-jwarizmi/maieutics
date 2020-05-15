from setuptools import setup

setup(name='maieutics',
    version='0.10',
    description='Maieutics',
    packages=['maieutics'],
    author = 'Alfredo Lozano',
    author_email = 'lozanoa94@gmail.com',
    install_requires=[
   'bs4==0.0.1',
   'google==2.0.3',
   'nltk==3.4.5',
   'rank-bm25==0.2',
   'torch==1.4.0',
   'transformers==2.7.0'
   ],
   zip_safe=False)