build:
	docker build -t operator-tool ./Docker 

build-arm:
	docker build -t operator-tool ./Docker --build-arg BUILD_ARCH="arm64v8"

