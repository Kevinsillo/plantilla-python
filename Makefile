DEPLOYMENT_IP = 
DEPLOYMENT_PATH = 
DEPLOYMENT_TEST = $(DEPLOYMENT_PATH)-test
DEPLOYMENT_FILES = src vendor scripts main.py requirements.txt
DEPLOYMENT_USER = $(shell whoami)

# VARIABLES
VENV_DIR = .venv
POETRY_RUN = poetry run python
PYTHON_VERSION = 3.10

venv:
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "$(GREEN)Virtual environment already exists in $(VENV_DIR)$(RESET)"; \
	else \
		echo "$(GREEN)Creating virtual environment in $(VENV_DIR)...$(RESET)"; \
		python -m venv $(VENV_DIR); \
	fi

install: venv
	@echo "$(GREEN)Installing dev requirements...$(RESET)"
	@poetry add python-dotenv pretty-errors
	@poetry add --dev mypy black pytest
	@poetry install
	@poetry self add poetry-plugin-export
	@poetry config virtualenvs.in-project true
	@poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

clean:
	@echo "$(YELLOW)Cleaning venv...$(RESET)"
	@rm -rf $(VENV_DIR)

test:
	@echo "$(GREEN)Running tests...$(RESET)"
	@$(POETRY_RUN) -m unittest tests/* -v

prettier:
	@echo "$(GREEN)Running checks...$(RESET)"
	@$(POETRY_RUN) prettier.py || { echo "$(RED)Mypy found errors! Aborting.$(RESET)"; exit 1; }
	@echo "$(GREEN)All checks passed$(RESET)"

env_example:
	@echo "$(GREEN)Creating .env.example file...$(RESET)"
	@cp .env .env.example && sed -i 's/=.*/=/g' .env.example

# COLORS
RED		:= $(shell tput -Txterm setaf 1)
GREEN	:= $(shell tput -Txterm setaf 2)
YELLOW	:= $(shell tput -Txterm setaf 3)
RESET	:= $(shell tput -Txterm sgr0)