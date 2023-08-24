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
    
    #test cluster resource exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "aws_eks_cluster.this"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test cluster sg exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "aws_security_group.cluster"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test that the data block aws_eks_cluster.lookup exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "aws_eks_cluster.lookup"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test that the aws_launch_template.templates exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "aws_launch_template.templates"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test that the node group for dataplane exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "aws_eks_node_group.workers"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test that the random_pet.node_groups exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "random_pet.node_groups"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output

    #test that the null_resource.applicationset_cluster exists
    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_eks_cluster_exists(self, actual_output, expected_output):
        key = "null_resource.applicationset_cluster"
        global value
        if key in expected_output:
            value = expected_output[key]
        assert value in actual_output