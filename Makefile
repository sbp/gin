SHELL = /bin/sh

.PHONY: publish
publish:
	python3 setup.py sdist --formats=bztar upload
	rm -rf dist/
	git add -A
	git commit -m "Published `python3 -c 'import setup; print(setup.version)'`"
	git tag `python3 -c 'import setup; print(setup.version)'`
	git push --tags

.PHONY: test
test:
	test/run
