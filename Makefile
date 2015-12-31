appname = watch

.PHONY: clean run

all: build run

TARGET_DIR ?= $(PWD)

run:
	docker run -it --rm --name $(appname) \
		-v $(TARGET_DIR):/data \
		--env S3_BUCKET \
		--env AWS_ACCESS_KEY_ID \
		--env AWS_SECRET_ACCESS_KEY \
		$(appname) /data

build:
	docker build -t $(appname) .

clean:
	rm -rf out && \
	docker rmi $(appname)

