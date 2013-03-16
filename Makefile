pypi: ;
	python3 setup.py sdist --formats=bztar upload
	rm -rf dist/
