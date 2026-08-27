import streamlit as st
import random

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)

# Store bookings during the current session
if "bookings" not in st.session_state:
    st.session_state.bookings = []

st.title("✈️ SkyBook")
st.subheader("Flight Booking Simulator")

st.write("Welcome to SkyBook!")

st.divider()

# ---------------- SEARCH FLIGHTS ----------------

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

            st.session_state.selected_flight = {
                "airline": "SkyBook Airways",
                "time": "08:00 AM - 11:00 AM",
                "price": 4500,
                "source": source,
                "destination": destination,
                "date": str(travel_date),
                "passengers": passengers
            }

        st.divider()

        # Flight 2
        st.subheader("Flight 2")
        st.write("✈️ SkyBook Express")
        st.write(f"🛫 {source} → {destination}")
        st.write("🕐 01:30 PM - 04:30 PM")
        st.write("💺 Economy")
        st.write("💰 ₹5,200 per passenger")

        if st.button("Book Flight 2"):

            st.session_state.selected_flight = {
                "airline": "SkyBook Express",
                "time": "01:30 PM - 04:30 PM",
                "price": 5200,
                "source": source,
                "destination": destination,
                "date": str(travel_date),
                "passengers": passengers
            }

        st.divider()

        # Flight 3
        st.subheader("Flight 3")
        st.write("✈️ SkyBook Airlines")
        st.write(f"🛫 {source} → {destination}")
        st.write("🕐 07:00 PM - 10:00 PM")
        st.write("💺 Economy")
        st.write("💰 ₹4,800 per passenger")

        if st.button("Book Flight 3"):

            st.session_state.selected_flight = {
                "airline": "SkyBook Airlines",
                "time": "07:00 PM - 10:00 PM",
                "price": 4800,
                "source": source,
                "destination": destination,
                "date": str(travel_date),
                "passengers": passengers
            }

    else:

        st.warning(
            "Please enter both From and To locations."
        )


# ---------------- PASSENGER DETAILS ----------------

if "selected_flight" in st.session_state:

    st.divider()

    st.header("👤 Passenger Details")

    flight = st.session_state.selected_flight

    st.info(
        f"Selected: {flight['airline']} | "
        f"{flight['source']} → {flight['destination']}"
    )

    passenger_name = st.text_input("Passenger Name")

    passenger_age = st.number_input(
        "Passenger Age",
        min_value=1,
        max_value=100,
        value=18
    )

    passenger_phone = st.text_input(
        "Phone Number"
    )

    passenger_email = st.text_input(
        "Email"
    )

    if st.button("✅ Confirm Booking"):

        if passenger_name and passenger_phone and passenger_email:

            booking_id = "SB" + str(random.randint(10000, 99999))

            total_price = (
                flight["price"] * flight["passengers"]
            )

            booking = {
                "Booking ID": booking_id,
                "Passenger": passenger_name,
                "Age": passenger_age,
                "Phone": passenger_phone,
                "Email": passenger_email,
                "From": flight["source"],
                "To": flight["destination"],
                "Date": flight["date"],
                "Flight": flight["airline"],
                "Time": flight["time"],
                "Passengers": flight["passengers"],
                "Total Price": total_price
            }

            st.session_state.bookings.append(booking)

            st.success("🎉 Booking Confirmed!")

            st.write(f"### 🎫 Booking ID: {booking_id}")

            st.write(
                f"**Passenger:** {passenger_name}"
            )

            st.write(
                f"**Flight:** {flight['airline']}"
            )

            st.write(
                f"**Route:** {flight['source']} → "
                f"{flight['destination']}"
            )

            st.write(
                f"**Total Price:** ₹{total_price}"
            )

        else:

            st.warning(
                "Please fill in all passenger details."
            )


# ---------------- MY BOOKINGS ----------------

st.divider()

st.header("📋 My Bookings")

if len(st.session_state.bookings) == 0:

    st.info("No bookings yet.")

else:

    for booking in st.session_state.bookings:

        st.subheader(
            f"🎫 {booking['Booking ID']}"
        )

        st.write(
            f"👤 **Passenger:** {booking['Passenger']}"
        )

        st.write(
            f"✈️ **Flight:** {booking['Flight']}"
        )

        st.write(
            f"🛫 **Route:** {booking['From']} → {booking['To']}"
        )

        st.write(
            f"📅 **Date:** {booking['Date']}"
        )

        st.write(
            f"👥 **Passengers:** {booking['Passengers']}"
        )

        st.write(
            f"💰 **Total Price:** ₹{booking['Total Price']}"
        )

        st.divider()
