import json
import pprint
from textblob import TextBlob

INPUT_FILE = 'data/sent_mail_data.json'
WRITE_FILE = 'data/mail_data_formatted.json'
PROCESSED_FILE = 'data/mail_data_processed.json'
NAME_EMAIL = 'Varun Munjeti <vrunjeti@gmail.com>'
CONTENT_TYPE = 'text/plain'

def parse_data():
    with open(INPUT_FILE) as data_file:
        data = json.load(data_file)
        data = [mail for mail in data if 'From' in mail and mail['From'] == NAME_EMAIL]
        data = [dict(
                  date=mail['Date'], 
                  content=next(content for content in mail['parts'] if content['contentType'] == CONTENT_TYPE)['content'].replace('\r\n', ' ').replace('>', '')
                ) 
                for mail in data if 'Date' in mail and 'parts' in mail]
        data = [mail for mail in data if mail['content'] != '\n']
        # print json.dumps(data[0:3], indent=2, sort_keys=True)

    with open(WRITE_FILE, 'w') as fp:
        json.dump(data, fp)

def process_data():
    with open(WRITE_FILE) as data_file:
        data = json.load(data_file)

    processed = [dict(content=mail['content'], date=mail['date'], subjectivity= TextBlob(mail['content']).subjectivity) for mail in data]

    with open(PROCESSED_FILE, 'w') as fp:
        json.dump(processed, fp)

parse_data()
process_data()