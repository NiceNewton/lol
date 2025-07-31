# 📷 Low Light Image Enhancer

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-FF6F00.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

*An AI-powered web application that brings your dark images to life using Zero-DCE deep learning model* ✨

<img width="800" alt="Low Light Enhancement Demo" src="https://github.com/user-attachments/assets/7e04bb93-06de-4f54-8f84-2997348115f2" />

</div>

---

## 🌟 Features

<table>
<tr>
<td>

### 🔄 **Batch Processing**
- Single image or ZIP file upload
- Process multiple images at once
- Automatic file format detection

</td>
<td>

### 🎛️ **Smart Controls**
- Adjustable enhancement intensity (1x-10x)
- Real-time preview
- Side-by-side comparison

</td>
</tr>
<tr>
<td>

### 🧠 **AI-Powered**
- Zero-DCE deep learning model
- No reference images needed
- Professional-grade enhancement

</td>
<td>

### 🔒 **Privacy First**
- Completely offline processing
- No data uploaded to servers
- Runs locally on your machine

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 4GB+ RAM recommended
- CUDA-compatible GPU (optional, for faster processing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NiceNewton/lol.git
   cd lol
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run src/app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
lol/
├── 📂 src/                 # Source code
│   └── app.py             # Main Streamlit application
├── 📂 models/             # Pre-trained models
│   ├── LOW_LIGHT_MODEL.h5 # Main Zero-DCE model
│   └── low_light_enhancement.h5
├── 📂 notebooks/          # Jupyter notebooks
│   └── training.ipynb     # Model training pipeline
├── 📂 assets/             # Images and demos
├── � requirements.txt    # Python dependencies
├── 🔒 .gitignore         # Git ignore rules
└── 📖 README.md          # Project documentation
```

---

## 🔬 How It Works

### Zero-DCE Algorithm
Our implementation uses **Zero-Reference Deep Curve Estimation (Zero-DCE)**, a state-of-the-art approach for low-light image enhancement:

1. **Input Processing**: Images are resized to 512×512 and normalized
2. **Curve Estimation**: The model predicts pixel-wise curves for enhancement
3. **Iterative Enhancement**: 8 rounds of curve-based transformations
4. **Output**: Naturally enhanced images with preserved details

```python
# Core enhancement algorithm
for i in range(8):
    a = curve[..., i*3:(i+1)*3]
    x = x + a * (tf.square(x) - x)
```

### Loss Functions
- **Illumination Smoothness Loss**: Ensures natural lighting
- **Spatial Consistency Loss**: Maintains image structure
- **Color Constancy Loss**: Preserves color balance
- **Exposure Loss**: Optimizes overall brightness

---

## 🎯 Usage Examples

### Single Image Enhancement
```python
from src.app import enhance_image, load_model
from PIL import Image

model = load_model()
image = Image.open("dark_image.jpg")
enhanced = enhance_image(model, image, intensity=3.0)
enhanced.save("bright_image.jpg")
```

### Batch Processing
Upload a ZIP file containing multiple images, and the app will process them all automatically!

---

## 🏆 Performance Metrics

| Metric | Score |
|--------|-------|
| **Processing Speed** | ~2-3 seconds per image |
| **Model Size** | 350KB (highly optimized) |
| **Memory Usage** | <500MB RAM |
| **Supported Formats** | JPG, JPEG, PNG |

---

## �️ Development

### Training Your Own Model

1. **Prepare Dataset**: Use the LOL dataset or your own low-light images
2. **Run Training**: Execute `notebooks/training.ipynb`
3. **Model Export**: The trained model will be saved as `LOW_LIGHT_MODEL.h5`

### Customization

- **Enhancement Intensity**: Modify the intensity multiplier in `enhance_image()`
- **Image Size**: Change `IMAGE_SIZE` constant for different resolutions
- **UI Themes**: Customize Streamlit components in `app.py`

---

## � Contributors

<div align="center">

### 🚀 **Project Maintainers**

<table>
<tr>
<td align="center">
<a href="https://github.com/NiceNewton">
<img src="https://github.com/NiceNewton.png" width="100px;" alt="NiceNewton"/>
<br />
<sub><b>NiceNewton</b></sub>
</a>
<br />
</td>
<!-- Add more contributors here -->
<td align="center">
<a href="https://github.com/shoury-dev">
<img src="https://github.com/shoury-dev.png" width="100px;" alt="Contributor"/>
<br />
<sub><b>Shouryjeet Gupta</b></sub>
</a>
<br />
</td>
<td align="center">
<a href="https://github.com/SatwickSinha">
<img src="https://github.com/SatwickSinha.png" width="100px;" alt="Contributor"/>
<br />
<sub><b>Your Name</b></sub>
</a>
<br />
</td>
</tr>
</table>

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **💾 Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **📤 Push** to the branch (`git push origin feature/AmazingFeature`)
5. **🔄 Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include unit tests for new features
- Update documentation as needed

---

## � Technical Details

### Model Architecture
- **Base**: Convolutional Neural Network
- **Layers**: 7 convolutional layers with skip connections
- **Output**: 24-channel curve parameters
- **Training**: Unsupervised learning (no paired data required)

### System Requirements
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 4GB | 8GB+ |
| **Storage** | 1GB | 2GB+ |
| **Python** | 3.8 | 3.9+ |
| **GPU** | None | CUDA-compatible |

---

## 🔗 Useful Links

- 📚 [Zero-DCE Paper](https://arxiv.org/abs/2001.06826)
- 🎯 [Streamlit Documentation](https://docs.streamlit.io/)
- 🧠 [TensorFlow Guide](https://www.tensorflow.org/guide)
- 🖼️ [LOL Dataset](https://daooshee.github.io/BMVC2018website/)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Zero-DCE Authors** for the groundbreaking research
- **LOL Dataset** creators for the training data
- **Streamlit Team** for the amazing web framework
- **TensorFlow Community** for the ML tools

---

<div align="center">

### ⭐ **Star this repo if you found it helpful!** ⭐

<img src="https://img.shields.io/github/stars/NiceNewton/lol?style=social" alt="GitHub stars">

**Made with ❤️ by the Low Light Enhancement Team**

</div>
