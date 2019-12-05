import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loger",
    version="0.2",
    author="Irid Zhang",
    author_email="irid.zzy@gmail.com",
    description="loger can easily control your log printing and sveing ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iridesc/loger",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)