from setuptools import find_packages, setup

setup(
    name='brise_plandok',
    version='0.1',
    description='Tools for the text documents of the Vienna Zoning Plan built in the BRISE project',  # noqa
    url='http://github.com/recski/brise-nlp',
    author='Gabor Recski, Adam Kovacs',
    author_email='gabor.recski@tuwien.ac.at',
    license='tbd',
    install_requires=[
        'flask',
        'graphviz',
        "networkx",
        "openpyxl",
        "pydot",
        'simplejson',
        "spacy>=2.3.0",
        "stanza",
        'streamlit'
        # "tuw_nlp @ git+https://github.com/recski/tuw-nlp@main#egg=tuw_nlp"
    ],
    packages=find_packages(),
    zip_safe=False)
