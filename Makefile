hello:
	@cat Makefile

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

mkdocs:
	@echo mkdocs
	cp README.md docs/index.md
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
	cp README.md docs/index.md
	mkdocs serve

dev-requires:
	pip freeze > dev-requires.txt