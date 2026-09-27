import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "search_done" not in st.session_state:
    st.session_state.search_done = False

if "passenger_details" not in st.session_state:
    st.session_state.passenger_details = None

if "current_booking" not in st.session_state:
    st.session_state.current_booking = None


# =========================================================
# TITLE
# =========================================================

st.title("✈️ SkyBook")
st.subheader("Flight Booking Simulator")

st.write("Welcome to SkyBook!")

st.divider()


# =========================================================
# SEARCH FLIGHTS
# =========================================================

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
        st.session_state.selected_flight = None
        st.session_state.passenger_details = None
        st.session_state.current_booking = None

        st.rerun()

    else:

        st.warning(
            "Please enter both From and To locations."
        )


# =========================================================
# AVAILABLE FLIGHTS
# =========================================================

if st.session_state.search_done:

    st.divider()

    st.header("✈️ Available Flights")


    # ---------------- FLIGHT 1 ----------------

    st.write("### Flight 1")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ Air India")
    st.write("🕐 08:00 AM - 11:00 AM")
    st.write("💺 Economy")
    st.write("💰 ₹6,500 per passenger")

    if st.button("Book Flight 1"):

        st.session_state.selected_flight = {
            "airline": "Air India",
            "flight_number": "AI101",
            "time": "08:00 AM - 11:00 AM",
            "class": "Economy",
            "price": 4500,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": int(passengers)
        }

        st.session_state.passenger_details = None
        st.rerun()


    st.divider()


    # ---------------- FLIGHT 2 ----------------

    st.write("### Flight 2")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ Emirates")
    st.write("🕐 01:30 PM - 04:30 PM")
    st.write("💺 Business Class")
    st.write("💰 ₹15,200 per passenger")

    if st.button("Book Flight 2"):

        st.session_state.selected_flight = {
            "airline": "Emirates",
            "flight_number": "EK202",
            "time": "01:30 PM - 04:30 PM",
            "class": "Business Class",
            "price": 5200,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": int(passengers)
        }

        st.session_state.passenger_details = None
        st.rerun()


    st.divider()


    # ---------------- FLIGHT 3 ----------------

    st.write("### Flight 3")

    st.write(
        f"🛫 {source} → {destination}"
    )

    st.write("✈️ IndiGo")
    st.write("🕐 07:00 PM - 10:00 PM")
    st.write("💺 Economy")
    st.write("💰 ₹9,800 per passenger")

    if st.button("Book Flight 3"):

        st.session_state.selected_flight = {
            "airline": "IndiGo",
            "flight_number": "6E303",
            "time": "07:00 PM - 10:00 PM",
            "class": "Economy",
            "price": 4800,
            "source": source,
            "destination": destination,
            "date": str(travel_date),
            "passengers": int(passengers)
        }

        st.session_state.passenger_details = None
        st.rerun()


# =========================================================
# PASSENGER DETAILS
# =========================================================

