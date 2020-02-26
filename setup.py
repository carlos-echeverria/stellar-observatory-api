"""setup"""
import setuptools

with open("README.md", "r") as fh:
        LONG_DESCRIPTION = fh.read()

        setuptools.setup(
                    name="stellar-observatory-api",
                        version="0.0b1",
                            author="Carlos Echeverría Serur",
                                author_email="echeverriacarlos@gmail.com",
                                    description="Python API (aiohttp) for analyzing the Stellar network",
                                        long_description=LONG_DESCRIPTION,
                                            long_description_content_type="text/markdown",
                                                url="https://github.com/carlos-echeverria/stellar-observatory-api",
                                                    packages=setuptools.find_packages(),
                                                        python_requires="~=3.5",
                                                            install_requires=[
                                                                        "aiohttp~=3.6.2"
                                                                                            ],
                                                                classifiers=[
                                                                            "Programming Language :: Python :: 3",
                                                                                    "License :: OSI Approved :: MIT License",
                                                                                            "Operating System :: OS Independent",
                                                                                                    "Intended Audience :: Science/Research"
                                                                                                        ],
                                                                )
