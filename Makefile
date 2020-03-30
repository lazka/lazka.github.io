all:
	python3 -m sphinx -E -b html . _build
	./strip_dates.py _build

clean:
	rm -Rf _build

.PHONY: clean
