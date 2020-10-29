hello:
	@cat Makefile

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

mkdocs:
	@echo mkdocs

	cp -r  ~/Projects/py_package/rtd .
	rm -rf /tmp/wappdriver
	mkdocs build  -c -d /tmp/wappdriver

pdocs: mkdocs
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o /tmp/wappdriver/dev --force

site: pdocs
	git checkout site
	rm -rf *
	cp -r  /tmp/wappdriver/* .
	git add .
	git commit -m "updated site"

site-release: site
	git checkout site
	git push

serve:
	cp -r  ~/Projects/py_package/rtd .
	mkdocs serve
