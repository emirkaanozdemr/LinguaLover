from setuptools import setup, find_packages

setup(
    name='LinguaLover',
    version='1.0.0',
    author='Emir Kaan Özdemir',
    author_email='emirkaanbulut08@gmail.com',
    description='A library to say your love.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/emirkaanozdemr/iloveyou',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache License 2.0'
)