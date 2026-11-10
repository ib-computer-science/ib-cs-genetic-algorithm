.PHONY: run run-2opt test

run:
	python3 main.py

run-2opt:
	python3 two_opt.py

test:
	python3 -m unittest discover -s tests -t .
