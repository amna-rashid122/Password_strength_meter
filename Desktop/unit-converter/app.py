
import streamlit as st

def unit_converter(value, unit_for, unit_to):
    conversions = {
        "meter": 1,
        "kilometer": 1000,
        "gram": 1,
        "kilogram": 1000
    }

    # check if units are compatible
    if unit_for in conversions and unit_to in conversions:
        # convert value to base unit (meter or gram)
        base_value = value * conversions[unit_for]
        # convert base unit to target unit
        converted_value = base_value / conversions[unit_to]
        return converted_value
    else:
        return "Conversion not supported."

# Streamlit UI
st.title("🏆➡🔑Unit Converter")

value = st.number_input("Enter value", min_value=0.0)
unit_type = st.selectbox("Choose type", ["Length", "Mass"])

if unit_type == "Length":
    units = ["meter", "kilometer"]
else:
    units = ["gram", "kilogram"]

unit_for = st.selectbox("From", units)
unit_to = st.selectbox("To", units)

if st.button("Convert"):
    result = unit_converter(value, unit_for, unit_to)
    st.success(f"{value} {unit_for} = {result} {unit_to}")

