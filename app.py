
import streamlit as st
import random


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)


# --------------------------------------------------
# STORE DATA
# --------------------------------------------------

if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "search_done" not in st.session_state:
    st.session_state.search_done = False

if "passenger_details" not in st.session_state:
    st.session_state.passenger_details = []

if "current_booking" not in st.session_state:
    st.session_state.current_booking = None


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("✈️ SkyBook")
st.subheader("Flight Booking Simulator")

st.write("Welcome to SkyBook!")

st.divider()


# ==================================================
# SEARCH FLIGHTS
# ==================================================

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

        if source.lower() == destination.lower():

            st.warning(
                "From and To locations cannot be the same."
            )

        else:

            st.session_state.search_done = True

    else:

        st.warning(
            "Please enter both From and To locations."
        )


# ==================================================
# AVAILABLE FLIGHTS
# ==================================================

if st.session_state.get(
    "search_done",
    False
):

    st.divider()

    st.header("✈️ Available Flights")


    # ------------------------------------------------
    # FLIGHT 1
    # ------------------------------------------------

    st.write("### Flight 1")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ Air India")

    st.write(
        "🕐 08:00 AM - 11:00 AM"
    )

    st.write("💺 Economy")

    st.write(
        "💰 ₹6,000 per passenger"
    )


    if st.button("Book Flight 1"):

        st.session_state.selected_flight = {

            "airline": "Air India",

            "flight_number": "AI101",

            "time": "08:00 AM - 11:00 AM",

            "price": 4500,

            "class": "Economy",

            "source": source,

            "destination": destination,

            "date": str(travel_date),

            "passengers": int(passengers)
        }

        st.session_state.passenger_details = []

        st.rerun()


    st.divider()


    # ------------------------------------------------
    # FLIGHT 2
    # ------------------------------------------------

    st.write("### Flight 2")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ Emirates")

    st.write(
        "🕐 01:30 PM - 04:30 PM"
    )

    st.write("💺 Business class")

    st.write(
        "💰 ₹15,200 per passenger"
    )


    if st.button("Book Flight 2"):

        st.session_state.selected_flight = {

            "airline": "Emirates",

            "flight_number": "EK202",

            "time": "01:30 PM - 04:30 PM",

            "price": 5200,

            "class": "Business Class",

            "source": source,

            "destination": destination,

            "date": str(travel_date),

            "passengers": int(passengers)
        }

        st.session_state.passenger_details = []

        st.rerun()


    st.divider()


    # ------------------------------------------------
    # FLIGHT 3
    # ------------------------------------------------

    st.write("### Flight 3")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ IndiGo")

    st.write(
        "🕐 07:00 PM - 10:00 PM"
    )

    st.write("💺 Economy")

    st.write(
        "💰 ₹9,000 per passenger"
    )


    if st.button("Book Flight 3"):

        st.session_state.selected_flight = {

            "airline": "IndiGo",

            "flight_number": "6E303",

            "time": "07:00 PM - 10:00 PM",

            "price": 4800,

            "class": "Economy",

            "source": source,

            "destination": destination,

            "date": str(travel_date),

            "passengers": int(passengers)
        }

        st.session_state.passenger_details = []

        st.rerun()


# ==================================================
# PASSENGER DETAILS
# ==================================================

if st.session_state.selected_flight:

    flight = st.session_state.selected_flight

    st.divider()

    st.header("👤 Passenger Details")

    st.success(
        f"Selected: {flight['airline']} | "
        f"{flight['source']} → "
        f"{flight['destination']}"
    )

    st.write(
        f"📅 Date: {flight['date']}"
    )

    st.write(
        f"🕐 Time: {flight['time']}"
    )

    st.write(
        f"💺 Class: {flight['class']}"
    )

    st.write(
        f"👥 Number of Passengers: "
        f"{flight['passengers']}"
    )


    # ------------------------------------------------
    # MULTIPLE PASSENGERS
    # ------------------------------------------------

    passenger_data = []


    for i in range(
        flight["passengers"]
    ):

        st.write(
            f"### 👤 Passenger {i + 1}"
        )
