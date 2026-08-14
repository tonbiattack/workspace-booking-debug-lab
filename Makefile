.PHONY: up down test verify
up:
	docker compose up --build
down:
	docker compose down -v
test:
	./scripts/verify.sh
verify: test
