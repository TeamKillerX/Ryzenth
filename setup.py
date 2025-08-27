import os
import re

import setuptools


def read(fname, version=False):
    text = open(
        os.path.join(
            os.path.dirname(__file__),
            fname),
        encoding="utf8").read()
    return re.search(r'__version__ = "(.*?)"', text)[1] if version else text


setuptools.setup(
    name="Ryzenth",
    packages=setuptools.find_packages(),
    version=read("Ryzenth/__version__.py", version=True),
    license="MIT",
    description="Ryzenth is a flexible Multi-API SDK with built-in support for API key management and database integration.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="TeamKillerX",
    project_urls={
        "Source": "https://github.com/TeamKillerX/Ryzenth/",
        "Issues": "https://github.com/TeamKillerX/Ryzenth/discussions",
    },
    keywords=[
        "Multi-API",
        "Ryzenth-SDK",
        "Ryzenth",
    ],
    install_requires=[
        "requests",
        "pydantic",
        "typing",
        "aiohttp",
        "motor",
        "httpx[http2]",
        "bs4",
        "python-box",
    ],
    extras_require={
        "fast": [
            "aiohttp",
            "motor",
            "wget",
            "requests",
            "httpx[http2]",
            "python-box",
            "pydantic",
            "bs4",
            "typing",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires="~=3.7",
)
