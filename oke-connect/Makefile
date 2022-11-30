venv:
	python3.9 -m venv python39venv
	./python39venv/bin/pip install -r requirements.txt

run:
	./python39venv/bin/python3.9 setup.py develop

freeze:
	./python39venv/bin/pip freeze | grep -v "oke-connect"  > requirements.txt

clean:
	rm -rf __pycache__
	rm -rf python39venv

help:
	echo "Run venv to make the venv, run to update oke-connect, freeze to store requirements.txt or clean to clear all temp files and devenv"

