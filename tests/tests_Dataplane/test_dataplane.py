from conftest import actual_output, expected_output  # Import the fixtures from conftest
import pytest

class TestDataplaneResourceInConfig:

    value = ""

    #test cluster name tag for subnet 1
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_ec2tag_clusternametag_exists(self, actual_output, expected_output):
        key = "aws_ec2_tag.cluster_name_tag"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output

    #test cluster name tag for subnet 2
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_ec2tag_clusternametag_subnet_exists(self, actual_output, expected_output):
        key = "aws_ec2_tag.cluster_name_tag.subnet-04eb74705cd4f279a"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output.resource_changes