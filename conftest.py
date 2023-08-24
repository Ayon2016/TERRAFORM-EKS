import pytest
import json
from tftest import TerraformPlanOutput

#Fixture 1 to read the actual plan output for resource changes
@pytest.fixture(scope="class")
def actual_output():
    with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/cluster_planoutput.json", "r") as file:
        raw_data = file.read()
        json_data = json.loads(raw_data)

    # resource changes
    plan_data = TerraformPlanOutput(json_data)
    #print(plan_data.resource_changes)
    yield plan_data.resource_changes

#Fixture 2 to read the expected output json
@pytest.fixture(scope="class")
def expected_output():
    with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/expectedResources_coded.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
    yield data

#Fixture 3 to read the expected output json for detailed resources
@pytest.fixture(scope="class")
def expected_output_attributes():
    with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/expectedResource_values_us-east-1.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)
        #print (data)
    yield data

def pytest_html_report_title(report):
	''' modifying the title of html report'''
	report.title = "Terraform Conifg Tests"



