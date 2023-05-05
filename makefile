#!/usr/bin/env make

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    PYTHON ?= python3
else
    PYTHON ?= py
endif

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:

# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d venv ] || $(PYTHON) -m venv venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". venv/bin/activate\n"
	@printf "On Windows Command Prompt, do:\n"
	@printf "    .\venv\Scripts\activate.bat\n"
	@printf "On Windows PowerShell, do:\n"
	@printf "    .\venv\Scripts\Activate.ps1\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv

# ---------------------------------------------------------
# Work with static code linters.
#
.PHONY: lint pylint flake8
pylint:
	@$(call MESSAGE,$@)
	-cd src && $(PYTHON) -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-cd src && $(PYTHON) -m flake8

lint: flake8 pylint

# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black .

codestyle: black

# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	$(PYTHON) -m unittest discover -s test/

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover test/
	coverage html
	coverage report -m

test: lint coverage

# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	# This does not work on Windows installed Python
	$(PYTHON) -m pydoc -w "$(PWD)"
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc .

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse *.py -a

.PHONY: format
format:
	autopep8 --in-place --recursive src/*.py

