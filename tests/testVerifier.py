import pytest
from awsVerifier import verify_aws_policy

@pytest.fixture
def base_policy_data(): # example data for a policy
    return {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ]
                }
            ]
        }
    }

def test_verify_resource_missing(base_policy_data):
    if "Resource" in base_policy_data["PolicyDocument"]["Statement"][0]:
        del base_policy_data["PolicyDocument"]["Statement"][0]["Resource"] # remove the resource key, should return True
    assert verify_aws_policy(base_policy_data) == True

def test_verify_resource_true(base_policy_data):
    base_policy_data["PolicyDocument"]["Statement"][0]["Resource"] = "SomeResource" # add a resource not equal to "*", should return True
    assert verify_aws_policy(base_policy_data) == True

def test_verify_resource_false(base_policy_data):
    base_policy_data["PolicyDocument"]["Statement"][0]["Resource"] = "*" # add a resource equal to "*", should return False
    assert verify_aws_policy(base_policy_data) == False

def test_verify_resource_true_file():
    assert verify_aws_policy("tests/testTrue.json") == True # file contains a resource not equal to "*", should return True

def test_verify_resource_false_file():
    assert verify_aws_policy("tests/testFalse.json") == False # file contains a resource equal to "*", should return False

def test_verify_resource_missing_file():
    with pytest.raises(FileNotFoundError):
        verify_aws_policy("testWrongFilePath.json") # file does not exist, should raise FileNotFoundError

def test_verify_wrong_format():
    with pytest.raises(KeyError):
        verify_aws_policy("tests/testWrongFormat.json") # file contains wrong json format, should raise KeyError