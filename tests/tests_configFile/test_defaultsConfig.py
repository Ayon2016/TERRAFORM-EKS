import yaml
import pytest

#Fixture 1 to read the new addon.tftpl file and yield as a yaml
@pytest.fixture()
def actual_addonConfig():
    with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/addon_actual.tfpl", "r") as file:
        raw_data = file.read()
        parsed_file_actual = yaml.safe_load(raw_data)
    yield parsed_file_actual

#Fixture 2 to read the expected keys.yaml file
@pytest.fixture()
def expected_addOnConfig():
    with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/keys.yaml', 'r') as file:
        raw_data = file.read()
        parsed_file_expected = yaml.safe_load(raw_data)
    yield parsed_file_expected

# Test # 1 to check all operator Keys Exist
def test_that_all_operators_exist(actual_addonConfig, expected_addOnConfig):
    actualOperatorKeys = actual_addonConfig.get('operators', {}).keys()
    expectedOperatorKeys = expected_addOnConfig.get('operators', {}).keys() 
    assert all(key in expectedOperatorKeys for key in actualOperatorKeys)

#Test # 2 to check whether the attribute keys match for each operator
def test_that_all_attributes_exist_within_keys(actual_addonConfig, expected_addOnConfig):
    for key, value in expected_addOnConfig.get('operators', {}).items():
        #print(value)
        if isinstance(value, dict):
            expectedOperatorValueKeys = set(value.keys())
            actualOperatorValueKeys = set(actual_addonConfig.get('operators', {}).get(key, {}).keys())
            assert expectedOperatorValueKeys == actualOperatorValueKeys, f"Keys mismatch for '{key}'"
            for inner_key, inner_value in value.items():
                if isinstance(inner_value, dict):
                    expectedInnerValueKeys = set(inner_value.keys())
                    actualInnerValueKeys = set(actual_addonConfig.get('operators', {}).get(key, {}).get(inner_key, {}).keys())
                    assert expectedInnerValueKeys == actualInnerValueKeys, f"Keys mismatch for '{key}' -> '{inner_key}'"

