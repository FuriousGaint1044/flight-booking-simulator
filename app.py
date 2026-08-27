import streamlit as st

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ SkyBook")
st.subheader("Flight Booking Simulator")

st.write("Welcome to SkyBook!")

st.divider()

st.header("Search Flights")

col1, col2 = st.columns(2)

with col1:
    source = st.text_input(
        "From",
        placeholder="e.g. Kochi"
    )

with col2:
    destination = st.text_input(
        "To",
        placeholder="e.g. Delhi"
    )

travel_date = st.date_input("Travel Date")

passengers = st.number_input(
    "Number of Passengers",
    min_value=1,
    max_value=10,
    value=1
)

if st.button("🔍 Search Flights"):

    if source and destination:

        st.success(
            f"Searching flights from {source} to {destination}"
        )

        st.write(f"📅 Date: {travel_date}")
        st.write(f"👥 Passengers: {passengers}")

    else:
        st.warning(
            "Please enter both From and To locations."
        )
