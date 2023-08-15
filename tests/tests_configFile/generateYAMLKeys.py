import yaml

with open("/Users/ayon.choudhury/Desktop/Terraform-EKS/addon_actual.tfpl", "r") as file:
        raw_data = file.read()
        parsed_file_actual = yaml.safe_load(raw_data)

# Function to replace values with None
def remove_values(structure):
    if isinstance(structure, dict):
        return {key: remove_values(value) if isinstance(value, (dict, list)) else None for key, value in structure.items()}
    elif isinstance(structure, list):
        return [remove_values(item) for item in structure]
    else:
        return ''

# Remove values from the parsed content
modified_content = remove_values(parsed_file_actual)

# Write the modified content to a new YAML file
with open('keys.yaml', 'w') as outfile:
    yaml.dump(modified_content, outfile, default_flow_style=False)

print("Modified YAML written to keys.yaml")