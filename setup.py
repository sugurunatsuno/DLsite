import sys
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()


info = sys.version_info

setup(
    name='DLsite',
    version='0.1.0',
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='sugurunatsuno',
    author_email='suguru.irie@gmail.com',
    url='https://github.com/sugurunatsuno/DLsite.git',
    packages=find_packages(),
    include_package_data=True,
    keywords='dlsite',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ],
    test_suite="test",
)
