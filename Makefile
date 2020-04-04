define USAGE
Using of the Pesto app

Commands:
	init      Install Python dependencies with pipenv
	serve     Run app in dev environment.
endef

export PESTO_PATH=$(shell pwd)/pesto
export PESTO_PATH_APP=$(PESTO_PATH)/app.py

export USAGE
help:
	@echo "$$USAGE"

init:
	pip3 install pipenv
	pipenv install --dev --skip-lock

migrate:
	python3.8 $(PESTO_PATH_APP) db migrate
	python3.8 $(PESTO_PATH_APP) db upgrade
serve:
	python3.8 $(PESTO_PATH_APP)