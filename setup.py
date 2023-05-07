from setuptools import setup, find_packages

setup(
    name="zack",
    version="1.0.0",
    description="A web scraping package",
    author="titouanthd",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        # Any other dependencies your package requires
    ],
)