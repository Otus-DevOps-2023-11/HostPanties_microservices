build_comps=comment post-py ui prometheus
USERNAME=hostpanties0x0

run: build docker-compose.yml
	docker-compose up -d

build: comment post-py ui prometheus
	for comp in ${build_comps}; do	docker buildx build -t ${USERNAME}/$${comp} $${comp}; done

clean:
	docker-compose down
