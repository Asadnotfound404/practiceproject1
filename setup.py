from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str ) -> list[str]:
    """
    This function will returns the list of requirements.
    """

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name = "FirstMLproject",
    version = "0.0.1",
    author="Asad",
    author_email = "asadnotfound404@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)