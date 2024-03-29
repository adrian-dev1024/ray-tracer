import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ray-tracer",
    version="0.0.1",
    author="Adrian Garay",
    author_email="agaray913@gmail.com",
    description="Ray Tracer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrian-dev1024/ray-tracer.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
