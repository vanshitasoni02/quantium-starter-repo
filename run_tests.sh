#Activate virtual environment
source .venv/Scripts/activate

#run tests
pytest

#Exit with pytest's exit code
exit $?