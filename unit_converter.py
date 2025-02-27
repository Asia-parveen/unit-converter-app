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

      .stSelectbox label, .stNumberInput label {
        color: #E2E2B6 !important; /* Light beige color */
        font-size: 16px;
        font-weight: bold;
    }
      /* Dropdown and Input Styling */
    .dropdown select, .stSelectbox div[data-baseweb="select"],
    input, textarea, select {
        cursor: pointer !important;
        # background: rgba(46, 139, 87, 0.2); /* Transparent Sea Green */
        color: white;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: bold;
        border: none !important; /* Removes default borders */
        outline: none !important;
        transition: all 0.3s ease-in-out;
    }

   
   

 .stButton>button {
    width: 100%;
    background: transparent;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: 2px solid white  /* Yellow border */
    border-radius: 12px;
    padding: 12px 24px;
    box-shadow: 0px 4px 10px rgba(255, 204, 0, 0.5);
    transition: all 0.3s ease-in;
}

.stButton>button:hover {
    background: rgba(255, 204, 0, 0.2);  /* Light yellow hover effect */
    transform: scale(1.03);
    color:white;
    box-shadow: 0px 6px 8px rgba(255, 204, 0, 0.6);
}

.stButton>button:active {
    transform: scale(0.98);
    box-shadow: 0px 2px 6px rgba(255, 204, 0, 0.4);
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
   

  .custom-info {
    width: 100%; /* Full width */
    background: transparent; /* No background */
    color: white; /* White text */
    box-shadow: 0px 4px 10px rgba(255, 204, 0, 0.5);
    font-size: 16px;
    font-weight: bold;
    # border: 2px solid #ffcc00; /* Yellow border */
    border-radius: 8px;
    padding: 10px 20px;
    text-align: center;
    margin-top:20px
    box-shadow: 0px 5px 10px rgba(255, 204, 0, 0.3); /* Soft glow effect */
}


    .created-by {
        font-size: 16px;
        font-weight: bold;
        color: #ffcc00;
        text-align: center;
        padding-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🌍 Universal Unit Converter </p>', unsafe_allow_html=True)
st.markdown("### 🔄 Convert Any Unit Into Another Easily and smartly!")

st.markdown('<p style="color: white;">Seamless and accurate unit conversions at your fingertips!</p>', unsafe_allow_html=True)

def length_conversion(value, from_unit, to_unit):
    units = {
        'Kilometer': 1000,
        'Meter': 1,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def area_conversion(value, from_unit, to_unit):
    units = {
        'Square Kilometer': 1000000,
        'Square Meter': 1,
        'Square Mile': 2589988.11,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10000,
        'Acre': 4046.86
    }
    return value * units[from_unit] / units[to_unit]

def pressure_conversion(value, from_unit, to_unit):
     units = {
        'Pascal': 1,
        'Kilopascal': 1000,
        'Bar': 100000,
        'Pound per square inch': 6894.76,
        'Atmosphere': 101325
    }
     return value * units[from_unit] / units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    units = {
        'Cubic meter': 1000,
        'Cubic centimeter': 0.001,
        'Liter': 1,
        'Milliliter': 0.001,
        'Gallon': 3.78541,
        'Quart': 0.946353,
        'Pint': 0.473176,
        'Cup': 0.236588
    }
    return value * units[from_unit] / units[to_unit]

    

def data_transfer_rate_conversion(value, from_unit, to_unit):
    units = {
        'Bit per second': 1,
        'Kilobit per second': 1000,
        'Megabit per second': 1000000,
        'Gigabit per second': 1000000000,
        'Byte per second': 8,
        'Kilobyte per second': 8000,
        'Megabyte per second': 8000000,
        'Gigabyte per second': 8000000000
    }
    return value * units[from_unit] / units[to_unit]

def energy_conversion(value, from_unit, to_unit):
 units = {
        'Joule': 1,
        'Kilojoule': 1000,
        'Calorie': 4.184,
        'Kilocalorie': 4184,
        'Watt-hour': 3600,
        'Kilowatt-hour': 3600000,
        'Electron volt': 1.602177e-19,
        'British thermal unit': 1055.06
    }
 return value * units[from_unit] / units[to_unit]

def digital_storage_conversion(value, from_unit, to_unit):
    units = {
        'Bit': 1,
        'Byte': 8,
        'Kilobyte': 8 * 1024,
        'Megabyte': 8 * 1024**2,
        'Gigabyte': 8 * 1024**3,
        'Terabyte': 8 * 1024**4,
        'Petabyte': 8 * 1024**5
    }
    return value * units[from_unit] / units[to_unit]



def frequency_conversion(value, from_unit, to_unit):
    units = {
        'Hertz': 1,
        'Kilohertz': 1000,
        'Megahertz': 1000000,
        'Gigahertz': 1000000000
    }
    return value * units[from_unit] / units[to_unit]

def fuel_economy_conversion(value, from_unit, to_unit):
    units = {
        'Miles per gallon': 1,
        'Miles per gallon(Imperial)': 0.832674,
        'Kilometer per liter': 0.425144,
        'Liter per 100 kilometers': 235.215
    }
    return value * units[from_unit] / units[to_unit]

def mass_conversion(value, from_unit, to_unit):
    units = {
        'Kilogram': 1000,
        'Gram': 1,
        'Milligram': 0.001,
        'Metric ton': 1000000,
        'Pound': 453.592,
        'Ounce': 28.3495,
        'Carat': 0.2
    }
    return value * units[from_unit] / units[to_unit]

def plane_angle_conversion(value, from_unit, to_unit):
    units = {
        'Degree': 1,
        'Radian': 57.2958,
        'Gradian': 0.9,
        'Milliradian': 0.057296,
        'Minute of arc': 0.016667,
        'Second of arc': 0.000278
    }
    return value * units[from_unit] / units[to_unit]



def speed_conversion(value, from_unit, to_unit):
    units = {
        'Meter per second': 1,
        'Kilometer per hour': 0.277778,
        'Mile per hour': 0.44704,
        'Knot': 0.514444,
        'Foot per second': 0.3048
    }
    return value * units[from_unit] / units[to_unit]

def time_conversion(value, from_unit, to_unit):
    units = {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2629746,
        'Year': 31556952
    }
    return value * units[from_unit] / units[to_unit]



# CONVERSION TYPES dic:
CONVERSION_TYPES = {
    'Length': {
        'units': ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
        'function': length_conversion
    },
    'Area': {
        'units': ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre'],
        'function': area_conversion
    },
     'Pressure': {
        'units': ['Pascal', 'Kilopascal', 'Bar', 'Pound per square inch', 'Atmosphere'],
        'function': pressure_conversion
    },
      'Energy': {
        'units': ['Joule', 'Kilojoule', 'Calorie', 'Kilocalorie', 'Watt-hour', 'Kilowatt-hour', 
                 'Electron volt', 'British thermal unit'],
        'function': energy_conversion
    },
    'Data Transfer Rate': {
        'units': ['Bit per second', 'Kilobit per second', 'Megabit per second', 'Gigabit per second', 
                 'Byte per second', 'Kilobyte per second', 'Megabyte per second', 'Gigabyte per second'],
        'function': data_transfer_rate_conversion
    },
    'Digital Storage': {
        'units': ['Bit', 'Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte'],
        'function': digital_storage_conversion
    },
  
    'Frequency': {
        'units': ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz'],
        'function': frequency_conversion
    },
    'Fuel Economy': {
        'units': ['Miles per gallon', 'Miles per gallon(Imperial)', 'Kilometer per liter', 'Liter per 100 kilometers'],
        'function': fuel_economy_conversion
    },
     'Time': {
        'units': ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year'],
        'function': time_conversion
    },
    'Mass': {
        'units': ['Kilogram', 'Gram', 'Milligram', 'Metric ton', 'Pound', 'Ounce', 'Carat'],
        'function': mass_conversion
    },
    'Plane Angle': {
        'units': ['Degree', 'Radian', 'Gradian', 'Milliradian', 'Minute of arc', 'Second of arc'],
        'function': plane_angle_conversion
    },
  
    'Speed': {
        'units': ['Meter per second', 'Kilometer per hour', 'Mile per hour', 'Knot', 'Foot per second'],
        'function': speed_conversion
    },
   
    'Volume': {
        'units': ['Cubic meter', 'Cubic centimeter', 'Liter', 'Milliliter', 'Gallon', 'Quart', 'Pint', 'Cup'],
        'function': volume_conversion
    }
}



# Select conversion type
conversion_type = st.selectbox('🌀 Select Conversion Type', list(CONVERSION_TYPES.keys()))


current_converter = CONVERSION_TYPES[conversion_type]

# Input value
value = st.number_input('🖍 Enter Value', value=0.0)


col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox('🎈From Unit', current_converter['units'])
with col2:
    to_unit = st.selectbox('🎯To Unit', current_converter['units'])

# Calculate and display result
if st.button('Convert'):
   
  
    result = current_converter['function'](value, from_unit, to_unit)
    st.markdown(f'<div class="stSuccess">✅ {value} {from_unit} = {result:.6f} {to_unit} ✅</div>', unsafe_allow_html=True)


st.markdown(
    f'<div class="custom-info">This converter supports {len(current_converter["units"])} different units for {conversion_type} conversion.</div>',
    unsafe_allow_html=True
)


st.divider()

#conversion message
conversion_explanations = {
    'Length': 'Convert between different units of length or distance.',
    'Area': 'Convert between different units of area or surface measurement.',
    'Mass': 'Convert between different units of mass or weight.',
    'Pressure': 'Convert between different units of pressure or force per unit area.',
    'Speed': 'Convert between different units of speed or velocity.',
    'Data Transfer Rate': 'Convert between different units of data transfer speed.',
    'Digital Storage': 'Convert between different units of digital data storage.',
    'Energy': 'Convert between different units of energy and work.',
    'Time': 'Convert between different units of time.',
    'Volume': 'Convert between different units of volume or capacity.',
    'Frequency': 'Convert between different units of frequency or rate of occurrence.',
    'Fuel Economy': 'Convert between different units of fuel consumption.',
    'Plane Angle': 'Convert between different units of angular measurement.',
   
   
}

# # st.write(conversion_explanations[conversion_type])
st.markdown('<p class="created-by">💖 Crafted with passion and precision by <b>Asia Parveen</b> 🚀</p>', unsafe_allow_html=True)


# import google.generativeai as genai

# # Gemini API Key
# API_KEY ="GEMINI_API_KEY" # Securely store this using dotenv or Streamlit secrets

# genai.configure(api_key=API_KEY)

# # Function to interact with Gemini AI
# def chat_with_gemini(prompt):
#     model = genai.GenerativeModel("gemini-pro")  # Adjust model name if needed
#     response = model.generate_content(prompt)
#     return response.text

# st.markdown("## 🤖 AI Chatbot Assistant")

# # Chatbot UI
# user_input = st.text_input("Ask me anything:")
# if user_input:
#     response = chat_with_gemini(user_input)
#     st.markdown(f"**Assistant:** {response}")










