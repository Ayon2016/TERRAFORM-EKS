from conftest import actual_output, expected_output  # Import the fixtures from conftest
import pytest

class TestNetworkResourceInConfig:

    value = ""

    # 1 test security group public ingress exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_coredns_addon_exists(self, actual_output, expected_output):
        key = "aws_security_group.public_ingress"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output

    # 2 test security group public_ingress_backend exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_appofApps_helmRelease_exists(self, actual_output, expected_output):
        key = "aws_security_group.public_ingress_backend"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
        #assert value in actual_output.resource_changes
    
    # 3 test security group aws_security_group.workers exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgWorkers_exists(self, actual_output, expected_output):
        key = "aws_security_group.workers"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 4 test aws_security_group_rule.cluster_egress_internet exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_clusteregressinternet_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.cluster_egress_internet"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 5 test aws_security_group_rule.cluster_https_management_https exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_clusterhttpsmgmnt_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.cluster_https_management_https"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 6 test aws_security_group_rule.cluster_https_worker_ingress exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_cluster_https_worker_ingress_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.cluster_https_worker_ingress"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 7 test aws_security_group_rule.public_ingress_backend_egress_internet exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_public_ingress_backend_egress_internet_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.public_ingress_backend_egress_internet"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 8 test aws_security_group_rule.public_ingress_egress_internet exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_public_ingress_egress_internet_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.public_ingress_egress_internet"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 9 test aws_security_group_rule.public_ingress_public_cidr exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_public_ingress_public_cidr_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.public_ingress_public_cidr"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 10 test aws_security_group_rule.workers_egress_internet exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_egress_internet_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_egress_internet"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 11 test aws_security_group_rule.workers_ingress_alb exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_ingress_alb_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_ingress_alb"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 12 test aws_security_group_rule.workers_ingress_cluster exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_ingress_cluster_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_ingress_cluster"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 13 test aws_security_group_rule.workers_ingress_cluster_https exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_ingress_cluster_https_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_ingress_cluster_https"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 14 test aws_security_group_rule.workers_ingress_management_ssh exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_ingress_management_ssh_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_ingress_management_ssh"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 15 test aws_security_group_rule.workers_ingress_self exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_awssgrule_workers_ingress_self_exists(self, actual_output, expected_output):
        key = "aws_security_group_rule.workers_ingress_self"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 16 test aws_wafv2_ip_set.ipset exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_aws_wafv2_ip_set_ipset_exists(self, actual_output, expected_output):
        key = "aws_wafv2_ip_set.ipset"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    # 17 test aws_wafv2_web_acl.this exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_aws_wafv2_web_acl_this_exists(self, actual_output, expected_output):
        key = "aws_wafv2_web_acl.this"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output
    
    # 18 test aws_wafv2_web_acl_logging_configuration.main exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_aws_wafv2_web_acl_logging_configuration_main_exists(self, actual_output, expected_output):
        key = "aws_wafv2_web_acl_logging_configuration.main"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output