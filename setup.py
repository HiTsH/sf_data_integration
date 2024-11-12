from setuptools import setup, find_packages

setup(
    name="sf_data_integration",
    version="0.2.0",  # Updated version
    packages=find_packages(),
    install_requires=[
        "pandas==2.1.1",  # Data manipulation library
        "simple-salesforce==1.11.4",  # Salesforce API wrapper
        "pytest==7.4.0",  # Testing framework
        "PyYAML==6.0",  # For YAML configuration files
        "requests==2.28.2",  # For API requests, including Salesforce REST API
        "python-dotenv==1.0.0",  # For environment variable management (if used)
        "boto3==1.26.8",  # For AWS SDK support (if applicable)
        "google-cloud==0.34.0",  # For Google Cloud SDK support (if applicable)
        "sqlalchemy==2.1.0",  # For SQLAlchemy ORM and database connectivity
        "psycopg2==2.9.3",  # PostgreSQL database connector
        "openpyxl==3.1.1",  # For handling Excel files
        "loguru==0.6.0",  # For advanced logging (optional)
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for integrating data from various sources into Salesforce and Salesforce Data Cloud services",
    long_description=open("README.md").read(),  # Automatically include the long description from README
    long_description_content_type="text/markdown",  # Specifies the format of the long description
    url="https://github.com/yourusername/sf_data_integration",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.6',  # Ensure Python 3.6 or higher is used
    entry_points={  # If you have command-line scripts, define them here
        'console_scripts': [
            'sf-data-integrator=sf_data_integration.integrator:main',  # Example entry point
        ],
    },
)
