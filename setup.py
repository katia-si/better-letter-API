from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='better-letter',
      version="0.0.1",
      description="Simplify and summarize official German letters",
      license="CC0 1.0 Universal",
      author="Ekaterina Sidorenko, Tereza Gramberg, Hrvoje Santek, Carsten Volland",
      author_email="ekaterina.sidorenko.se@gmail.com",
      url="https://github.com/katia-si/better-letter",
      install_requires=requirements,
      packages=find_packages(),
      # test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
