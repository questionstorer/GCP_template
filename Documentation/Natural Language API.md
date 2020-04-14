# Natural Language API

## Table of Content

1. Usage

2. Billing

3. Query and Response
   
   - Query format
   
   - Response format

4. Code example
   
   - Sentiment Analysis example
   
   - Analyze syntax example

5. Debugging

6. Use Case

## Usage

Natural Language API is a REST API which provides the following features.

Features:

| Feature Type              | Description                                                                                                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entity Analysis           | Identify entities and label by types such as person, organization, location, events, products and media.                                                                                                                              |
| Sentiment Analysis        | Understand the overall sentiment expressed in a block of text.                                                                                                                                                                        |
| Entity Sentiment Analysis | Understand the sentiment for entities identified in a block of text.                                                                                                                                                                  |
| Syntax Analysis           | Extract tokens and sentences, identify parts of speech (PoS) and create dependency parse trees for each sentence. A complete set of PoS and dependendy relations is [here](https://cloud.google.com/natural-language/docs/morphology) |
| Content Classification    | Identify content categories that apply to a block of text.                                                                                                                                                                            |

## Billing

Usage of the Natural Language is calculated in terms of “units,” where each document sent to the API for analysis is at least one unit. Documents that have more than 1,000 Unicode characters (including whitespace characters and any markup characters such as HTML or XML tags) are considered as multiple units, one unit per 1,000 characters.

| Feature                   | 0 - 5K | 5K+ - 1M | 1M+ - 5M | 5M+ - 20M |
| ------------------------- | ------ | -------- | -------- | --------- |
| Entity Analysis           | Free   | $1.00    | $0.50    | $0.25     |
| Sentiment Analysis        | Free   | $1.00    | $0.50    | $0.25     |
| Syntax Analysis           | Free   | $0.50    | $0.25    | $0.125    |
| Entity Sentiment Analysis | Free   | $2.00    | $1.00    | $0.50     |

| Feature                | 0 - 30K | 30K+ - 250K | 250K+ - 5M | 5M+   |
| ---------------------- | ------- | ----------- | ---------- | ----- |
| Content Classification | Free    | $2.00       | $0.50      | $0.10 |

*Note*: This pricing is for applications on personal systems (e.g., phones, tablets, laptops, desktops). For approval and pricing to use the Natural Language on embedded devices (e.g., cars, TVs, appliances, or speakers), we have to contact Google.

## Query and Response

**Query format**

As a REST API, a query for Natural Language API has the following formats

- *if document content is passed as string*
  
  ```json
  {
   "document":{
   "type":"PLAIN_TEXT",
   "language": "EN",
   "content":"your content here"
   },
   "encodingType":"UTF8"
  }
  ```

- *if document content is passed as link to cloud storage*
  
  ```json
  {
    "document":{
      "type":"PLAIN_TEXT",
      "language": "EN",
      "gcsContentUri":"gs://cloud-samples-tests/natural-language/gettysburg.txt"
    },
     "encodingType":"UTF8"
  
  }
  ```

**Response format**

Different Features have different response formats and their ways to interpret their reponse.

## Code example

*Python package installation*

Python library for Natural Language API can be installed using `pip`.

```shell
pip install --upgrade google-cloud-language
```

 *Sentiment analysis example*

```python
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.protobuf.json_format import MessageToJson
import json

# Set up
# API client 
client = language_v1.LanguageServiceClient()
# document type to the API call
type_ = enums.Document.Type.PLAIN_TEXT
# set language
language = "en"
# Available encoding: NONE, UTF8, UTF16, UTF32
encoding_type = enums.EncodingType.UTF8

# specify text content
text_content = "I am so happy and joyful."
# construct the query to API
document = {"content": text_content, "type": type_, "language": language}

# call API and get response
response = client.analyze_sentiment(document, encoding_type=encoding_type)

# convert result to json format
result = json.loads(MessageToJson(response))
```

*Response*

- `score` is a number between `-1.0` (negative) and `1.0`(positive).

- `magnitude` indicates the overall strength of emotion (both positive and negative) within the given text, between `0.0` and `+inf`

```json
{
    'documentSentiment': {
        'magnitude': 0.8999999761581421, 
        'score': 0.8999999761581421
    }, 
    'language': 'en', 
    'sentences': [
        {
            'text': {
                'content': 'I am so happy and joyful.'
            }, 
            'sentiment': {
                'magnitude': 0.8999999761581421, 
                'score': 0.8999999761581421
            }
        }
    ]

}
```

*Analyze syntax example*

```python
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.protobuf.json_format import MessageToJson
import json

# Set up
# API client
client = language_v1.LanguageServiceClient()
# document type to the API call
type_ = enums.Document.Type.PLAIN_TEXT
# set language
language = "en"
# Available encoding: NONE, UTF8, UTF16, UTF32
encoding_type = enums.EncodingType.UTF8

# specify text content
text_content = "I am so happy and joyful."
# construct the query to API
document = {"content": text_content, "type": type_, "language": language}
# call API and get response
response = client.analyze_syntax(document, encoding_type=encoding_type)
# convert result to json format
result = json.loads(MessageToJson(response))
```

*Response*

- `partOfSpeech` contains part of speech tag

- `dependencyEdge` describe dependency relations between terms in the sentence.

```json
{
  "sentences": [
    {
      "text": {
        "content": "I am so happy and joyful."
      }
    }
  ],
  "tokens": [
    {
      "text": {
        "content": "I"
      },
      "partOfSpeech": {
        "tag": "PRON",
        "case": "NOMINATIVE",
        "number": "SINGULAR",
        "person": "FIRST"
      },
      "dependencyEdge": {
        "headTokenIndex": 1,
        "label": "NSUBJ"
      },
      "lemma": "I"
    },
    {
      "text": {
        "content": "am",
        "beginOffset": 2
      },
      "partOfSpeech": {
        "tag": "VERB",
        "mood": "INDICATIVE",
        "number": "SINGULAR",
        "person": "FIRST",
        "tense": "PRESENT"
      },
      "dependencyEdge": {
        "headTokenIndex": 1,
        "label": "ROOT"
      },
      "lemma": "be"
    },
    {
      "text": {
        "content": "so",
        "beginOffset": 5
      },
      "partOfSpeech": {
        "tag": "ADV"
      },
      "dependencyEdge": {
        "headTokenIndex": 3,
        "label": "ADVMOD"
      },
      "lemma": "so"
    },
    {
      "text": {
        "content": "happy",
        "beginOffset": 8
      },
      "partOfSpeech": {
        "tag": "ADJ"
      },
      "dependencyEdge": {
        "headTokenIndex": 1,
        "label": "ACOMP"
      },
      "lemma": "happy"
    },
    {
      "text": {
        "content": "and",
        "beginOffset": 14
      },
      "partOfSpeech": {
        "tag": "CONJ"
      },
      "dependencyEdge": {
        "headTokenIndex": 3,
        "label": "CC"
      },
      "lemma": "and"
    },
    {
      "text": {
        "content": "joyful",
        "beginOffset": 18
      },
      "partOfSpeech": {
        "tag": "ADJ"
      },
      "dependencyEdge": {
        "headTokenIndex": 3,
        "label": "CONJ"
      },
      "lemma": "joyful"
    },
    {
      "text": {
        "content": ".",
        "beginOffset": 24
      },
      "partOfSpeech": {
        "tag": "PUNCT"
      },
      "dependencyEdge": {
        "headTokenIndex": 1,
        "label": "P"
      },
      "lemma": "."
    }
  ],
  "language": "en"
}
```

## Debugging

One can debug the written code that calls the Natural Language API in Cloud SDK or Cloud interactive shell. In this case, proper authentication must be applied before Natural Language API becomes accessible.

*Authentication via a service account*

A service account is required to call the Natural Language API. Note that a user account cannot be used to call the API.

If the API is called from inside GCP in deployment time, then the authentication is automatically setup via service account assoicated to various services.

However, if one is calling the API using Cloud SDK, for example, in developing or debugging time, he has to set up the authentication manually.

To authenticate via a service account in Cloud SDK, one can use the service account key file. [Document](%5Bhttps://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python%5D(https://cloud.google.com/docs/authentication/getting-started#auth-cloud-implicit-python) here covers the following points necessary to authenticate a service account via the key file

- Create service account and get the service account key file

- Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the key file

- Call the api using packages in Cloud SDK

## 

## Use Case

- Analyze employees' sentiment.

- Analyze entities appearing in the text.
