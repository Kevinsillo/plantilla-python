DEPLOYMENT_IP = 
DEPLOYMENT_PATH = 
DEPLOYMENT_TEST = $(DEPLOYMENT_PATH)-test
DEPLOYMENT_FILES = src vendor scripts main.py
DEPLOYMENT_USER = $(shell whoami)

# VARIABLES PYTHON
VENV_DIR = venv
PIP = $(VENV_DIR)/bin/pip
PYTHON = $(VENV_DIR)/bin/python

venv:
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "$(GREEN)Virtual environment already exists in $(VENV_DIR)$(RESET)"; \
	else \
		echo "$(GREEN)Creating virtual environment in $(VENV_DIR)...$(RESET)"; \
		python -m venv $(VENV_DIR); \
	fi

install: venv
	@echo "$(GREEN)Installing dev requirements...$(RESET)"
	@$(PIP) install -r requirements-dev.txt

install_prod: venv
	@echo "$(GREEN)Installing requirements...$(RESET)"
	@$(PIP) install -r requirements.txt

clean:
	@echo "$(YELLOW)Cleaning venv...$(RESET)"
	@rm -rf $(VENV_DIR)

env_example:
	@echo "$(GREEN)Creating .env.example file...$(RESET)"
	@cp .env .env.example && sed -i 's/=.*/=/g' .env.example

test:
	@echo "$(GREEN)Running tests...$(RESET)"
	@$(PYTHON) -m unittest tests/* -v

check:
	@echo "$(GREEN)Running checks...$(RESET)"
	@$(PYTHON) prettier.py || { echo "$(RED)Mypy found errors! Aborting.$(RESET)"; exit 1; }
	@echo "$(GREEN)All checks passed$(RESET)"

deploy: env_example test check clean install_prod
	@echo "$(GREEN)Deploying...$(RESET)"
	@rsync -zrPLp --chmod=ug=rwX,o=rX --delete $(DEPLOYMENT_FILES) $(DEPLOYMENT_USER)@$(DEPLOYMENT_IP):$(DEPLOYMENT_PATH)
	$(MAKE) clean
	$(MAKE) install

test_deploy: env_example test check clean install_prod
	@echo "$(GREEN)Deploying to test...$(RESET)"
	@rsync -zrPLp --chmod=ug=rwX,o=rX --delete $(DEPLOYMENT_FILES) $(DEPLOYMENT_USER)@$(DEPLOYMENT_IP):$(DEPLOYMENT_TEST)
	$(MAKE) clean
	$(MAKE) install

# COLORS
RED		:= $(shell tput -Txterm setaf 1)
GREEN	:= $(shell tput -Txterm setaf 2)
YELLOW	:= $(shell tput -Txterm setaf 3)
RESET	:= $(shell tput -Txterm sgr0)