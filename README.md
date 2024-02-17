# diagrams_aws_package

This package provides a command-line tool to generate AWS infrastructure diagrams from Terraform state files. It leverages the `diagrams` Python library to create a visual representation of your AWS resources as defined in a Terraform state file.

## Installation

To install `diagrams_aws_package`, clone this repository and run the following command in the root directory:

```bash
pip install .
```

This will install the package and its dependencies, making the `diagrams_aws` command available in your environment.

## Usage

After installation, you can generate a diagram by running:

```bash
diagrams_aws --input <path_to_your_terraform_state_json> --output <output_filename_without_extension>
```

- `--input` or `-i`: Specifies the path to the Terraform state file in JSON format.
- `--output` or `-o`: Specifies the base name for the output file (without extension). The diagram will be saved in the PNG format.

## Requirements

- Python 3.6+
- `diagrams` library

## Development

To contribute to `diagrams_aws_package` or modify it for your use case:

1. Clone the repository.
2. Make your changes in the `diagrams_aws_package` directory.
3. Run `pip install -e .` in the root directory to install the package in editable mode.

## Contact

For questions or feedback, please reach out to nevergonnagiveyouup@rickrolled.com.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
