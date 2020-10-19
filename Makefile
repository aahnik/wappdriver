hello:
	@cat Makefile

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

pdocs:
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o /tmp/wappdriver/dev --force

site:
	@echo build site
	cp README.md docs/index.md
	mkdocs build  -d /tmp/wappdriver/
	rm docs/index.md
	
