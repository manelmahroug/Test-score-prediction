from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements.txt file and returns a cleaned list of dependencies.
    Removes empty lines and any '-e .' entry if present.
    """
    with open(file_path, "r") as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip()]  # Removes newlines & empty lines
    
    # Remove '-e .' if it's present
    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements







setup (

    name= 'attritionProject',
    version = '0.0.1',
    author= 'manel',
    author_email= 'manel.khan@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
