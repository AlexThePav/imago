run:
	docker-compose up

stop:
	docker-compose down

rundev:
	docker-compose -f docker-compose-development.yml up --build