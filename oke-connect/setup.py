from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'oke-connect',
    version = '0.0.1',
    author = 'Sunny Miglani',
    author_email = 'sunnymiglani936@gmail.com',
    license = 'gpl-3.0',
    description = 'Tool to drive OKE-Operator-Container',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/sunnyMiglani/OKE-Operator-Container',
    py_modules = ['tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        oke-connect=tool:cli
    '''
)
