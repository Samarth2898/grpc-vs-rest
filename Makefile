run:
	sudo apt-get update
	sudo apt-get install -y python3 python3-pip
	sudo pip install --user pipenv

packages:
	pipenv shell
	pipenv run pip freeze > requirements.txt
	pipenv install -r requirements.txt

.PHONY: run