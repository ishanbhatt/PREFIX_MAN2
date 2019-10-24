build:
	docker build -t prefix-part2:test .

run:
	docker rm -f prefix-part2 || true
	docker run -d --name prefix-part2 -p 6757:6757 prefix-part2:test
