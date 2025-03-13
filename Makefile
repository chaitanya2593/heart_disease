.PHONY: test
test:
	coverage run -m pytest --junitxml=pytest_results.xml --html=pytest_results.html --self-contained-html --alluredir pytest_allure
	# call the coverage target
	@$(MAKE) coverage

.PHONY: coverage
coverage:
	coverage report --show-missing --skip-empty
	coverage xml
	coverage html -d coverage_html


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist