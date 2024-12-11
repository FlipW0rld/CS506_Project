# Define your virtual environment
VENV = venv

# Install dependencies from requirements.txt
install:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt
	./$(VENV)/bin/pip install notebook

notebook:
	./$(VENV)/bin/jupyter notebook

# Clean up virtual environment
clean:
	rm -rf $(VENV)

# Reinstall all dependencies
reinstall: clean install
