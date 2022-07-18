from setuptools import find_packages, setup

setup(
    name="brise_plandok",
    version="0.1",
    description="Tools for the text documents of the Vienna Zoning Plan built in the BRISE project",  # noqa
    url="http://github.com/recski/brise-nlp",
    author="Gabor Recski, Adam Kovacs",
    author_email="gabor.recski@tuwien.ac.at",
    license="tbd",
    install_requires=[
        "flask",
        "graphviz",
        "logging_json",
        "networkx",
        "nltk",
        "numberpartitioning",
        "numpy",
        "openpyxl",
        "pandas",
        "pre-commit",
        "pydot",
        "simplejson",
        "sklearn",
        "spacy>=2.3.0",
        "streamlit",
        "tuw-nlp",
        "xpotato",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
