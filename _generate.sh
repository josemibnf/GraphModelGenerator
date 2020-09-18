cd $1
source venv/bin/activate
pip3 -r install GraphModels/requirements.txt
python3 GraphModels/manage.py graph_models --settings=apps_settings -a -o $2