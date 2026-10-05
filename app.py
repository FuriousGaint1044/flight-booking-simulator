import streamlit as st
import random
st.set_page_config(page_title="SkyBook", page_icon="✈️", layout="wide")
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None
if "passenger_details" not in st.session_state:
    st.session_state.passenger_details = []
if "search_from" not in st.session_state:
    st.session_state.search_from = ""
if "search_to" not in st.session_state:
    st.session_state.search_to = ""
if "search_date" not in st.session_state:
    st.session_state.search_date = None
if "search_passengers" not in st.session_state:
    st.session_state.search_passengers = 1
if "current_booking" not in st.session_state:
    st.session_state.current_booking = None
st.title("✈️ SkyBook")
st.write("Your Journey, Our Responsibility")
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
with c2:
    if st.button("🔎 Search Flights", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()
with c3:
    if st.button("📚 My Bookings", use_container_width=True):
        st.session_state.page = "Bookings"
        st.rerun()
st.divider()
if st.session_state.page == "Home":
    st.header("Welcome to SkyBook! 👋")
    st.write(
        "Book your flights easily, enter passenger details, "
        "make payment and get your ticket."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("🔎 Search")
        st.write("Find flights according to your travel requirements.")
    with c2:
        st.subheader("💳 Pay")
        st.write("Choose your payment method and complete your booking.")
    with c3:
        st.subheader("🎫 Fly")
        st.write("Get your booking confirmation and flight ticket.")
    st.write("")
    if st.button("🔎 Start Booking", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()
elif st.session_state.page == "Search":
    st.header("🔎 Search Flights")
    c1, c2 = st.columns(2)
    with c1:
        from_city = st.text_input(
            "From",
            placeholder="Example: Kochi"
        )
    with c2:
        to_city = st.text_input(
            "To",
            placeholder="Example: Dubai"
        )
    c1, c2 = st.columns(2)
    with c1:
        travel_date = st.date_input("Travel Date")
    with c2:
        passengers = st.number_input(
            "Number of Passengers",
            min_value=1,
            max_value=9,
            value=1
        )
    if st.button(
        "🔎 Search Flights",
        use_container_width=True,
        key="search_button"
    ):

        if from_city.strip() == "":
            st.warning("Please enter the departure city.")

        elif to_city.strip() == "":
            st.warning("Please enter the destination city.")

        else:
            st.session_state.search_from = from_city
            st.session_state.search_to = to_city
            st.session_state.search_date = travel_date
            st.session_state.search_passengers = passengers
            st.session_state.page = "Flights"
            st.rerun()


# ---------------- FLIGHTS ----------------

elif st.session_state.page == "Flights":

    st.header("✈️ Available Flights")

    st.write(
        f"📍 {st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )

    st.write(f"📅 {st.session_state.search_date}")
    st.write(f"👥 Passengers: {st.session_state.search_passengers}")

    st.divider()

    flights = [
        {
            "airline": "Air India",
            "flight": "AI-101",
            "time": "08:00 AM - 11:00 AM",
            "class": "Economy",
            "price": 4500
        },
        {
            "airline": "Emirates",
            "flight": "EK-502",
            "time": "01:30 PM - 04:30 PM",
            "class": "Business Class",
            "price": 5200
        },
        {
            "airline": "IndiGo",
            "flight": "6E-145",
            "time": "07:00 PM - 10:00 PM",
            "class": "Economy",
            "price": 4800
        }
    ]

    for i, flight in enumerate(flights):

        st.subheader("✈️ " + flight["airline"])

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.write("Flight")
            st.write(flight["flight"])

        with c2:
            st.write("Time")
            st.write(flight["time"])

        with c3:
            st.write("Class")
            st.write(flight["class"])

        with c4:
            st.write("Price")
            st.write(f"₹{flight['price']} / passenger")

        if st.button(
            "Select " + flight["airline"],
            key="flight_" + str(i),
            use_container_width=True
        ):

            flight["passengers"] = st.session_state.search_passengers

            st.session_state.selected_flight = flight
            st.session_state.page = "Passengers"
            st.rerun()

        st.divider()


# ---------------- PASSENGERS ----------------

elif st.session_state.page == "Passengers":

    flight = st.session_state.selected_flight

    st.header("👤 Passenger Details")

    st.info(
        f"{flight['airline']} | "
        f"{st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )

    st.write(f"📅 Date: {st.session_state.search_date}")
    st.write(f"✈️ Flight: {flight['flight']}")
    st.write(f"👥 Passengers: {flight['passengers']}")

    passenger_data = []

    for i in range(flight["passengers"]):

        st.subheader(f"👤 Passenger {i + 1}")

        name = st.text_input(
            "Full Name",
            key=f"name_{i}"
        )

        c1, c2 = st.columns(2)

        with c1:
            passenger_type = st.radio(
                "Passenger Type",
                ["Adult", "Child"],
                horizontal=True,
                key=f"type_{i}"
            )

        with c2:
            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18,
                key=f"age_{i}"
            )

        phone = st.text_input(
            "Phone Number",
            key=f"phone_{i}"
        )

        email = st.text_input(
            "Email",
            key=f"email_{i}"
        )

        passenger_data.append({
            "name": name,
            "type": passenger_type,
            "age": age,
            "phone": phone,
            "email": email
        })

        st.divider()

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "← Back to Flights",
            use_container_width=True
        ):
            st.session_state.page = "Flights"
            st.rerun()

    with c2:
        if st.button(
            "Continue to Payment →",
            use_container_width=True
        ):

            valid = True

            for passenger in passenger_data:

                if passenger["name"].strip() == "":
                    valid = False

                if passenger["phone"].strip() == "":
                    valid = False

                if passenger["email"].strip() == "":
                    valid = False

            if valid:
                st.session_state.passenger_details = passenger_data
                st.session_state.page = "Payment"
                st.rerun()
            else:
                st.warning("Please fill in all passenger details.")


# ---------------- PAYMENT ----------------

elif st.session_state.page == "Payment":

    flight = st.session_state.selected_flight
    passengers = st.session_state.passenger_details

    st.header("💳 Payment")

    st.subheader("Booking Summary")

    st.write(f"✈️ Airline: {flight['airline']}")
    st.write(f"🛫 Flight: {flight['flight']}")

    st.write(
        f"📍 Route: {st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )

    st.write(f"📅 Date: {st.session_state.search_date}")
    st.write(f"👥 Passengers: {len(passengers)}")

    st.divider()

    base_fare = flight["price"] * len(passengers)
    gst = base_fare * 0.05
    total = base_fare + gst

    st.write(f"Base Fare: ₹{base_fare:,.2f}")
    st.write(f"GST (5%): ₹{gst:,.2f}")

    st.subheader(f"Total Amount: ₹{total:,.2f}")

    st.divider()

    payment_method = st.radio(
        "Select Payment Method",
        [
            "Credit / Debit Card",
            "UPI",
            "Net Banking"
        ]
    )

    if payment_method == "Credit / Debit Card":

        st.text_input(
            "Card Number",
            placeholder="1234 5678 9012 3456"
        )

        c1, c2 = st.columns(2)

        with c1:
            st.text_input(
                "Expiry Date",
                placeholder="MM/YY"
            )

        with c2:
            st.text_input(
                "CVV",
                type="password"
            )

    elif payment_method == "UPI":

        st.text_input(
            "UPI ID",
            placeholder="example@upi"
        )

    else:

        st.selectbox(
            "Select Bank",
            [
                "SBI",
                "HDFC Bank",
                "ICICI Bank",
                "Axis Bank",
                "Canara Bank"
            ]
        )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "← Back to Passenger Details",
            use_container_width=True
        ):
            st.session_state.page = "Passengers"
            st.rerun()

    with c2:
        if st.button(
            "💳 Pay Now",
            use_container_width=True
        ):

            booking_id = "SB" + str(random.randint(10000, 99999))

            booking = {
                "booking_id": booking_id,
                "airline": flight["airline"],
                "flight": flight["flight"],
                "from": st.session_state.search_from,
                "to": st.session_state.search_to,
                "date": str(st.session_state.search_date),
                "time": flight["time"],
                "class": flight["class"],
                "passengers": passengers,
                "base_fare": base_fare,
                "gst": gst,
                "total": total,
                "payment_method": payment_method,
                "payment_status": "Paid"
            }

            st.session_state.bookings.append(booking)
            st.session_state.current_booking = booking
            st.session_state.page = "Ticket"
            st.rerun()


# ---------------- TICKET ----------------

elif st.session_state.page == "Ticket":

    booking = st.session_state.current_booking

    st.header("🎫 Booking Confirmed!")

    st.success("Your flight has been successfully booked.")

    st.subheader(
        f"Booking ID: {booking['booking_id']}"
    )

    st.divider()

    st.subheader("✈️ Flight Details")

    c1, c2 = st.columns(2)

    with c1:
        st.write(f"**Airline:** {booking['airline']}")
        st.write(f"**Flight:** {booking['flight']}")
        st.write(f"**From:** {booking['from']}")
        st.write(f"**To:** {booking['to']}")

    with c2:
        st.write(f"**Date:** {booking['date']}")
        st.write(f"**Time:** {booking['time']}")
        st.write(f"**Class:** {booking['class']}")
        st.write(f"**Payment:** {booking['payment_status']}")

    st.divider()

    st.subheader("👤 Passenger Details")

    for i, passenger in enumerate(booking["passengers"]):

        st.write(f"### Passenger {i + 1}")

        st.write(f"👤 Name: {passenger['name']}")
        st.write(f"🧑 Type: {passenger['type']}")
        st.write(f"🎂 Age: {passenger['age']}")
        st.write(f"📞 Phone: {passenger['phone']}")
        st.write(f"📧 Email: {passenger['email']}")

        st.divider()

    st.subheader("💰 Payment Details")

    st.write(
        f"Base Fare: ₹{booking['base_fare']:,.2f}"
    )

    st.write(
        f"GST: ₹{booking['gst']:,.2f}"
    )

    st.write(
        f"Total Paid: ₹{booking['total']:,.2f}"
    )

    st.write(
        f"Payment Method: {booking['payment_method']}"
    )

    # Ticket text for downloading
    ticket = f"""
========================================
              SKYBOOK
            FLIGHT TICKET
========================================

Booking ID: {booking['booking_id']}

Airline: {booking['airline']}
Flight: {booking['flight']}
From: {booking['from']}
To: {booking['to']}
Date: {booking['date']}
Time: {booking['time']}
Class: {booking['class']}

PASSENGER DETAILS
----------------------------------------
"""

    for i, passenger in enumerate(booking["passengers"]):

        ticket += f"""
Passenger {i + 1}
Name: {passenger['name']}
Type: {passenger['type']}
Age: {passenger['age']}
Phone: {passenger['phone']}
Email: {passenger['email']}
"""

    ticket += f"""
----------------------------------------

Base Fare: ₹{booking['base_fare']:,.2f}
GST: ₹{booking['gst']:,.2f}
Total Paid: ₹{booking['total']:,.2f}

Payment Method: {booking['payment_method']}
Payment Status: {booking['payment_status']}

========================================
       Thank you for choosing SkyBook!
========================================
"""

    st.download_button(
        "📥 Download Ticket",
        ticket,
        file_name=f"SkyBook_{booking['booking_id']}.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):
        st.session_state.page = "Home"
        st.rerun()


# ---------------- MY BOOKINGS ----------------

elif st.session_state.page == "Bookings":

    st.header("📚 My Bookings")

    if len(st.session_state.bookings) == 0:

        st.info("You don't have any bookings yet.")

        if st.button(
            "🔎 Search Flights",
            use_container_width=True
        ):
            st.session_state.page = "Search"
            st.rerun()

    else:

        for booking in st.session_state.bookings:

            st.subheader(
                f"🎫 Booking ID: {booking['booking_id']}"
            )

            st.write(
                f"✈️ {booking['airline']} "
                f"({booking['flight']})"
            )

            st.write(
                f"📍 {booking['from']} → {booking['to']}"
            )

            st.write(f"📅 {booking['date']}")

            st.write(
                f"💰 Total: ₹{booking['total']:,.2f}"
            )

            st.write(
                f"✅ Status: {booking['payment_status']}"
            )

            st.write("👤 Passengers:")

            for i, passenger in enumerate(
                booking["passengers"]
            ):

                st.write(
                    f"{i + 1}. {passenger['name']} - "
                    f"{passenger['type']} "
                    f"(Age: {passenger['age']})"
                )

            st.divider()
