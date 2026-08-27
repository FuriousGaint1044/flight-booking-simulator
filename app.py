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

st.header("🔍 Search Flights")

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
            f"Flights found from {source} to {destination}"
        )

        st.write(f"📅 Date: {travel_date}")
        st.write(f"👥 Passengers: {passengers}")

        st.divider()

        st.header("✈️ Available Flights")

        # Flight 1
        st.subheader("Flight 1")
        st.write("✈️ SkyBook Airways")
        st.write(f"🛫 {source} → {destination}")
        st.write("🕐 08:00 AM - 11:00 AM")
        st.write("💺 Economy")
        st.write("💰 ₹4,500 per passenger")

        if st.button("Book Flight 1"):
            st.success("Flight 1 selected!")

        st.divider()

        # Flight 2
        st.subheader("Flight 2")
        st.write("✈️ SkyBook Express")
        st.write(f"🛫 {source} → {destination}")
        st.write("🕐 01:30 PM - 04:30 PM")
        st.write("💺 Economy")
        st.write("💰 ₹5,200 per passenger")

        if st.button("Book Flight 2"):
            st.success("Flight 2 selected!")

        st.divider()

        # Flight 3
        st.subheader("Flight 3")
        st.write("✈️ SkyBook Airlines")
        st.write(f"🛫 {source} → {destination}")
        st.write("🕐 07:00 PM - 10:00 PM")
        st.write("💺 Economy")
        st.write("💰 ₹4,800 per passenger")

        if st.button("Book Flight 3"):
            st.success("Flight 3 selected!")

    else:
        st.warning(
            "Please enter both From and To locations."
        )
