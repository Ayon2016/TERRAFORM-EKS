from conftest import actual_output, expected_output  # Import the fixtures from conftest
import pytest

class TestNetworkResourceInConfig:

    value = ""

    #test public ingress exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_coredns_addon_exists(self, actual_output, expected_output):
        key = "aws_security_group.public_ingress"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output

    #test public_ingress_backend exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_appofApps_helmRelease_exists(self, actual_output, expected_output):
        key = "aws_security_group.public_ingress_backend"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output.resource_changes