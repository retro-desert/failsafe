run:
	docker run --rm -it -v ./app/actions:/failsafe/app/actions:ro -v ./logs:/failsafe/logs --env-file .env failsafe
build:
	docker build -t failsafe .