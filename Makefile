PYTHONPATH= .
SHELL := /bin/bash

USER_NAME := $(shell whoami)
PYTHON_VERSION=$(shell python3 -c 'import sys; print("{0}.{1}".format(sys.version_info[0], sys.version_info[1]))')
PYTHON_PATH=$(shell which python3)


CURRENT_DIRECTORY:=$(shell pwd)
INSTALL_DIRECTORY:=$(CURRENT_DIRECTORY)/.venv
TEST_DIRECTORY:=$(CURRENT_DIRECTORY)/tests
EXEC_PATH:=$(INSTALL_DIRECTORY)/bin/

# Commands
PIP := $(EXEC_PATH)pip
PYTHON := $(EXEC_PATH)python3
PYTEST := $(PYTHON) -m pytest
FLAKE := $(EXEC_PATH)flake8
UVICORN := $(EXEC_PATH)uvicorn
VENV:= python3 -m venv

variables := PYTHONPATH  USER_NAME PYTHON_VERSION PYTHON_PATH CURRENT_DIRECTORY INSTALL_DIRECTORY TEST_DIRECTORY EXEC_PATH 

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
    %help; \
    while(<>) { push @{$$help{$$2 // 'Targets'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
    print "Usage: make [target]\n\n"; \
    for (sort keys %help) { \
    print "${WHITE}$$_:${RESET}\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (32 - length $$_->[0]); \
    print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
    }; \
    print "\n"; }

help: ##@Help Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)
	@IFS=$$'\n' ; printf " ${YELLOW}%-28s ${GREEN}%s\n${RESET}" "Variables" ; 
	@for variable in $(variables) ; do \
  		$(eval export $(variable)) \
		printf " ${YELLOW}%-28s ${GREEN}%s\n${RESET}" "$$variable" "$${!variable}" ; \
	done

setup:
	$(VENV) $(CURRENT_DIRECTORY)/.venv

deps:setup
	@$(PIP) install -r requirements.txt

test:
	$(PYTEST) $(TEST_DIRECTORY)  -W ignore::DeprecationWarning

lint: ##@Lint Check codebase with flake8
	$(FLAKE) .  --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=.venv &\
	$(FLAKE) .  --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=.venv


train:
	$(PYTHON) starter/train_model.py

api:
	$(UVICORN) main:app --reload