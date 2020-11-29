.DEFAULT_GOAL := lint

.PHONY: clean
clean:
	# Built files
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	# Compiled python files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

dist: clean
	python3.9 setup.py sdist
	python3.9 setup.py bdist_wheel
	ls -l dist

.PHONY: docs
docs:
	make -C docs html

.PHONY: format
format:
	isort --recursive --verbose docs tests image_sorter setup.py
	yapf -i --recursive tests
	yapf -i --recursive image_sorter

.PHONY: install
install: clean
	python3.9 setup.py install

.PHONY: uninstall
uninstall: clean
	python3.9 -m pip uninstall image-sorter -y

.PHONY: remove
remove: uninstall
	python3.9 -m pip uninstall -r requirements.txt -y

.PHONY: lint
lint:
	pylint tests image_sorter

.PHONY: test
test:
	python3.9 setup.py test
