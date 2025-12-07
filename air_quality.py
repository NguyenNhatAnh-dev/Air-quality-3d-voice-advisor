import pandas as pd
import numpy as np
import requests
import zipfile
import io
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import plotly.express as px
from gtts import gTTS

print("=== AIR QUALITY 3D VOICE AI LAB ===\n")

print("Step 1: Downloading dataset...")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00360/AirQualityUCI.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('./air_quality_data')

df = pd.read_csv(
    './air_quality_data/AirQualityUCI.csv',
    sep=';',
    decimal=',',
    na_values=-200
)
print(f"Dataset loaded successfully! Shape: {df.shape}")
print("\nSample data:")
print(df.head())

print("\n\nStep 2: Preprocessing data...")
cols = ['CO(GT)', 'T', 'RH', 'AH']
data = df[cols].copy()
data = data.dropna()
data.columns = ['CO', 'Temp', 'RH', 'AH']

print(f"Cleaned data rows: {len(data)}")
print("\nDescriptive statistics:")
print(data.describe())

print("\n\nStep 3: Categorizing CO levels...")

def co_category(co):
    if co < 2:
        return "Safe"
    elif co < 4:
        return "Warning"
    else:
        return "Danger"

data['CO_level'] = data['CO'].apply(co_category)
print("CO level distribution:")
print(data['CO_level'].value_counts())

print("\n\nStep 4: Training Random Forest model...")
X = data[['Temp', 'RH', 'AH']]
y = data['CO']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model training complete!")
print(f"\nMODEL PERFORMANCE:")
print(f"MAE = {mae:.3f} mg/m³")
print(f"R²  = {r2:.3f}")

print("\n\nStep 5: Creating recommendation system...")

def recommend_from_co(co_value):
    cat = co_category(co_value)
    if cat == "Safe":
        rec = ("Air quality is safe. You can stay outdoors as usual, "
               "but keep monitoring if conditions change.")
    elif cat == "Warning":
        rec = ("Air quality is getting worse. Sensitive groups should "
               "limit long outdoor activities and keep windows closed.")
    else:
        rec = ("Air quality is dangerous. Everyone should avoid outdoor "
               "exercise, close windows, and consider wearing a mask.")
    return cat, rec

sample_idx = 10
x_sample = X_test.iloc[sample_idx]
co_true = y_test.iloc[sample_idx]
co_pred = model.predict([x_sample])[0]

cat, rec = recommend_from_co(co_pred)

print("Recommendation system ready!")
print(f"\nSAMPLE PREDICTION:")
print(f"Input features: {x_sample.to_dict()}")
print(f"True CO: {co_true:.2f} mg/m³")
print(f"Predicted CO: {co_pred:.2f} mg/m³")
print(f"Category: {cat}")
print(f"Recommendation: {rec}")

print("\n\nStep 6: Generating voice output...")
text_for_voice = (
    f"Predicted carbon monoxide level is {co_pred:.2f} milligrams per cubic meter. "
    f"Category: {cat}. {rec}"
)

tts = gTTS(text=text_for_voice, lang='en')
tts.save("air_quality_advice.mp3")
print("Voice file saved: air_quality_advice.mp3")

print("\n\nStep 7: Creating 3D visualization...")
n_points = 1000
sub = data.iloc[:n_points].copy()
sub['time_idx'] = np.arange(len(sub))

sub_pred = model.predict(sub[['Temp', 'RH', 'AH']])
sub['CO_pred'] = sub_pred
sub['level_pred'] = sub['CO_pred'].apply(co_category)

fig = px.scatter_3d(
    sub,
    x='time_idx',
    y='Temp',
    z='CO_pred',
    color='level_pred',
    color_discrete_map={
        'Safe': 'green',
        'Warning': 'yellow',
        'Danger': 'red'
    },
    labels={
        'time_idx': 'Time (hours)',
        'Temp': 'Temperature (°C)',
        'CO_pred': 'Predicted CO (mg/m³)',
        'level_pred': 'Risk level'
    },
    title='3D Air Quality Visualization'
)
fig.update_traces(marker=dict(size=3))

fig.write_html("air_quality_3d.html")
print("3D visualization saved: air_quality_3d.html")

fig.show()

print("\n\n=== LAB COMPLETED SUCCESSFULLY ===")
print("\nGenerated files:")
print("- air_quality_advice.mp3")
print("- air_quality_3d.html")
print("- air_quality_data/ folder")