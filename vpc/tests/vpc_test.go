package vpc

import (
	"fmt"
	"os"
	"path/filepath"
	"testing"

	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

var terraformOutput string

func TestIAMPoliciesWorkerNodes(t *testing.T) {
	t.Parallel()
	//Get The Present Working Directory
	pwd, _ := os.Getwd()

	//Saves Plan Output Json to this location
	planFilePath := filepath.Join(pwd, "plan.out")

	//Directory Path and plan filePath
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		TerraformDir: "/Users/ayon.choudhury/Desktop/Terraform-EKS",
		PlanFilePath: planFilePath,
	})

	//Gets the terraform plan output as a struct so that maps can be traversed
	planOutput := terraform.InitAndPlanAndShowWithStruct(t, terraformOptions)
	fmt.Println(planOutput)

	//Checks if the maps exist
	terraform.RequirePlannedValuesMapKeyExists(t, planOutput, "aws_iam_role_policy_attachment.node_AmazonEKSWorkerNodePolicy")
	workerNodePolicy := planOutput.ResourcePlannedValuesMap["aws_iam_role_policy_attachment.node_AmazonEKSWorkerNodePolicy"]
	workerNodePolicyName := workerNodePolicy.AttributeValues["policy_arn"]

	//Assertions
	assert.Equal(t, workerNodePolicyName, "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy")
}
