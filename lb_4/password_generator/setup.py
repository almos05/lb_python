from setuptools import setup, find_packages

setup(
    name="password-generator",
    version="1.0.0",
    author="almos05",
    author_email="tenderboylive3@gmail.com",
    description="A simple password generator library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/almos05/lb_python/tree/main/lb_4",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)