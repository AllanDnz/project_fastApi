run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@echo Current directory: %cd%
	@echo PYTHONPATH before: %PYTHONPATH%
	@set "PYTHONPATH=%PYTHONPATH%;%cd%" && echo PYTHONPATH after: %PYTHONPATH% && alembic revision --autogenerate -m "$(d)"

run-migrations:
	@echo Current directory: %cd%
	@echo PYTHONPATH before: %PYTHONPATH%
	@set "PYTHONPATH=%PYTHONPATH%;%cd%" && echo PYTHONPATH after: %PYTHONPATH% && alembic upgrade head

