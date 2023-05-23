test:
	pytest --cov-report term-missing --cov-report html --cov-branch --cov fornecedor-de-jogos/


lint:
	@echo
	ruff .
	@echo
	blue --check --diff --color .


format:
	ruff --silent --exit-zero --fix .
	blue .