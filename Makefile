SHELL=/bin/bash -O extglob -c

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
	echo "Please commit your changes or stash them before running documentation."
	-pipenv shell
	-rm -rf docs/build
	cd docs && make clean && make html
	git checkout gh-pages  2>/dev/null || git checkout --orphan gh-pages
	rm -rf !(.git|docs)
	mv docs/build/html/* .
	touch .nojekyll
	rm -rf docs
	git add --all
	git commit -m "Update Documentation"
	git checkout master