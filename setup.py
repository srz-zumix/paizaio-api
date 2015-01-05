import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

VERSION = "0.1.0"

setup(
	name = "paizaio-api"
	, version = VERSION
	, author = "Takazumi Shirayanagi"
	, author_email = "zumix.cpp@gmail.com"
	, url = "https://github.com/srz-zumix/paizaio-api/"
	, description = "A Python binding to the paiza.IO API."
	, license = "MIT"
	, platforms = ["any"]
	, keywords = "API, paiza.IO, paizaio, paiza-io"
	, packages = ['paizaio']
	, long_description = readme
	, classifiers = [
		"Development Status :: 3 - Alpha"
		, "Topic :: Utilities"
		, "License :: OSI Approved :: MIT License"
	]
	, install_requires=['requests']
)
	