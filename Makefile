.PHONY: setup run compare clean

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

setup:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install pip-tools uv matplotlib

check_venv:
	@if [ ! -f .venv/bin/python ]; then \
		echo "Virtual environment not found. Please run 'make venv' first."; \
		exit 1; \
	fi

run: check_venv
	$(PYTHON) compare_tools.py

compare: run
	@echo "Comparison complete. Check tool_comparison.png for results."

clean:
	rm -rf $(VENV)
	rm -f requirements-pip.txt requirements-uv.txt tool_comparison.png
