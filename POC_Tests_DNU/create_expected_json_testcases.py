import json

def find_name_values(json_data):
    name_values = []

    def find_names(obj):
        if isinstance(obj, dict):
            if "resource_changes" in obj:
                if isinstance(obj["resource_changes"], list):
                    for resource in obj["resource_changes"]:
                        if "name" in resource:
                            name_values.append(resource["name"])
            for value in obj.values():
                find_names(value)

        elif isinstance(obj, list):
            for item in obj:
                find_names(item)

    data = json.loads(json_data)
    find_names(data)
    return name_values

with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/cluster_plan.json") as f:
    json_data = f.read()

name_values = find_name_values(json_data)

with open('name_values.json', 'w') as f:
    json.dump(name_values, f)

with open ('testcases.txt', 'w') as f:
    for value in name_values:
        f.write("Verify that the resource name '" + value + "' exists in the terraform code \n" )

#print("Values of 'name' instances:", name_values)
