from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in data_mining_migrate/__init__.py
from data_mining_migrate import __version__ as version

setup(
	name="data_mining_migrate",
	version=version,
	description="Migrate",
	author="Shashank",
	author_email="shashank@esycommerce.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
