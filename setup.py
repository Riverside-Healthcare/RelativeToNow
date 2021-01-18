from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="relative_to_now",
    version="0.0.1",
    description="Print a datetimes distance from now",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    author="Christopher Pickering",
    author_email="cpickering@rhc.net",
    license="GPL-3.0-or-later",
    packages=["RelativeToNow"],
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
    ],
)