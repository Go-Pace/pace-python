import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gopace",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Paingha Joe Alagoa (Go Pace)",                     # Full name of the author
    description="Go Pace is a delivery service that enables everyone to get what they want when they need it most. This is a Python Client Library to interact with the Go Pace Client API.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    project_urls={
        "Bug Tracker": "https://github.com/Go-Pace/pace-python/issues",
        "Documentation": "https://gopace.readme.io",
        "Source Code": "https://github.com/Go-Pace/pace-python",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["gopace"],             # Name of the python package
    package_dir={'':'gopace/src'},     # Directory of the source code of the package
    install_requires=['requests']                     # Install other dependencies if any
)