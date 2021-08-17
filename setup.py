from setuptools import setup, find_packages

setup(
    name="loger",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    },
    install_requires=[],
    url="https://github.com/iridesc/loger",
    author="Irid Zhang",
    author_email="irid.zzy@gmail.com",
    description="loger can control your log printing and sveing easily",
    long_description="loger can your log printing and sveing easily",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)