'''
This setup.py plays an important role in packaging and distributing python 
projects.It is used by setuptools(or disutils in older Python version) to 
define the configuration of the projects, like dependencies,metadata or so on.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                req=line.strip()
                if req and req!='-e .':
                    requirement.append(req)
    except FileNotFoundError:
        print("Not able to read requirements.txt")

    return requirement

setup(
    name="Network Security",
    version="0.0.1",
    author="Lavish Laller",
    author_email="apna2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

