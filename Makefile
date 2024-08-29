install:
	pip install -r backend/requirements.txt

run:
	uvicorn backend.app:app --host 0.0.0.0