if st.session_state.selected_flight:

    flight = st.session_state.selected_flight

    st.divider()

    st.header("👤 Passenger Details")

    st.success(
        f"Selected: {flight['airline']} | "
        f"{flight['source']} → {flight['destination']}"
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


    # -----------------------------------------------------
    # PASSENGER FORMS
    # -----------------------------------------------------

    passenger_data = []

    for i in range(flight["passengers"]):

    st.subheader(
        f"👤 Passenger {i + 1}"
    )

    name = st.text_input(
        f"Full Name - Passenger {i + 1}",
        key=f"name_{i}"
    )

    passenger_type = st.radio(
        f"Passenger Type - Passenger {i + 1}",
        ["Adult", "Child"],
        horizontal=True,
        key=f"type_{i}"
    )

    age = st.number_input(
        f"Age - Passenger {i + 1}",
        min_value=1,
        max_value=100,
        value=18,
        key=f"age_{i}"
    )

    phone = st.text_input(
        f"Phone Number - Passenger {i + 1}",
        key=f"phone_{i}"
    )

    email = st.text_input(
        f"Email - Passenger {i + 1}",
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

        phone = st.text_input(
            f"Phone Number - Passenger {i + 1}",
            key=f"phone_{i}"
        )

        email = st.text_input(
            f"Email - Passenger {i + 1}",
            key=f"email_{i}"
        )

        passenger_data.append({
            "name": name,
            "age": age,
            "phone": phone,
            "email": email
        })

        st.divider()


    # -----------------------------------------------------
    # CONTINUE TO PAYMENT
    # -----------------------------------------------------

    if st.button("💳 Continue to Payment"):

        details_complete = True

        for passenger in passenger_data:

            if (
                passenger["name"] == ""
                or passenger["phone"] == ""
                or passenger["email"] == ""
            ):

                details_complete = False


        if details_complete:

            st.session_state.passenger_details = passenger_data

            st.success(
                "Passenger details saved successfully!"
            )

            st.rerun()

        else:

            st.warning(
                "Please fill in all passenger details."
            )


# =========================================================
# PAYMENT PAGE
# =========================================================

if (
    st.session_state.selected_flight
    and st.session_state.passenger_details is not None
    and st.session_state.current_booking is None
):

    flight = st.session_state.selected_flight

    st.divider()

    st.header("💳 Payment Page")


    # -----------------------------------------------------
    # PRICE CALCULATION
    # -----------------------------------------------------

    base_price = (
        flight["price"]
        * flight["passengers"]
    )

    gst = base_price * 0.05

    total_price = base_price + gst


    st.write(
        f"✈️ Flight: {flight['airline']}"
    )

    st.write(
        f"🛫 Route: "
        f"{flight['source']} → "
        f"{flight['destination']}"
    )

    st.write(
        f"👥 Passengers: "
        f"{flight['passengers']}"
    )

    st.write(
        f"💰 Base Fare: ₹{base_price:.2f}"
    )

    st.write(
        f"🧾 GST (5%): ₹{gst:.2f}"
    )

    st.write(
        f"### 💵 Total Amount: ₹{total_price:.2f}"
    )


    # -----------------------------------------------------
    # PAYMENT METHOD
    # -----------------------------------------------------

    payment_method = st.radio(
        "Select Payment Method",
        [
            "Credit / Debit Card",
            "UPI",
            "Net Banking"
        ]
    )


    # -----------------------------------------------------
    # CARD
    # -----------------------------------------------------

    if payment_method == "Credit / Debit Card":

        st.text_input(
            "Card Number",
            placeholder="Enter card number"
        )

        st.text_input(
            "Card Holder Name"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                "Expiry Date",
                placeholder="MM/YY"
            )

        with col2:

            st.text_input(
                "CVV",
                type="password"
            )


    # -----------------------------------------------------
    # UPI
    # -----------------------------------------------------

    elif payment_method == "UPI":

        st.text_input(
            "UPI ID",
            placeholder="example@upi"
        )


    # -----------------------------------------------------
    # NET BANKING
    # -----------------------------------------------------

    else:

        st.selectbox(
            "Select Bank",
            [
                "State Bank of India",
                "HDFC Bank",
                "ICICI Bank",
                "Axis Bank"
            ]
        )

        st.text_input(
            "Account Number"
        )


    # -----------------------------------------------------
    # PAY NOW
    # -----------------------------------------------------

    if st.button("💰 Pay Now"):

        booking_id = (
            "SB"
            + str(random.randint(10000, 99999))
        )


        booking = {

            "Booking ID": booking_id,

            "Passengers":
                st.session_state.passenger_details,

            "From":
                flight["source"],

            "To":
                flight["destination"],

            "Date":
                flight["date"],

            "Flight":
                flight["airline"],

            "Flight Number":
                flight["flight_number"],

            "Time":
                flight["time"],

            "Class":
                flight["class"],

            "Number of Passengers":
                flight["passengers"],

            "Base Price":
                base_price,

            "GST":
                gst,

            "Total Price":
                total_price,

            "Payment Method":
                payment_method
        }


        st.session_state.bookings.append(
            booking
        )

        st.session_state.current_booking = booking

        st.success(
            "🎉 Payment Successful!"
        )

        st.rerun()


# =========================================================
# FLIGHT TICKET
# =========================================================

if st.session_state.current_booking:

    booking = st.session_state.current_booking

    st.divider()

    st.header("🎫 Flight Ticket")

    st.success(
        "🎉 Booking Confirmed!"
    )


    st.write(
        f"### 🎫 Booking ID: "
        f"{booking['Booking ID']}"
    )

    st.write("---")


    # -----------------------------------------------------
    # FLIGHT INFORMATION
    # -----------------------------------------------------

    st.subheader("✈️ Flight Information")

    st.write(
        f"**Airline:** "
        f"{booking['Flight']}"
    )

    st.write(
        f"**Flight Number:** "
        f"{booking['Flight Number']}"
    )

    st.write(
        f"**From:** "
        f"{booking['From']}"
    )

    st.write(
        f"**To:** "
        f"{booking['To']}"
    )

    st.write(
        f"**Date:** "
        f"{booking['Date']}"
    )

    st.write(
        f"**Time:** "
        f"{booking['Time']}"
    )

    st.write(
        f"**Class:** "
        f"{booking['Class']}"
    )


    st.write("---")


    # -----------------------------------------------------
    # PASSENGER INFORMATION
    # -----------------------------------------------------

    st.subheader("👥 Passenger Information")

    for i, passenger in enumerate(
        booking["Passengers"]
    ):

        st.write(
            f"### Passenger {i + 1}"
        )

        st.write(
            f"👤 Name: "
            f"{passenger['name']}"
        )

        st.write(
            f"🎂 Age: "
            f"{passenger['age']}"
        )

        st.write(
            f"📞 Phone: "
            f"{passenger['phone']}"
        )

        st.write(
            f"📧 Email: "
            f"{passenger['email']}"
        )

        st.write("---")


    # -----------------------------------------------------
    # PAYMENT INFORMATION
    # -----------------------------------------------------

    st.subheader("💳 Payment Information")

    st.write(
        f"Base Fare: "
        f"₹{booking['Base Price']:.2f}"
    )

    st.write(
        f"GST: "
        f"₹{booking['GST']:.2f}"
    )

    st.write(
        f"### Total Paid: "
        f"₹{booking['Total Price']:.2f}"
    )

    st.write(
        f"Payment Method: "
        f"{booking['Payment Method']}"
    )

    st.success("✅ Payment Status: PAID")


    # =====================================================
    # DOWNLOAD TICKET
    # =====================================================

    ticket = ""

    ticket += "========================================\n"
    ticket += "              SKYBOOK\n"
    ticket += "           FLIGHT TICKET\n"
    ticket += "========================================\n\n"

    ticket += (
        "Booking ID: "
        + booking["Booking ID"]
        + "\n\n"
    )

    ticket += (
        "Airline: "
        + booking["Flight"]
        + "\n"
    )

    ticket += (
        "Flight Number: "
        + booking["Flight Number"]
        + "\n"
    )

    ticket += (
        "From: "
        + booking["From"]
        + "\n"
    )

    ticket += (
        "To: "
        + booking["To"]
        + "\n"
    )

    ticket += (
        "Date: "
        + booking["Date"]
        + "\n"
    )

    ticket += (
        "Time: "
        + booking["Time"]
        + "\n"
    )

    ticket += (
        "Class: "
        + booking["Class"]
        + "\n\n"
    )


    ticket += "----------------------------------------\n"
    ticket += "PASSENGER DETAILS\n"
    ticket += "----------------------------------------\n\n"


    for i, passenger in enumerate(
        booking["Passengers"]
    ):

        ticket += (
            "Passenger "
            + str(i + 1)
            + "\n"
        )

        ticket += (
            "Name: "
            + passenger["name"]
            + "\n"
        )

        ticket += (
            "Age: "
            + str(passenger["age"])
            + "\n"
        )

        ticket += (
            "Phone: "
            + passenger["phone"]
            + "\n"
        )

        ticket += (
            "Email: "
            + passenger["email"]
            + "\n\n"
        )


    ticket += "----------------------------------------\n"
    ticket += "PAYMENT DETAILS\n"
    ticket += "----------------------------------------\n\n"


    ticket += (
        "Base Fare: ₹"
        + f"{booking['Base Price']:.2f}"
        + "\n"
    )

    ticket += (
        "GST: ₹"
        + f"{booking['GST']:.2f}"
        + "\n"
    )

    ticket += (
        "Total Paid: ₹"
        + f"{booking['Total Price']:.2f}"
        + "\n"
    )

    ticket += (
        "Payment Method: "
        + booking["Payment Method"]
        + "\n"
    )

    ticket += "Payment Status: PAID\n\n"

    ticket += "========================================\n"
    ticket += "       THANK YOU FOR USING SKYBOOK\n"
    ticket += "========================================\n"


    st.download_button(
        "📥 Download Flight Ticket",
        ticket,
        file_name=(
            "SkyBook_Ticket_"
            + booking["Booking ID"]
            + ".txt"
        ),
        mime="text/plain"
    )


# =========================================================
# MY BOOKINGS
# =========================================================

st.divider()

st.header("📋 My Bookings")


if not st.session_state.bookings:

    st.info(
        "No bookings yet."
    )

else:

    for booking in st.session_state.bookings:

        st.success(
            "🎫 Booking ID: "
            + booking["Booking ID"]
        )

        st.write(
            "✈️ Flight: "
            + booking["Flight"]
        )

        st.write(
            "🛫 Route: "
            + booking["From"]
            + " → "
            + booking["To"]
        )

        st.write(
            "📅 Date: "
            + booking["Date"]
        )

        st.write(
            "👥 Number of Passengers: "
            + str(booking["Number of Passengers"])
        )


        st.write("### Passengers")


        for i, passenger in enumerate(
            booking["Passengers"]
        ):

            st.write(
                str(i + 1)
                + ". "
                + passenger["name"]
                + " (Age: "
                + str(passenger["age"])
                + ")"
            )


        st.write(
            "💰 Total Price: ₹"
            + f"{booking['Total Price']:.2f}"
        )

        st.write(
            "💳 Payment: "
            + booking["Payment Method"]
        )

        st.divider()
