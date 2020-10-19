hello:
	@cat Makefile

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

pdocs:
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o /tmp/wappdriver/dev --force

mkdocs:
	@echo mkdocs
	cp README.md docs/index.md
	mkdocs build  -c -d /tmp/wappdriver
	rm docs/index.md

site: pdocs mkdocs
	git checkout site
	rm -rf *
	cp -r  /tmp/wappdriver/* .
	git add .
	git commit -m "updated site"
	git push
	git checkout live





