from codecs import open

from setuptools import setup

'''
:authors: dymshnc.
:license: Apache License, Version 2.0, see LICENSE file.

:copyright: (c) 2022 by dymshnc.
'''

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name='eltch',
    version='0.9.3',
    description='Electrotechnical assistant.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='dymshnc',
    author_email='officialdyomshin@gmail.com',
    url='https://github.com/dymshnc/eltch',
    packages=["eltch"],
    python_requires=">=3.6",
    license='Apache License, Version 2.0, see LICENSE file',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    project_urls={
        "Documentation": "https://github.com/dymshnc/eltch#readme",
        "Source": "https://github.com/dymshnc/eltch",
    },
)
