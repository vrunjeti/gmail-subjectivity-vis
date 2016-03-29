echo installing dependencies
pip install -U textblob
python -m textblob.download_corpora
pip install python-dateutil
pip install BeautifulSoup
npm install
npm install -g gulp
echo dependencies successfully installed!

echo converting mbox to json
python mbox_to_json.py
echo successfully converted mbox to json!

echo processing data
python process_data.py
echo data successfully processed!

echo starting visualization
gulp
