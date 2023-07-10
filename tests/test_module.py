import pytest
import json
from tftest import TerraformPlanOutput

#Fixture 1 to read the actual plan output for resource changes
@pytest.fixture
def actual_output():
    with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/planoutput.json", "r") as file:
        raw_data = file.read()
        json_data = json.loads(raw_data)

    # resource changes
    plan_data = TerraformPlanOutput(json_data)
    yield plan_data

#Fixture 2 to read the expected output json
@pytest.fixture
def expected_output():
    with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/tests/expectedResources.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
    yield data

#test eip
def test_eip_exists(actual_output, expected_output):
    key = "eip_name"
    if key in expected_output:
        value = expected_output[key]
    assert value in actual_output.resource_changes

#test vpc exists
def test_nodeGroup_exists(actual_output, expected_output):
    key = "nodegroup_name"
    if key in expected_output:
        value = expected_output[key]
    assert value in actual_output.resource_changes



