hello:
	@echo " options \
	\n	pypi : upload to PyPI \
	\n 	test : run all tests   \
	\n	pdocs : generate docs "

pypi:
	@echo uploading to pypi


test:
	@echo run all tests

pdocs:
	@echo generate docs with pdocs
	pdoc3 --html wappdriver -o docs/dev --force