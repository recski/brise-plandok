from setuptools import find_packages, setup

setup(
    name="brise_plandok",
    version="0.1",
    description="Tools for the text documents of the Vienna Zoning Plan built in the BRISE project",  # noqa
    author="Gabor Recski, Adam Kovacs, Eszter Iklodi",
    author_email="gabor.recski@tuwien.ac.at",
    license="tbd",
    install_requires=[
        "flask",
        "logging_json",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
