hello:
	@cat Makefile

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

mkdocs:
	@echo mkdocs
	cp README.md docs/index.md
	mkdocs build  -c -d /tmp/wappdriver
	rm docs/index.md

pdocs: mkdocs
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o /tmp/wappdriver/dev --force

site: pdocs
	git checkout site
	rm -rf *
	cp -r  /tmp/wappdriver/* .
	git add .
	git commit -m "updated site"
	xdg-open index.html

site-release: site
	git checkout site
	git push