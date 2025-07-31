#!/bin/bash

# Low Light Image Enhancer Setup Script

echo "🚀 Setting up Low Light Image Enhancer..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "📍 Python version: $python_version"

# Create virtual environment
echo "🔨 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate  # For Unix/Linux/Mac
# venv\Scripts\activate  # For Windows

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Download models if not present
if [ ! -f "models/LOW_LIGHT_MODEL.h5" ]; then
    echo "⚠️  Model files not found in models/ directory"
    echo "📝 Please ensure model files are placed in the models/ folder"
fi

echo "✅ Setup complete!"
echo "🚀 Run the application with: streamlit run src/app.py"
