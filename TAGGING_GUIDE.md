# Git Tagging and Release Guidelines

This document outlines the git tagging and versioning strategy for the Data Structures and Algorithms Learning Project.

## 🏷️ Versioning Strategy

We follow **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Incompatible API changes or major restructuring
- **MINOR**: New features, new data structures, significant enhancements
- **PATCH**: Bug fixes, documentation updates, minor improvements

### Current Version: `v1.0.0`

## 📋 Release Process

### 1. Pre-Release Checklist

```bash
# Ensure all tests pass
python -m pytest ds_algo/

# Run code quality checks
black ds_algo/
flake8 ds_algo/
mypy ds_algo/

# Update documentation
# Update CHANGELOG.md
# Update version in setup.py
```

### 2. Create Release Tag

```bash
# Create annotated tag with message
git tag -a v1.0.0 -m "Release v1.0.0: Initial comprehensive implementation

Features:
- Complete complexity analysis module
- Linear structures (arrays, lists, linked lists)
- Abstract data types (stacks, queues)
- Non-linear structures (trees, BST)
- Comprehensive documentation and examples
- Full test coverage"

# Push tag to remote
git push origin v1.0.0
```

### 3. GitHub Release

Create a release on GitHub with:

- **Tag version**: v1.0.0
- **Release title**: Data Structures & Algorithms v1.0.0
- **Description**: Summary of features and changes
- **Assets**: Source code archives (auto-generated)

## 🗂️ Tagging Examples

### Feature Release (Minor Version)

```bash
git tag -a v1.1.0 -m "Release v1.1.0: Advanced Tree Structures

New Features:
- AVL Tree implementation with self-balancing
- Red-Black Tree with rotations
- B-Tree for disk-based storage
- Tree visualization utilities
- Performance benchmarking tools"
```

### Bug Fix Release (Patch Version)

```bash
git tag -a v1.0.1 -m "Release v1.0.1: Bug Fixes and Improvements

Fixes:
- Fixed edge case in BST deletion
- Corrected complexity analysis in README
- Updated type hints for Python 3.7 compatibility
- Fixed memory leak in linked list iterator"
```

### Major Release (Breaking Changes)

```bash
git tag -a v2.0.0 -m "Release v2.0.0: Major API Redesign

Breaking Changes:
- Renamed modules for consistency
- Unified interface for all data structures
- Changed function signatures for clarity
- Restructured package hierarchy

New Features:
- Graph data structures and algorithms
- Advanced sorting algorithms
- Dynamic programming utilities
- Algorithm animation framework"
```

## 📈 Suggested Roadmap

### v1.x Series (Current - Educational Focus)

- `v1.0.0`: Initial release with core data structures ✅
- `v1.1.0`: Advanced trees (AVL, Red-Black, B-trees)
- `v1.2.0`: Graph structures and basic algorithms
- `v1.3.0`: Sorting and searching algorithms
- `v1.4.0`: Dynamic programming examples

### v2.x Series (Future - Advanced Features)

- `v2.0.0`: Algorithm visualization and animation
- `v2.1.0`: Performance benchmarking framework
- `v2.2.0`: Interactive learning modules
- `v2.3.0`: Competitive programming templates

### v3.x Series (Future - Specialized Topics)

- `v3.0.0`: Advanced algorithms (network flow, string algorithms)
- `v3.1.0`: Computational geometry
- `v3.2.0`: Machine learning data structures

## 🔄 Development Workflow

### Branch Strategy

```bash
main           # Stable releases only
develop        # Integration branch for features
feature/*      # Individual feature development
hotfix/*       # Critical bug fixes for releases
```

### Tag Management

```bash
# List all tags
git tag -l

# Show tag details
git show v1.0.0

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0

# Checkout specific version
git checkout v1.0.0
```

## 📝 Changelog Guidelines

Maintain `CHANGELOG.md` with sections:

- **Added**: New features
- **Changed**: Modifications to existing features
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

### Example Entry

```markdown
## [1.0.0] - 2024-01-15

### Added

- Comprehensive complexity analysis module
- Linear data structures (arrays, lists, linked lists)
- Abstract data types (stacks, queues) with dual implementations
- Tree structures (general, binary, BST) with traversals
- Extensive documentation and learning guides
- Visual demonstrations and testing suites

### Changed

- Restructured from monolithic notebook to modular package
- Enhanced error handling and edge case coverage
- Improved type hints and documentation consistency

### Fixed

- Memory optimization in linked list implementations
- Edge cases in tree deletion algorithms
- Performance issues in large dataset operations
```

## 🏗️ Build and Distribution

### PyPI Package Release

```bash
# Build distribution packages
python setup.py sdist bdist_wheel

# Check package
twine check dist/*

# Upload to Test PyPI (optional)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

### Docker Container (Future)

```bash
# Build container
docker build -t ds-algo-learning:v1.0.0 .

# Tag for Docker Hub
docker tag ds-algo-learning:v1.0.0 barathlearns/ds-algo-learning:v1.0.0

# Push to registry
docker push barathlearns/ds-algo-learning:v1.0.0
```

## 🎯 Git Commands Summary

```bash
# Development workflow
git checkout -b feature/new-algorithm
git add .
git commit -m "feat: implement merge sort algorithm"
git push origin feature/new-algorithm

# Create pull request, merge to develop
git checkout develop
git merge feature/new-algorithm
git push origin develop

# Prepare release
git checkout main
git merge develop
git tag -a v1.1.0 -m "Release message"
git push origin main --tags

# Hotfix workflow
git checkout -b hotfix/critical-bug main
git commit -m "fix: resolve memory leak in BST"
git checkout main
git merge hotfix/critical-bug
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git push origin main --tags
```

---

## 📚 Resources

- [Semantic Versioning](https://semver.org/)
- [Git Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- [Keep a Changelog](https://keepachangelog.com/)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github)

Following this tagging structure ensures clear project evolution and easy rollback capabilities! 🏷️
