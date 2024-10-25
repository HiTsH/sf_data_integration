from setuptools import setup, find_packages

setup(
    name="sf_data_integration",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "simple-salesforce",
        "pytest"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for integrating data from various sources into Salesforce",
    url="https://github.com/yourusername/sf_data_integration",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
