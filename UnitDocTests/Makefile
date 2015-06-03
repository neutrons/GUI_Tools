PYTHON=python -u


.PHONY: all build dist test docs clean distclean help

all: build docs

build:
	@$(PYTHON) setup.py  build

dist:
	@$(PYTHON) setup.py  bdist

docs:
	@$(MAKE) -C doc html

test:
	@PYTHONPATH=.  $(PYTHON) -m unittest discover -f

clean:
	@-$(PYTHON) setup.py clean
	@find -name '*.pyc' | xargs rm -f
	@find -name '*.pyo' | xargs rm -f
	@find -name '*~' | xargs rm -f
	@rm -f lint.log

distclean: clean
	rm -rf build dist MANIFEST cachedir 
	@$(MAKE) -C doc clean


help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "Build Commands"
	@echo "  build		to build module"
	@echo "  dist		to build windows installer"
	@echo "Developmend Commmands"
	@echo "  docs           to generate documentation"
	@echo "  test		to run unit tests"
	@echo "  clean		to run cleaner" 
	@echo "  distclean	to make a good clean"


