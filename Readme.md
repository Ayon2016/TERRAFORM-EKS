# Installations

pip install tftest
pip install pytest
pip install pytest-html

# Test Files

There are 2 files in this project under "tests" folder that is being used for the component tetsing poc

1. create_expected_json_testcases.py: This file is parsing the planoutput.json from cluster workspace and creating the test cases + expectedresources.json
   The test cases are under Terraform-EKS/testcases.txt file and the expectedresources.json is Terraform-EKS/expectedResources_coded.json

2. the test_tf_module.py: This file reads the expectedResources_coded.json and the actual planoutput.json and asserts that the resources on expected are there in actual

# Run tests

cd tests
pytest test_tf_module.py --html=report.html --self-contained-html
