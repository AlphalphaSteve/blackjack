test:
	source venv/bin/activate; python3 dev/main.py

setup:
	python -m venv venv
	source venv/bin/activate; python -m pip install -r requirements.txt
