VENV = .venv
REQ = requirements.txt
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
SHELL_NAME=$(basename "$SHELL")


install: $(VENV)/bin/activate
	$(PIP) install --upgrade pip -q
	$(PIP) install -r $(REQ)

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

run:
	$(PYTHON) main.py

debug:
	$(PYTHON) -m pyb main.py

flake:
	$(FLAKE) --exclude=$(VENV) .

lint: flake
	$(MYPY)  . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	find . -name "*.pyc" -exec rm -rf {} +
	find . -type d \( -name "__pycache__" -o -name ".mypy_cache" \) -exec rm -rf {} +

fclean: clean
	rm -rf $(VENV)

.PHONY: run debug flake lint clean fclean install
