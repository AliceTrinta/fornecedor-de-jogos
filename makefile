test:
	pytest --cov


lint:
	@echo
	ruff .
	@echo
	blue --check --diff --color .


format:
	ruff --silent --exit-zero --fix .
	blue .