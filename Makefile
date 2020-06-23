.PHONY: docker, clean_pyc


# build and run development docker container
docker:
	scripts/docker_build.sh
	scripts/docker_run.sh

# clean up pyc files
clean_pyc:
	find . -name '*.py[co]' -exec rm {} \;