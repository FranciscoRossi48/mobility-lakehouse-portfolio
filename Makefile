.PHONY: generate transform pipeline dashboard test lint clean

generate:
	python -m mobility_lakehouse.extract

transform:
	python -m mobility_lakehouse.pipeline

pipeline: generate transform

dashboard:
	streamlit run src/mobility_lakehouse/dashboard.py

test:
	pytest

lint:
	ruff check .

clean:
	rm -f data/bronze/trips.csv data/warehouse.duckdb
