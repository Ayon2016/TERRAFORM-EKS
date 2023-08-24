
import json
from tftest import TerraformPlanOutput
import pytest

class TestIamRolesFromPlanOutput:

    @pytest.mark.usefixtures("actual_output", "expected_output_attributes")
    def test_that_policy_arn_value_for_iam_roles_match(self, actual_output, expected_output_attributes):
        for key, value in expected_output_attributes["data"]["iam_roles"].items():
            policy_arn_expected = str(value["policy_arn"])
            for key1, value1 in actual_output.items():
                if value1["name"] == key:
                    policy_arn_actual = str(value1["change"]["before"]["policy_arn"])
                    assert  policy_arn_expected == policy_arn_actual