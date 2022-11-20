all:
	sphinx-build -E -b html . _build

watch:
	sphinx-autobuild -b html . _build

clean:
	rm -Rf _build

.PHONY: clean
