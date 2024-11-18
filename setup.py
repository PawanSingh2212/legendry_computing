from setuptools import find_packages,setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open("requirements.txt") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="legendry_projects",
    version="0.0.1",
    author="pawan singh",
    author_email="pstangariya@gmail.com",
    pacakages=find_packages(),
    install_requires=get_requirements("requirements.txt"))