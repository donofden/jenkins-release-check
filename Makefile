.DEFAULT_GOAL := explain
explain:
	### Welcome
	#
	### Check jenkins version
	#
	# Check jenkins version is up to date
	#  -> $$ make jenkins-version-check
	#
	### Targets
	#
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: jenkins-version-check
jenkins-version-check: ## Check Jenkins Version
	python jenkins.py

.PHONY: install-python-deps
install-python-deps: ## Install Python Dependencies
	pip install -r requirements.txt
