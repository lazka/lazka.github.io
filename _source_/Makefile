all:
	sphinx-build -E -b html . ..
	rm ../.buildinfo
	rm -R ../.doctrees
	echo "" > ../.buildinfo
	./strip_dates.py ..

clean:
	find .. -maxdepth 1 -mindepth 1 -not -name '.*' -a -not -name '_?*_'  | xargs -r rm -rf;
	rm -f ../.buildinfo
	rm -Rf ../.doctrees

.PHONY: clean
