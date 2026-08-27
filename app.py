import streamlit as st
import random

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)

# Store data
if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None

if "bookings" not in st.session_state:
    st.session_state.bookings = []


st.title("✈️ SkyBook")
st.subheader("Flight Booking Simulator")

st.write("Welcome to SkyBook!")

st.divider()

# SEARCH
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

        st.session_state.search_done = True

    else:

        st.warning("Please enter both From and To locations.")


# FLIGHTS
if st.session_state.get("search_done", False):

    st.divider()
    st.header("✈️ Available Flights")

    st.write("### Flight 1")
    st.write(f"🛫 {source} → {destination}")
    st.write("✈️ Air India")
    st.write("🕐 08:00 AM - 11:00 AM")
    st.write("💺 Economy")
    st.write("💰 ₹4,500 per passenger")

    if st.button("Book Flight 1"):

        st.session_state.selected_flight = {
            "airline": "Air India",
            "time": "08:00 AM - 11:00 AM",
            "price": 4500,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": passengers
        }

        st.rerun()


    st.divider()

    st.write("### Flight 2")
    st.write(f"🛫 {source} → {destination}")
    st.write("✈️ Emirates")
    st.write("🕐 01:30 PM - 04:30 PM")
    st.write("💺 Business class")
    st.write("💰 ₹5,200 per passenger")

    if st.button("Book Flight 2"):

        st.session_state.selected_flight = {
            "airline": "Emirates",
            "time": "01:30 PM - 04:30 PM",
            "price": 5200,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": passengers
        }

        st.rerun()


    st.divider()

    st.write("### Flight 3")
    st.write(f"🛫 {source} → {destination}")
    st.write("✈️ IndiGo")
    st.write("🕐 07:00 PM - 10:00 PM")
    st.write("💺 Economy")
    st.write("💰 ₹4,800 per passenger")

    if st.button("Book Flight 3"):

        st.session_state.selected_flight = {
            "airline": "IndiGo",
            "time": "07:00 PM - 10:00 PM",
            "price": 4800,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": passengers
        }

        st.rerun()


# PASSENGER DETAILS
if st.session_state.selected_flight:

    flight = st.session_state.selected_flight

    st.divider()

    st.header("👤 Passenger Details")

    st.success(
        f"Selected: {flight['airline']} | "
        f"{flight['source']} → {flight['destination']}"
    )

    name = st.text_input("Passenger Name")
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=18
    )
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("✅ Confirm Booking"):

        if name and phone and email:

            booking_id = "SB" + str(random.randint(10000, 99999))

            total = flight["price"] * flight["passengers"]

            booking = {
                "Booking ID": booking_id,
                "Passenger": name,
                "Age": age,
                "Phone": phone,
                "Email": email,
                "From": flight["source"],
                "To": flight["destination"],
                "Date": flight["date"],
                "Flight": flight["airline"],
                "Time": flight["time"],
                "Passengers": flight["passengers"],
                "Total Price": total
            }

            st.session_state.bookings.append(booking)

            st.success("🎉 Booking Confirmed!")

            st.write(f"### 🎫 Booking ID: {booking_id}")

        else:

            st.warning(
                "Please fill in all passenger details."
            )


# MY BOOKINGS
st.divider()

st.header("📋 My Bookings")

if not st.session_state.bookings:

    st.info("No bookings yet.")

else:

    for booking in st.session_state.bookings:

        st.success(
            f"🎫 Booking ID: {booking['Booking ID']}"
        )

        st.write(f"👤 Passenger: {booking['Passenger']}")
        st.write(
            f"✈️ Flight: {booking['Flight']}"
        )
        st.write(
            f"🛫 Route: {booking['From']} → {booking['To']}"
        )
        st.write(
            f"📅 Date: {booking['Date']}"
        )
        st.write(
            f"👥 Passengers: {booking['Passengers']}"
        )
        st.write(
            f"💰 Total Price: ₹{booking['Total Price']}"
        )

        st.divider()
