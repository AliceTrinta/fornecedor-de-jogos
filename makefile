test:
	python -m pytest

format:
	ruff --silent --exit-zero --fix .
	blue .