# 🌍 3D Air Quality Advisor with Voice

An AI-powered air quality monitoring system that predicts CO pollution levels using machine learning, provides health recommendations, and delivers results through interactive 3D visualization and voice alerts.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)

## 🎯 Features

- **🤖 ML Prediction**: Random Forest model trained on 9,358+ hourly air quality records
- **⚠️ Risk Classification**: Automatic CO level categorization (Safe/Warning/Danger) based on WHO guidelines
- **💡 Health Recommendations**: Rule-based advisory system for different pollution levels
- **📊 3D Visualization**: Interactive Plotly scatter plots showing time-temperature-CO relationships
- **🔊 Voice Output**: Text-to-speech audio alerts using Google TTS

## 📸 Screenshots

### 3D Visualization
![3D Plot](screenshots/3d_visualization.png)

### Terminal Output
![Results](screenshots/terminal_output.png)

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip package manager
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/NguyenNhatAnh-dev/Air-quality-3d-voice-advisor.git
cd Air-quality-3d-voice-advisor
```

2. Install dependencies
```bash
pip install pandas numpy scikit-learn plotly gtts matplotlib
```

3. Run the project
```bash
python air_quality.py
```

## 📊 Dataset

**Source**: [UCI Air Quality Dataset](https://archive.ics.uci.edu/dataset/387/air+quality)

- 9,358 hourly measurements
- Features: CO, NOx, NO₂, benzene, temperature, humidity
- Location: Italian city multi-sensor monitoring system

## 🔧 How It Works

1. **Data Loading**: Automatically downloads and preprocesses UCI Air Quality dataset
2. **Feature Engineering**: Extracts Temperature, Relative Humidity, Absolute Humidity
3. **Model Training**: Random Forest Regressor predicts CO concentration (mg/m³)
4. **Risk Assessment**: Categorizes CO levels based on WHO guidelines
5. **Recommendation Generation**: Provides health advice based on pollution level
6. **Visualization**: Creates interactive 3D plots with color-coded risk levels
7. **Voice Output**: Generates MP3 audio file with prediction and recommendation

## 📈 Model Performance
```
MAE (Mean Absolute Error): ~X.XXX mg/m³
R² Score: ~0.XXX
```

## 🎨 CO Risk Levels

| Level | CO Range (mg/m³) | Color | Recommendation |
|-------|------------------|-------|----------------|
| Safe | < 2 | 🟢 Green | Normal outdoor activities |
| Warning | 2 - 4 | 🟡 Yellow | Sensitive groups limit exposure |
| Danger | ≥ 4 | 🔴 Red | Everyone avoid outdoor exercise |

## 📁 Project Structure
```
air-quality-3d-voice-advisor/
│
├── air_quality.py              # Main script
├── air_quality_advice.mp3      # Generated voice output
├── air_quality_3d.html         # Interactive 3D visualization
├── air_quality_data/           # Downloaded dataset
│   └── AirQualityUCI.csv
├── screenshots/                # Project screenshots
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🛠️ Technologies

- **Python 3.8+**
- **scikit-learn**: Random Forest regression
- **Plotly**: Interactive 3D visualization
- **gTTS**: Google Text-to-Speech
- **pandas**: Data manipulation
- **numpy**: Numerical computing

## 💻 Usage Example
```python
# Sample input
input_features = {
    'Temperature': 18.3,
    'Relative Humidity': 41,
    'Absolute Humidity': 0.89
}

# Output
Predicted CO: 3.25 mg/m³
Category: Warning
Recommendation: "Sensitive groups should limit outdoor activities..."
```

## 🌐 Applications

- Smart city environmental monitoring dashboards
- IoT air quality sensors with voice alerts
- Public health advisory kiosks
- Mobile apps for pollution-sensitive populations
- Smart home environmental control systems

## 📝 WHO Guidelines Reference

Based on [WHO Air Quality Guidelines](https://en.wikipedia.org/wiki/Air_quality_guideline):
- CO 24-hour mean: < 4 mg/m³
- Prolonged exposure increases risk of cardiovascular and respiratory diseases

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is no licensed

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Air Quality dataset
- WHO for air quality guidelines
- scikit-learn community for ML tools

## 📧 Contact

Your Name - [nhatanh4works@gmail.com](nhatanh4works@gmail.com)

Project Link: [https://github.com/NguyenNhatAnh-dev/Air-quality-3d-voice-advisor](https://github.com/NguyenNhatAnh-dev/Air-quality-3d-voice-advisor)

---

⭐ Star this repo if you find it helpful!
```

---

### **Short Description (for GitHub repo)**
```
🌍 AI-powered air quality monitoring system using Random Forest ML to predict 
CO pollution, generate health recommendations, and visualize data in 
interactive 3D plots with voice alerts. Built with Python, scikit-learn, 
Plotly, and gTTS.
```

---

### **GitHub Topics/Tags to Add:**
```
air-quality
machine-learning
random-forest
data-visualization
3d-visualization
plotly
text-to-speech
iot
environmental-monitoring
health-tech
smart-city
python
scikit-learn
data-science
pollution-monitoring