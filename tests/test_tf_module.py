import pytest
import json
from tftest import TerraformPlanOutput

#Fixture 1 to read the actual plan output for resource changes
@pytest.fixture
def actual_output():
    with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/cluster_planoutput.json", "r") as file:
        raw_data = file.read()
        json_data = json.loads(raw_data)

    # resource changes
    plan_data = TerraformPlanOutput(json_data)
    print(plan_data.resource_changes)
    yield plan_data

#Fixture 2 to read the expected output json
@pytest.fixture
def expected_output():
    with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/expectedResources_coded.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
    yield data

#test coredns addon exists
def test_that_coredns_addon_exists(actual_output, expected_output):
    key = "coredns"
    if key in expected_output:
        value = expected_output[key]
    assert value in actual_output.resource_changes
    #assert value in actual_output

#test app_of_apps exists
def test_that_appofApps_helmRelease_exists(actual_output, expected_output):
    key = "app_of_apps"
    if key in expected_output:
        value = expected_output[key]
    assert value in actual_output.resource_changes
    #assert value in actual_output.resource_changes


