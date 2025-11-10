from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a clean list of dependencies.
    Removes '-e .' and empty lines automatically.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements

setup(
    name="ml_project",
    version="1.0.0",
    author="Mohd Kaif",
    author_email="officialmohdkaif20@gmail.com",
    description="An awesome project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
    )
