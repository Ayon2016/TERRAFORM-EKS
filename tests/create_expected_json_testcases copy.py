import json

def find_name_values(json_data):
    name_values = {}

    def find_names(obj):
        nonlocal name_values
        if isinstance(obj, dict):
            if "resource_changes" in obj:
                if isinstance(obj["resource_changes"], list):
                    for resource in obj["resource_changes"]:
                        if "name" in resource and "address" in resource:
                            resource_address = resource["address"]
                            resource_name = resource["name"]
                        name_values[resource_name] = resource_address
            for value in obj.values():
                find_names(value)

        elif isinstance(obj, list):
            for item in obj:
                find_names(item)

    data = json.loads(json_data)
    find_names(data)
    return name_values

# change path to the actual path of the planoutput.json
with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/cluster_planoutput.json") as f:
    json_data = f.read()

name_values = find_name_values(json_data)

# creates expectedResources.json
with open('expectedResources_coded.json', 'w') as f:
    json.dump(name_values, f)

# Writes the test cases
with open('testcases.txt', 'w') as f:
    for key, value in name_values.items():  
        f.write(f"Verify that the resource name '{key}' of type '{value}' exists in the Terraform code\n")
