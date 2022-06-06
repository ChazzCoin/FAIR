from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairNLP',
    version='1.3.1',
    description='FairNLP (Natural Language Processing) Library.',
    url='https://github.com/chazzcoin/FAIR',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['FCoRE~=1.0.3'],
    package_data={
        'fairResources': ['*.txt']
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)