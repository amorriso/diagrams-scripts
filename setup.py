from setuptools import setup, find_packages

setup(
    name='diagrams_aws_package',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'diagrams_aws=diagrams_aws_package.diagrams_aws:entry_point_wrapper',
        ],
    },
    install_requires=[
        'diagrams',
    ],
    author='TMo',
    author_email='nevergonnagiveyouup@rickrolled.com',
    description='An installable package for AWS diagrams script.',
    keywords='AWS diagrams',
)
