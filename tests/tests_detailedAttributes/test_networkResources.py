
import json
from tftest import TerraformPlanOutput
import pytest

class TestNetworkResourcesFromPlanOutput:

    @pytest.mark.usefixtures("actual_output", "expected_output_attributes")
    def test_ingress_rule_cidr_in_security_groups(self, actual_output, expected_output_attributes):
        for key, value in expected_output_attributes["data"]["network_resources"]["security_groups"].items():
            ingress_cidr_in_expected_file = value["ingress"]["cidr_blocks"]
            print(ingress_cidr_in_expected_file)    
        for key1, value1 in actual_output.items():
            if value1["name"] == key:
                for attributes in value1["change"]["before"]["ingress"]:
                    ingress_cidr_in_actual_file = attributes["cidr_blocks"]
                    print(ingress_cidr_in_actual_file)  
                    for ip in ingress_cidr_in_expected_file:
                        assert ip in ingress_cidr_in_actual_file
