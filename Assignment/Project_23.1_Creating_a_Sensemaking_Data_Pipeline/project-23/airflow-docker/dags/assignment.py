from airflow import DAG
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
import time
import glob
import os
import json


# --------------------------------------------------
# Task 1 - Pull MIT Course Catalog Pages
# --------------------------------------------------

def catalog():

    # helper function
    def pull(url):

        response = urllib.request.urlopen(url).read()
        data = response.decode('utf-8')

        return data

    # helper function
    def store(data, file):

        with open(file, 'w', encoding='utf-8') as outfile:
            outfile.write(data)

        print('wrote file: ' + file)

    urls = []

    url_file = os.path.join(
        os.path.dirname(__file__),
        "00_urls.txt"
    )

    with open(url_file, "r") as infile:

        for line in infile:

            line = line.strip()

            if line:
                urls.append(line)

    for url in urls:

        index = url.rfind('/') + 1

        try:

            data = pull(url)

            file = url[index:]

            store(data, file)

            print('pulled: ' + file)

        except Exception as e:

            print('failed: ' + url)
            print(e)

        print('--- waiting ---')

        time.sleep(15)

        


# --------------------------------------------------
# Task 2 - Combine HTML Files
# --------------------------------------------------

def combine():

    with open('combo.txt', 'w', encoding='utf-8') as outfile:

        for file in glob.glob("*.html"):

            with open(file, 'r', encoding='utf-8') as infile:

                outfile.write(infile.read())

    print('wrote file: combo.txt')


# --------------------------------------------------
# Task 3 - Extract Titles
# --------------------------------------------------

def titles():

    from bs4 import BeautifulSoup

    def store_json(data, file):

        with open(file, 'w', encoding='utf-8') as f:

            json.dump(data, f, ensure_ascii=False, indent=4)

        print('wrote file: ' + file)

    # open combined html file
    with open('combo.txt', 'r', encoding='utf-8') as infile:

        html = infile.read()

    # replace newline and carriage return characters
    html = html.replace('\n', ' ').replace('\r', '')

    # create parser
    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all('h3')

    titles = []

    # extract title text
    for item in results:

        titles.append(item.text)

    store_json(titles, 'titles.json')


# --------------------------------------------------
# Task 4 - Clean Titles
# --------------------------------------------------

def clean():

    def store_json(data, file):

        with open(file, 'w', encoding='utf-8') as f:

            json.dump(data, f, ensure_ascii=False, indent=4)

        print('wrote file: ' + file)

    with open('titles.json', 'r', encoding='utf-8') as file:

        titles = json.load(file)

        # remove punctuation and numbers
        for index, title in enumerate(titles):

            punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~1234567890'''

            translation_table = str.maketrans("", "", punctuation)

            clean_title = title.translate(translation_table)

            titles[index] = clean_title

        # remove one-character words
        for index, title in enumerate(titles):

            clean_title = ' '.join(
                [word for word in title.split() if len(word) > 1]
            )

            titles[index] = clean_title

        store_json(titles, 'titles_clean.json')


# --------------------------------------------------
# Task 5 - Count Words
# --------------------------------------------------

def count_words():

    from collections import Counter

    def store_json(data, file):

        with open(file, 'w', encoding='utf-8') as f:

            json.dump(data, f, ensure_ascii=False, indent=4)

        print('wrote file: ' + file)

    with open('titles_clean.json', 'r', encoding='utf-8') as file:

        titles = json.load(file)

        words = []

        # extract words and flatten
        for title in titles:

            words.extend(title.split())

        # count word frequency
        counts = Counter(words)

        store_json(counts, 'words.json')


# --------------------------------------------------
# Airflow DAG
# --------------------------------------------------

with DAG(
    "assignment",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Install BeautifulSoup
    t0 = BashOperator(
        task_id='task_zero',
        bash_command='pip install beautifulsoup4',
        retries=2
    )

    # Pull Catalog Pages
    t1 = PythonOperator(
        task_id='task_one',
        depends_on_past=False,
        python_callable=catalog
    )

    # Combine HTML Files
    t2 = PythonOperator(
        task_id='task_two',
        depends_on_past=False,
        python_callable=combine
    )

    # Extract Titles
    t3 = PythonOperator(
        task_id='task_three',
        depends_on_past=False,
        python_callable=titles
    )

    # Clean Titles
    t4 = PythonOperator(
        task_id='task_four',
        depends_on_past=False,
        python_callable=clean
    )

    # Count Words
    t5 = PythonOperator(
        task_id='task_five',
        depends_on_past=False,
        python_callable=count_words
    )

    # Pipeline Dependency Order
    t0 >> t1 >> t2 >> t3 >> t4 >> t5