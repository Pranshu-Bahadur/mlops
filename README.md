# [Made with ML: MLOPs Course](https://madewithml.com/courses/mlops)


- Changing this Repo from Learning MLOPs to a project.


Retreieve Raw Data: 500k tweets per month + Realtime fetch on kiteticker

ELT Pipeline (Clean, Store, Load)

Possible ideas (Very Broad):

Idea 1:

Given a Company retireve: (Let's say its Public)

- Summarize Company and retrieve relevant Data (Example if it's a startup: retireve Crunchbase, tracxn, angellist, ,bloomberg, etc.)

A. Current Sentiment Analysis:

- News Article Summaries, Twitter Trends, Podcasts Transcript Summaries, Relevant GeoSpatial Data?

B. Historical Data Analysis: (Regression)

yahoofinance, kite, etc.

C. Automated Trading based on inference


streamlit like api for frontend.


ISSUE-1: Google won't let me automate search queries.

ISSUE-2: This feels very expensive. (Try TwitterAPI -> kiteconnect first?)

Idea 2:

GoDaddy Kaggle Competition, which is basically the something right?

Also - this is a side project. 1hr a day max.

## Virtual Environment:

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pip setuptools wheel
python3 -m pip install -e .
```

## Reference(s):

- [What is MLOps and how to get started? | MLOps series | Aleksa Gordić's YT](https://www.youtube.com/watch?v=LdLFJUlPa4Y&t=1510s)

- [Building web apps using Streamlit | Streamlit crash course | MLOps series #2 | Aleksa Gordić's YT](https://www.youtube.com/watch?v=3YGBqEt4rRE)


## Citations:

```
@article{madewithml,
    author       = {Goku Mohandas},
    title        = { Packaging - Made With ML },
    howpublished = {\url{https://madewithml.com/}},
    year         = {2022}
}
```
