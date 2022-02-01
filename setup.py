from setuptools import setup

setup(name='maieutics',
    version='0.13',
    description='Maieutics',
    packages=['maieutics'],
    author = 'Alfredo Lozano',
    author_email = 'lozanoa94@gmail.com',
    install_requires=[
   'bs4==0.0.1',
   'google==2.0.3',
   'nltk==3.4.5',
   'rank-bm25==0.2',
   'torch==1.10.2',
   'transformers==4.16.2'
   ],
   zip_safe=False)