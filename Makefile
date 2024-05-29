run_api:
	uvicorn better_letter.API.fast:app --reload

reinstall_package:
	@pip uninstall -y betterletter || :
	@pip install -e .
