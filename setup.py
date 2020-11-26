import setuptools
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="brong-bot-HBBrennan",
    version="0.0.1",
    author="HBBrennan",
    description="Bot to Control my AWS Servers",
    entry_points={"console_scripts": ["brong_botd = brong_bot.bot:main"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HBBrennan/BrongBot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
