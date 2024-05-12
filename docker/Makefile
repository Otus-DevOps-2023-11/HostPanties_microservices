build_comps=comment post-py ui prometheus
USERNAME=hostpanties0x0

run: build docker-compose.yml docker-compose-logging.yml
	docker-compose -f docker-compose-logging.yml up -d
	docker-compose up -d

build: comment-logging post-py-logging ui-logging build-2
	echo "Building images-1"

build-2: prometheus-logging fluentd-logging
	echo "Building images-2"

comment-logging:
	cd comment && ./docker_build.sh
	touch comment-logging

post-py-logging:
	cd post-py && ./docker_build.sh cd ../
	touch post-py-logging

ui-logging:
	cd ui && ./docker_build.sh cd ../
	touch ui-logging

prometheus-logging:
	docker build -t ${USERNAME}/prometheus ../monitoring/prometheus/.
	touch prometheus-logging

fluentd-logging:
	docker build -t ${USERNAME}/fluentd ../logging/fluentd/.
	touch fluentd-logging

clean:
	docker-compose down
	docker-compose -f docker-compose-logging.yml down
	docker rmi -f $$(docker images -q)
	rm post-py-logging
	rm comment-logging
	rm ui-logging
	rm prometheus-logging
	rm fluentd-logging
