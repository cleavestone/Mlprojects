from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOR='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements from the file
    :param file_path: str: file path for requirements
    """
    with open('requirements.txt', 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements] # remove \n from the requirements
        
        if HYPHEN_E_DOR in requirements:
            requirements.remove(HYPHEN_E_DOR)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Cleave',
    author_email='cleavestone94@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),


)