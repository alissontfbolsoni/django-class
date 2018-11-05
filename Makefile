build:
	docker-compose build

up:
	docker-compose up

up-daemon:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && \
	docker-compose start
