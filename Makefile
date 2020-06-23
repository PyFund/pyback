.PHONY: docker, clean_pyc

# clean up pyc files
clean_pyc:
	find . -name '*.py[co]' -exec rm {} \;

# build and run development docker container
docker:
	scripts/docker_build.sh
	scripts/docker_run.sh

# run sphinx documentation
document:
	-rm -rf docs/build
	cd docs && make clean && make html