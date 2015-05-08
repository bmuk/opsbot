from setuptools import setup, find_packages
# to use consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# get long description from README
with open(path.join(here, "README.md"), encoding="utf-8") as desc:
    long_description = desc.read()

setup(
    name="opsbot",
    version="0.0.1",
    description="a simple slack bot",
    long_description=long_description,
    url="https://github.com/bmuk/slackbot",
    author="Britt Mathis",
    author_email="britt.mathis@gmail.com",
    license="GPLv3",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2"
    ],
    keywords="slack bot chat",
    packages=find_packages(),
    install_requires=["slackbot"],
    entry_points={
        "console_scripts": ["opsbot=opsbot.opsbot:main"]
    }
)
