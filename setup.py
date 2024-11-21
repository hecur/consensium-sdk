from setuptools import setup, find_packages

setup(
    name="consensium-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0"
    ],
    author="Consensium",
    author_email="hector@consensium.io",
    description="A Python SDK for the Consensium API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="ttps://github.com/hecur/consensium-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 