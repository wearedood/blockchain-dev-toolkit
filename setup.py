#!/usr/bin/env python3
"""
Blockchain Development Toolkit Setup
A comprehensive toolkit for blockchain developers with utilities, validators, and testing frameworks.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="blockchain-dev-toolkit",
    version="1.0.0",
    author="Blockchain Developer",
    author_email="dev@blockchain-toolkit.com",
    description="Comprehensive toolkit for blockchain developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wearedood/blockchain-dev-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "web3>=6.0.0",
        "eth-account>=0.8.0",
        "cryptography>=3.4.8",
        "pycryptodome>=3.15.0",
        "jsonschema>=4.0.0",
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "black>=22.0.0",
        "flake8>=5.0.0",
        "isort>=5.10.0",
    ],
    extras_require={
        "dev": [
            "pytest-mock>=3.8.0",
            "coverage>=6.0.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "bitcoin": [
            "bitcoinlib>=0.12.0",
            "python-bitcoinlib>=0.12.0",
        ],
        "ethereum": [
            "web3>=6.0.0",
            "eth-account>=0.8.0",
            "py-evm>=0.6.0",
        ],
        "solana": [
            "solana>=0.30.0",
            "anchorpy>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "blockchain-toolkit=blockchain_toolkit.cli:main",
            "btk=blockchain_toolkit.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/wearedood/blockchain-dev-toolkit/issues",
        "Source": "https://github.com/wearedood/blockchain-dev-toolkit",
        "Documentation": "https://blockchain-dev-toolkit.readthedocs.io/",
    },
)
