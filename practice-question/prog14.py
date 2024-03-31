import boto3

def list_vpcs():
    """
    Function to list all VPCs in the AWS account.
    """
    # Initialize the Boto3 client for EC2 service
    ec2_client = boto3.client('ec2')

    # Describe all VPCs
    response = ec2_client.describe_vpcs()

    # Extract and return VPC details
    return response['Vpcs']

def describe_vpc(vpc_id):
    """
    Function to describe a specific VPC using its ID.
    
    :param vpc_id: ID of the VPC to describe.
    """
    # Initialize the Boto3 client for EC2 service
    ec2_client = boto3.client('ec2')

    # Describe the specified VPC
    response = ec2_client.describe_vpcs(
        VpcIds=[
            vpc_id,
        ]
    )

    # Return the details of the VPC
    return response['Vpcs'][0] if response['Vpcs'] else None

# Example usage:
# List all VPCs
all_vpcs = list_vpcs()
print("List of all VPCs:")
for vpc in all_vpcs:
    print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}")

# Describe a specific VPC
if all_vpcs:
    vpc_id_to_describe = all_vpcs[0]['VpcId']  # Choose the first VPC for demonstration
    print("\nDescribing VPC with ID:", vpc_id_to_describe)
    vpc_details = describe_vpc(vpc_id_to_describe)
    if vpc_details:
        print("VPC Details:", vpc_details)
    else:
        print("VPC not found.")
else:
    print("No VPCs found.")
