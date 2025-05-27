from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from the requirements.txt file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Aishvi',
    author_email='aishvitomar01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    dependency_links=[HYPHEN_E_DOT],  # This line is crucial
)
