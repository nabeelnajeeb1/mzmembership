from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mzmembership/__init__.py
from mzmembership import __version__ as version

setup(
	name="mzmembership",
	version=version,
	description="Memebrship Portal",
	author="M20Zero",
	author_email="hello@m20zero.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
