"""
Setup script for X-Codec package.

Installation:
    pip install git+https://github.com/Qingzheng-Wang/xcodec.git
    
    Or from local:
    pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
install_requires = []
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="xcodec",
    version="1.0.0",
    description="Unified Semantic and Acoustic Codec for Audio Language Model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="",  # Add your email if needed
    url="https://github.com/Qingzheng-Wang/xcodec",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests", "test_audio", "test_audio_reconstruction", "*.pyc", "__pycache__"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],
    keywords=[
        "audio",
        "codec",
        "compression",
        "neural codec",
        "semantic codec",
        "acoustic codec",
        "audio language model",
        "hubert",
        "wavlm",
    ],
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.txt", "*.md"],
    },
    entry_points={
        "console_scripts": [
            # Add command-line scripts if needed
            # "xcodec-encode=encode_audio:main",
            # "xcodec-decode=decode_codes:main",
        ],
    },
    zip_safe=False,
)

