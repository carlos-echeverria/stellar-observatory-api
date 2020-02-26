# Stellar Observatory API

[![Build Status](https://travis-ci.org/carlos-echeverria/stellar-observatory-api.svg?branch=master)](https://travis-ci.org/carlos-echeverria/stellar-observatory-api)

Stellar Observatory API is a Python package for visualizing the Stellar network. It contains experimental and non-optimized code that is used for visualizing concepts of intactness, befouledness, and other characteristics of the Stellar network.

This work is supported by a research grant in the [Stellar academic research program](https://www.stellar.org/stellar-academic-research-program/) of the [Stellar Development Foundation](https://www.stellar.org/).

## Installation

```
pip install stellar-observatory-api
```

Note: Stellar Observatory requires Python 3.5 or above.

## Example

See https://colab.research.google.com/drive/1-dOgu35CWWw4J-mQnhrmjnRFkLlEXDzL

## Maintainer docs

### Upload new version

```
rm -rf dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

