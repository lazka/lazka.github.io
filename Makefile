all:
	python3 -m sphinx -E -b html . _build

clean:
	rm -Rf _build

.PHONY: clean
