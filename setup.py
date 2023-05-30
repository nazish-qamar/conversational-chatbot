from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path: str) -> List[str]:
    """Returns the list of requiements
    :param file_path:
    :return:
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # every line will have \n character also at end, so need to remove it
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:  # this is to explicitly tell to skip "-e ." from the requirements.txt file
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='conversational-chatbot',
    version='0.0.1',
    author='Nazish',
    author_email='nazishqamar01@gmail.com',
    packages=find_packages(),  # this will find all the files with __init__.py as package
    install_requires=get_requirements('requirements.txt')
)
