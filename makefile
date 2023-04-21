# Makefile

# Define variables
VENV_NAME := venv
PYTHON := python3
PIP := $(VENV_NAME)/bin/pip
OS := $(shell uname -s)

# Update virtual environment command based on OS
ifeq ($(OS),Darwin)
	VENV_CMD := python3 -m venv $(VENV_NAME)
else ifeq ($(OS),Linux)
	VENV_CMD := python3 -m venv $(VENV_NAME)
else ifeq ($(OS),Windows_NT)
	VENV_CMD := python -m venv $(VENV_NAME)
else
	$(error Unsupported OS: $(OS))
endif

# Default target
all: install

# Create virtual environment
venv:
	@echo "Checking if virtual environment exists..."
	@if [ ! -d "$(VENV_NAME)" ]; then \
		echo "Creating virtual environment..."; \
		$(VENV_CMD); \
	else \
		echo "Virtual environment already exists."; \
	fi

# Install dependencies
install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

# Run tests
test: venv
	@echo "Running tests..."
	$(PYTHON) -m unittest discover test

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)

# Linters
lint: venv
	@echo "Running pylint and flake8..."
	$(VENV_NAME)/bin/pylint src/
	$(VENV_NAME)/bin/flake8 src/

format:
	@echo "Running autopep8..."
	$(VENV_NAME)/bin/autopep8 --in-place --recursive src/



.PHONY: venv install test clean lint
