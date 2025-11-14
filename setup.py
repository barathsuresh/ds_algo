"""
Setup script for Data Structures and Algorithms Learning Project.

This package provides comprehensive implementations of fundamental data structures
and algorithms in Python, designed for educational purposes with detailed
documentation, complexity analysis, and interactive demonstrations.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="ds-algo-learning",
    version="1.0.0",
    author="DSA Learning Project",
    author_email="barath.learns@gmail.com",
    description="Comprehensive data structures and algorithms implementation for learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barath-learns/ds-algo-learning",
    project_urls={
        "Bug Tracker": "https://github.com/barath-learns/ds-algo-learning/issues",
        "Documentation": "https://github.com/barath-learns/ds-algo-learning/wiki",
        "Source Code": "https://github.com/barath-learns/ds-algo-learning",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # Core package has no dependencies - uses only Python standard library
    ],
    extras_require={
        "visualization": [
            "matplotlib>=3.5.0",
            "numpy>=1.20.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "notebook": [
            "notebook>=6.4.0",
            "ipywidgets>=8.0.0",
        ],
        "profiling": [
            "memory-profiler>=0.60.0",
            "line-profiler>=4.0.0",
        ],
        "all": [
            # Combines all optional dependencies
            "matplotlib>=3.5.0",
            "numpy>=1.20.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "notebook>=6.4.0",
            "ipywidgets>=8.0.0",
            "memory-profiler>=0.60.0",
            "line-profiler>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ds-algo-demo=ds_algo.demos:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "data-structures",
        "algorithms",
        "education",
        "learning",
        "computer-science",
        "programming",
        "python",
        "trees",
        "linked-lists",
        "stacks",
        "queues",
        "complexity-analysis",
        "big-o",
        "binary-search-tree",
        "tutorial",
    ],
    license="MIT",
)
