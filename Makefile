install:
	poetry install
	
brain-games:
	poetry run brain-games
	
brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 --max-line-length=120 brain_games
