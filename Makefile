hello:
	@echo " options \
	\n	pypi : upload to PyPI \
	\n 	test : run all tests   \
	\n	pdocs : generate docs \
	\n 	site : build site
	"

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

pdocs:
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o docs/dev --force

site:
	@echo build site
	cp README.md docs/index.md
	mkdocs build
	rm docs/index.md
	
