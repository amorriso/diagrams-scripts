import argparse
import json
from diagrams import Diagram
from diagrams.aws.compute import EC2, Lambda, ECS
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import VPC, Route53
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM, Cognito
from diagrams.aws.ml import Sagemaker
from diagrams.aws.analytics import Kinesis
from diagrams.aws.management import Cloudwatch
# Add other imports as needed

# Resource mapping remains the same
resource_mapping = {
    "aws_ec2_instance": EC2,
    "aws_lambda_function": Lambda,
    "aws_ecs_cluster": ECS,
    "aws_rds_instance": RDS,
    "aws_dynamodb_table": Dynamodb,
    "aws_vpc": VPC,
    "aws_route53_zone": Route53,
    "aws_sqs_queue": SQS,
    "aws_sns_topic": SNS,
    "aws_s3_bucket": S3,
    "aws_iam_role": IAM,
    "aws_iam_policy": IAM,
    "aws_iam_user": IAM,
    "aws_cognito_user_pool": Cognito,
    "aws_sagemaker_notebook_instance": Sagemaker,
    "aws_kinesis_stream": Kinesis,
    "aws_cloudwatch_metric_alarm": Cloudwatch,
    # Extend with more mappings
}

def load_terraform_state(state_file):
    with open(state_file) as file:
        return json.load(file)

def extract_and_map_resources(state, mappings):
    resources = {}
    for resource in state.get("values", {}).get("root_module", {}).get("resources", []):
        resource_type = resource.get("type")
        if resource_type in mappings:
            if resource_type not in resources:
                resources[resource_type] = []
            resource_name = resource.get("values", {}).get("id")
            if resource_name:
                resources[resource_type].append(resource_name)
    return resources

def create_diagram(resources, mappings, output_filename):
    with Diagram(output_filename, show=False):
        nodes = {}
        for resource_type, names in resources.items():
            node_type = mappings.get(resource_type)
            if not node_type:
                continue  # Skip unsupported types
            nodes[resource_type] = [node_type(name) for name in names]

        # Example: Connect first of each type (if exists)
        previous_nodes = []
        for resource_type, node_list in nodes.items():
            if previous_nodes:
                for node in node_list:
                    for prev_node in previous_nodes:
                        prev_node >> node
            previous_nodes = node_list

def main(input_file, output_file):

    # Remove the file extension if it exists
    if output_file.endswith(".png") or \
            output_file.endswith(".jpg") or \
            output_file.endswith(".svg"):
        output_file = output_file[:-4]

    # Load Terraform state using the provided file path
    state = load_terraform_state(input_file)

    # Extract and map resources from state
    resources = extract_and_map_resources(state, resource_mapping)

    # Create the diagram, now also passing the output file name
    create_diagram(resources, resource_mapping, output_file)

def entry_point_wrapper():
    parser = argparse.ArgumentParser(description='Generate AWS infrastructure diagram from Terraform state file.')
    parser.add_argument('--input', '-i', required=True, help='Path to the Terraform state file in JSON format.')
    parser.add_argument('--output', '-o', required=True, help='Output filename for the diagram without extension.')

    args = parser.parse_args()

    # Call main with the processed input and output arguments
    main(args.input, args.output)

if __name__ == "__main__":
    entry_point_wrapper()

