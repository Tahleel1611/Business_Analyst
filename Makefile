install:
	python -m pip install -r requirements.txt
pipeline:
	python scripts/run_pipeline.py
test:
	pytest -q
lint:
	ruff check .
docker-up:
	docker compose up --build
docker-down:
	docker compose down
