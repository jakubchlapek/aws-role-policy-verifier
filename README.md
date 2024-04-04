# aws-role-policy-verifier
 Method reading from a json and asserting whether the "Resource" key contains a single asterisk. Complete with unit tests.

# Usage
To use, either specify the file path or provide a dictionary for the method call as an argument in main.py.

# Tests
For testing, run the following command in the project directory.
```
pytest ./testVerifier.py
```

# Run locally
1. Clone the project
```
git clone https://github.com/jakubchlapek/aws-role-policy-verifier.git
```
2. Provide the arguments for the method call, then run main.py