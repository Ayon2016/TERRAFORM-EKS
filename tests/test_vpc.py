import json
import pytest


class Test:
    def test_find_value_recursive(self):
        # Open the JSON file
        with open('/Users/ayon.choudhury/Desktop/Terraform-EKS/tests/results_json.json', 'r') as file:
            # Load the JSON data
            json_data = json.load(file)

        # Define the value to search for
        search_value = 'aws_subnet.private'

        # Find keys recursively using the value
        values = self.find_value_recursive(json_data, search_value)

        assert len(values)==1

    def find_value_recursive(self, data, search_value):
        results = []

        def search_json(data, value):
            if isinstance(data, dict):
                for v in data.values():
                    if v == value:
                        results.append(v)
                    elif isinstance(v, (dict, list)):
                        search_json(v, value)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, (dict, list)):
                        search_json(item, value)

        search_json(data, search_value)
        return results


if __name__ == '__main__':
    pytest.main([__file__])