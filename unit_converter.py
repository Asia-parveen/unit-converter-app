import streamlit as st

# Custom Styling (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #ffcc00;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    .dropdown select {
        cursor: pointer !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        cursor: pointer !important;
    }
    .stButton>button {
        background: linear-gradient(to right, #ffcc00, #ff9900);
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
    }
    .stSuccess {
        background-color: #1e293b;
        color: #ffcc00;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(255, 204, 0, 0.3);
    }
    .created-by {
        font-size: 16px;
        font-weight: bold;
        color: #ffcc00;
        text-align: center;
        padding-top: 40px;  /* Increased margin */
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Conversion Factors
conversion_factors = {
    "Length": {
        "Meter": {"Kilometer": 0.001, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
        "Kilometer": {"Meter": 1000, "Mile": 0.621371, "Yard": 1093.61, "Foot": 3280.84, "Inch": 39370.1},
        "Mile": {"Meter": 1609.34, "Kilometer": 1.60934, "Yard": 1760, "Foot": 5280, "Inch": 63360},
        "Yard": {"Meter": 0.9144, "Kilometer": 0.0009144, "Mile": 0.000568182, "Foot": 3, "Inch": 36},
        "Foot": {"Meter": 0.3048, "Kilometer": 0.0003048, "Mile": 0.000189394, "Yard": 0.333333, "Inch": 12},
        "Inch": {"Meter": 0.0254, "Kilometer": 0.0000254, "Mile": 0.000015783, "Yard": 0.0277778, "Foot": 0.0833333}
    },
    "Weight": {
        "Kilogram": {"Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Gram": {"Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
        "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Ounce": 16},
        "Ounce": {"Kilogram": 0.0283495, "Gram": 28.3495, "Pound": 0.0625}
    }
}

# Function to Convert Temperature
def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # If same unit selected, return the value as it is

# Streamlit App
st.markdown('<p class="title">🌍 Universal Unit Converter</p>', unsafe_allow_html=True)
st.markdown("### 🔄 Convert Any Unit Into Another Easily and smartly!")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category == "Temperature":
    from_unit = st.selectbox("Convert From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("Convert To", ["Celsius", "Fahrenheit", "Kelvin"])
else:
    from_unit = st.selectbox("Convert From", list(conversion_factors[category].keys()))
    to_unit = st.selectbox("Convert To", list(conversion_factors[category][from_unit].keys()))

value = st.number_input(f"Enter value in {from_unit}", min_value=0.0, step=0.01)

if st.button("Convert"):
    if category == "Temperature":
        result = convert_temperature(from_unit, to_unit, value)
    else:
        result = value * conversion_factors[category][from_unit].get(to_unit, 1)
    
    st.markdown(f'<div class="stSuccess">✅ {value} {from_unit} = {result} {to_unit} ✅</div>', unsafe_allow_html=True)
    
    # Custom message with animation
    st.markdown('<p class="created-by">💖 Crafted with passion and precision by <b>Asia Parveen</b> 🚀</p>', unsafe_allow_html=True)





