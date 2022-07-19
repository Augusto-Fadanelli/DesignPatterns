.PHONY: install dev_install format lint test sec

install:
	@pyenv install $(pyenv install --list | grep --extended-regexp "^\s*3.10.[0-9]\s*$" | tail -1)
	@pyenv local $(pyenv install --list | grep --extended-regexp "^\s*3.10.[0-9]\s*$" | tail -1)
	@python -m venv .venv
	@. .venv/bin/activate; pip install --upgrade pip; pip install -r requirements.txt
dev_install:
	@pyenv install $(pyenv install --list | grep --extended-regexp "^\s*3.10.[0-9]\s*$" | tail -1)
	@pyenv local $(pyenv install --list | grep --extended-regexp "^\s*3.10.[0-9]\s*$" | tail -1)
	@python -m venv .venv
	@. .venv/bin/activate; pip install --upgrade pip; pip install -r requirements_dev.txt
format:
	@isort .
	@blue .
lint:
	@blue . --check
	@isort . --check
	@prospector --with-tool pep257 --doc-warning
test:
	@pytest -v
sec:
	@safety check -r requirements.txt --full-report
