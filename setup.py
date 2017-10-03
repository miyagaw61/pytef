from setuptools import setup, find_packages
import os
exec(open(os.path.join("pytef", "_version.py")).read())

console_scripts = [
        "pytef=pytef.pytef:pytef"
        ]

setup(
    name="pytef",
    version=__version__,
    packages=find_packages(),
    description="test code maker",
    author="Taisei Miyagawa <miyagaw61 at miyagaw61.github.io>",
    author_email="miyagaw61@gmail.com",
    install_requires=["enert==0.0.2", "better_exceptions", "pytest"],
    dependency_links=["git+https://github.com/miyagaw61/enert.git#egg=enert-0.0.2"],
    entry_points = {"console_scripts": console_scripts},
    url="https://github.com/miyagaw61/pytef.git",
    license="MIT"
)
