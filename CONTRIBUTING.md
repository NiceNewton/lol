# 🤝 Contributing to Low Light Image Enhancer

First off, thank you for considering contributing to Low Light Image Enhancer! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic understanding of machine learning and image processing

### First Contribution
1. **🍴 Fork** the repository
2. **📥 Clone** your fork: `git clone https://github.com/YOUR_USERNAME/lol.git`
3. **🌿 Create** a branch: `git checkout -b feature/your-feature-name`
4. **💾 Make** your changes
5. **🧪 Test** your changes
6. **📤 Submit** a pull request

## 🛠️ How to Contribute

### 🐛 Reporting Bugs
- Use the bug report template
- Include detailed reproduction steps
- Provide environment information
- Add screenshots if applicable

### 💡 Suggesting Features
- Use the feature request template
- Explain the use case clearly
- Consider implementation challenges
- Discuss with maintainers first for large features

### 📝 Documentation
- Fix typos and grammatical errors
- Improve code examples
- Add missing documentation
- Translate documentation

### 🧪 Testing
- Add unit tests for new features
- Improve test coverage
- Test on different platforms
- Performance testing

## 🔧 Development Setup

### Local Development
```bash
# Clone the repository
git clone https://github.com/NiceNewton/lol.git
cd lol

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Install pre-commit hooks
pre-commit install

# Run the application
streamlit run src/app.py
```

### Project Structure
```
lol/
├── src/                    # Source code
│   └── app.py             # Main application
├── models/                # ML models
├── notebooks/             # Jupyter notebooks
├── tests/                 # Test files
├── assets/                # Static assets
├── .github/               # GitHub workflows
└── docs/                  # Documentation
```

## 🔄 Pull Request Process

### Before Submitting
1. **✅ Run tests**: `pytest tests/`
2. **🔍 Lint code**: `flake8 src/`
3. **📝 Update docs**: If you change functionality
4. **🏷️ Update version**: Follow semantic versioning

### PR Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
- [ ] Linked to relevant issues

### Review Process
1. **👀 Automated checks** must pass
2. **👥 Peer review** by maintainers
3. **🧪 Manual testing** if needed
4. **✅ Approval** and merge

## 🎨 Style Guidelines

### Python Code Style
We follow **PEP 8** with some modifications:

```python
# Good
def enhance_image(model, image: Image.Image, intensity: float = 3.0) -> Image.Image:
    """Enhance a low-light image using the Zero-DCE model.
    
    Args:
        model: The trained Zero-DCE model
        image: Input PIL Image
        intensity: Enhancement intensity multiplier
        
    Returns:
        Enhanced PIL Image
    """
    # Implementation here
    pass

# Bad
def enhance_image(model,image,intensity=3.0):
    #enhance image
    pass
```

### Documentation
- Use **docstrings** for all functions
- Add **type hints** where possible
- Keep **comments** concise and helpful
- Update **README** for user-facing changes

### Commit Messages
Follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
feat: add batch processing for ZIP files
fix: resolve memory leak in image processing  
docs: update installation instructions
test: add unit tests for enhancement algorithm
```

## 🧪 Testing Guidelines

### Test Categories
1. **Unit Tests**: Test individual functions
2. **Integration Tests**: Test component interactions
3. **UI Tests**: Test Streamlit interface
4. **Performance Tests**: Test speed and memory usage

### Writing Tests
```python
import pytest
from src.app import preprocess_image
from PIL import Image

def test_preprocess_image():
    """Test image preprocessing function."""
    # Arrange
    test_image = Image.new('RGB', (256, 256), color='red')
    
    # Act
    result = preprocess_image(test_image)
    
    # Assert
    assert result.shape == (1, 512, 512, 3)
    assert 0 <= result.min() <= result.max() <= 1
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_app.py

# Run tests in parallel
pytest -n auto
```

## 📊 Performance Guidelines

### Code Performance
- Profile code before optimizing
- Use appropriate data structures
- Cache expensive operations
- Optimize for common use cases

### Model Performance
- Monitor inference time
- Track memory usage
- Test on different hardware
- Consider model quantization

## 🌍 Community

### Getting Help
- 💬 **Discord**: [Join our community](https://discord.gg/lowlight)
- 📧 **Email**: support@lowlightenhancer.com
- 🐛 **Issues**: GitHub Issues for bugs
- 💡 **Discussions**: GitHub Discussions for ideas

### Communication
- Be respectful and professional
- Use clear, descriptive titles
- Provide context and examples
- Follow up on your contributions

## 🏆 Recognition

We recognize contributors in several ways:

### Contributors Wall
All contributors are featured in our README with:
- GitHub profile picture
- Name and role
- Link to profile

### Special Recognition
- **🌟 Top Contributors**: Monthly recognition
- **🚀 Feature Champions**: For major feature contributions
- **🐛 Bug Hunters**: For finding critical bugs
- **📚 Documentation Heroes**: For documentation improvements

## 📚 Learning Resources

### Machine Learning
- [Zero-DCE Paper](https://arxiv.org/abs/2001.06826)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [Computer Vision Course](https://cs231n.stanford.edu/)

### Web Development
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Best Practices](https://realpython.com/python-code-quality/)

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 🎉 Thank You!

Your contributions make this project better for everyone. Whether you're fixing bugs, adding features, improving documentation, or helping other users, every contribution matters! 🙏

---

**Happy Contributing!** 🚀

*For questions about contributing, feel free to reach out to the maintainers.*
