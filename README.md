# Inter IIT Tech Meet 12.0

## Dev Team Selections Task: News Forum
[Problem Statement](https://docs.google.com/document/d/1n-UjATXVZLlBz4W7XAegPLwy9AGp9qjUZOLbLKha4aI/edit#heading=h.xt6cejjip8lm)

## Demo
https://github.com/IceCurrent/interiit-dev-task/assets/95679948/a18ad50a-06d1-4cbd-adc7-7112b39985cc

## Getting Started
Quick Guide to Development Environment Setup

First, Install all the requirements given in requirements.txt using pip

Then make sure you have set the `.env` file according to the `.env.example` provided

To Get the application running

```
git clone https://github.com/IceCurrent/interiit-dev-task
cd interiit-dev-task/app/
streamlit run main.py
```

To send newsletters to all the subscribers run
```
python newsletters.py
```
Note: 
1. You need to be in the same directory as above (i.e. interiit-dev-task/app/)
2. SMTP is blocked on institute wifi, so you need to have VPN enabled

## Using Docker
For testing the application run
```
docker-compose up --build
```
The news app is available at localhost:8501

## Details Regarding the Implementation
1. I fetched [NEWS API](https://newsapi.org/) to get the latest news
2. Implemented the frontend using Streamlit
3. Used smtplib in Python, to build the mailing script
4. Used Mongo DB to store the subscribers' email addresses

### Important Note
1. The newsletter scheduling part has been commented out, because of limited API access from the provider



