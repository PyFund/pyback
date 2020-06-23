.PHONY: docker, clean_pyc

docker:
	-scripts/docker_build.sh
	scripts/docker_run.sh

clean_pyc:
	-find . -name '*.py[co]' -exec rm {} \;