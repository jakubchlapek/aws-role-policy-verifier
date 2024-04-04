import json

def verify_aws_policy(role_policy_data: dict | str) -> bool:
    """
    Verify if the policy contains a resource that is not equal to "*"

    Parameters: 
    role_policy_data (dict | str): The policy data to verify as a dictionary or a file path to a JSON file

    Returns:
    bool: True if the policy contains a resource that is not equal to "*", False in any other case
    """
    if isinstance(role_policy_data, str): # check if the data is a file path to convert it to a dictionary and if it exists
        try:
            with open(role_policy_data, "r") as file:
                role_policy_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found. Please provide a valid file path.")
        
    if ("PolicyDocument" or "PolicyName") not in role_policy_data: # check if the data is in the correct AWS::IaM::RolePolicy format
        raise KeyError("PolicyDocument or PolicyName key not found in the policy data. Please provide valid policy data.")
    
    try: # check if the resource is equal to "*" or there is no resource
        if role_policy_data["PolicyDocument"]["Statement"][0]["Resource"] == "*":
            return False
    except KeyError:
        pass
    return True

