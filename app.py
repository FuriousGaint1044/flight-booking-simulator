import streamlit as st
import random
st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None
if "passenger_details" not in st.session_state:
    st.session_state.passenger_details = []
if "current_booking" not in st.session_state:
    st.session_state.current_booking = None
if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "search_from" not in st.session_state:
    st.session_state.search_from = ""
if "search_to" not in st.session_state:
    st.session_state.search_to = ""
if "search_date" not in st.session_state:
    st.session_state.search_date = None
if "search_passengers" not in st.session_state:
    st.session_state.search_passengers = 1
st.title("✈️ SkyBook")
st.write("Your Journey, Our Responsibility")
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button(
        "🏠 Home",
        use_container_width=True
    ):
        st.session_state.page = "Home"
        st.rerun()
with col2:
    if st.button(
        "🔎 Search Flights",
        use_container_width=True
    ):
        st.session_state.page = "Search"
        st.rerun()
with col3:
    if st.button(
        "📚 My Bookings",
        use_container_width=True
    ):
        st.session_state.page = "Bookings"
        st.rerun()
st.divider()
if st.session_state.page == "Home":
    st.header("Welcome to SkyBook! 👋")
    st.write(
        "Book your flights easily, enter passenger details, "
        "make payment and get your ticket."
    )
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🔎 Search")
        st.write(
            "Find flights according to your travel requirements."
        )
    with col2:
        st.subheader("💳 Pay")
        st.write(
            "Choose your payment method and complete your booking."
        )
    with col3:
        st.subheader("🎫 Fly")
        st.write(
            "Get your booking confirmation and flight ticket."
        )
    st.write("")
    if st.button(
        "🔎 Start Booking",
        use_container_width=True
    ):
        st.session_state.page = "Search"
        st.rerun()
elif st.session_state.page == "Search":
    st.header("🔎 Search Flights")
    st.write(
        "Enter your travel details below."
    )
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        from_city = st.text_input(
            "From",
            placeholder="Example: Kochi"
        )
    with col2:
        to_city = st.text_input(
            "To",
            placeholder="Example: Dubai"
        )
    col1, col2 = st.columns(2)
    with col1:
        travel_date = st.date_input(
            "Travel Date"
        )
    with col2:
        passengers = st.number_input(
            "Number of Passengers",
            min_value=1,
            max_value=9,
            value=1,
            step=1
        )
    st.write("")
    if st.button(
    "🔎 Search Flights",
    use_container_width=True,
    key="search_flights_button"
    ):

        if from_city.strip() == "":

            st.warning(
                "Please enter the departure city."
            )


        elif to_city.strip() == "":

            st.warning(
                "Please enter the destination city."
            )


        else:

            st.session_state.search_from = from_city

            st.session_state.search_to = to_city

            st.session_state.search_date = travel_date

            st.session_state.search_passengers = passengers

            st.session_state.page = "Flights"

            st.rerun()


# ==================================================
# FLIGHT SELECTION PAGE
# ==================================================

elif st.session_state.page == "Flights":

    st.header("✈️ Available Flights")

    st.write(
        f"📍 {st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )

    st.write(
        f"📅 {st.session_state.search_date}"
    )

    st.write(
        f"👥 Passengers: "
        f"{st.session_state.search_passengers}"
    )

    st.divider()


    # --------------------------------------------------
    # AIR INDIA
    # --------------------------------------------------

    st.subheader("🇮🇳 Air India")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.write("✈️ Flight")

        st.write("AI-101")


    with col2:

        st.write("🕐 Time")

        st.write("08:00 AM - 11:00 AM")


    with col3:

        st.write("💺 Class")

        st.write("Economy")


    with col4:

        st.write("💰 Price")

        st.write("₹4,500 / passenger")


    if st.button(
        "Select Air India",
        key="air_india_button",
        use_container_width=True
    ):

        st.session_state.selected_flight = {

            "airline": "Air India",

            "flight_number": "AI-101",

            "time": "08:00 AM - 11:00 AM",

            "class": "Economy",

            "price": 4500,

            "passengers":
                st.session_state.search_passengers

        }

        st.session_state.page = "Passengers"

        st.rerun()


    st.divider()


    # --------------------------------------------------
    # EMIRATES
    # --------------------------------------------------

    st.subheader("🇦🇪 Emirates")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.write("✈️ Flight")

        st.write("EK-502")


    with col2:

        st.write("🕐 Time")

        st.write("01:30 PM - 04:30 PM")


    with col3:

        st.write("💺 Class")

        st.write("Business Class")


    with col4:

        st.write("💰 Price")

        st.write("₹5,200 / passenger")


    if st.button(
        "Select Emirates",
        key="emirates_button",
        use_container_width=True
    ):

        st.session_state.selected_flight = {

            "airline": "Emirates",

            "flight_number": "EK-502",

            "time": "01:30 PM - 04:30 PM",

            "class": "Business Class",

            "price": 5200,

            "passengers":
                st.session_state.search_passengers

        }

        st.session_state.page = "Passengers"

        st.rerun()


    st.divider()


    # --------------------------------------------------
    # INDIGO
    # --------------------------------------------------

    st.subheader("🇮🇳 IndiGo")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.write("✈️ Flight")

        st.write("6E-145")


    with col2:

        st.write("🕐 Time")

        st.write("07:00 PM - 10:00 PM")


    with col3:

        st.write("💺 Class")

        st.write("Economy")


    with col4:

        st.write("💰 Price")

        st.write("₹4,800 / passenger")


    if st.button(
        "Select IndiGo",
        key="indigo_button",
        use_container_width=True
    ):

        st.session_state.selected_flight = {

            "airline": "IndiGo",

            "flight_number": "6E-145",

            "time": "07:00 PM - 10:00 PM",

            "class": "Economy",

            "price": 4800,

            "passengers":
                st.session_state.search_passengers

        }

        st.session_state.page = "Passengers"

        st.rerun()


# ==================================================
# PASSENGER DETAILS PAGE
# ==================================================

elif st.session_state.page == "Passengers":

    flight = st.session_state.selected_flight


    st.header("👤 Passenger Details")


    st.info(
        f"Selected: {flight['airline']} | "
        f"{st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )


    st.write(
        f"📅 Date: "
        f"{st.session_state.search_date}"
    )


    st.write(
        f"✈️ Flight: "
        f"{flight['flight_number']}"
    )


    st.write(
        f"👥 Passengers: "
        f"{flight['passengers']}"
    )


    st.divider()


    passenger_data = []


    for i in range(flight["passengers"]):

        st.subheader(
            f"👤 Passenger {i + 1}"
        )


        name = st.text_input(
            f"Full Name - Passenger {i + 1}",
            key=f"passenger_name_{i}"
        )


        passenger_type = st.radio(
            f"Passenger Type - Passenger {i + 1}",
            [
                "Adult",
                "Child"
            ],
            horizontal=True,
            key=f"passenger_type_{i}"
        )


        age = st.number_input(
            f"Age - Passenger {i + 1}",
            min_value=1,
            max_value=100,
            value=18,
            step=1,
            key=f"passenger_age_{i}"
        )


        phone = st.text_input(
            f"Phone Number - Passenger {i + 1}",
            key=f"passenger_phone_{i}"
        )


        email = st.text_input(
            f"Email - Passenger {i + 1}",
            key=f"passenger_email_{i}"
        )


        passenger_data.append({

            "name": name,

            "type": passenger_type,

            "age": age,

            "phone": phone,

            "email": email

        })


        st.divider()


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "← Back to Flights",
            use_container_width=True
        ):

            st.session_state.page = "Flights"

            st.rerun()


    with col2:

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

                st.session_state.passenger_details = (
                    passenger_data
                )

                st.session_state.page = "Payment"

                st.rerun()


            else:

                st.warning(
                    "Please fill in all passenger details."
                )


# ==================================================
# PAYMENT PAGE
# ==================================================

elif st.session_state.page == "Payment":

    flight = st.session_state.selected_flight

    passengers = st.session_state.passenger_details


    st.header("💳 Payment")


    st.subheader("Booking Summary")


    st.write(
        f"✈️ Airline: "
        f"{flight['airline']}"
    )


    st.write(
        f"🛫 Flight: "
        f"{flight['flight_number']}"
    )


    st.write(
        f"📍 Route: "
        f"{st.session_state.search_from} → "
        f"{st.session_state.search_to}"
    )


    st.write(
        f"📅 Date: "
        f"{st.session_state.search_date}"
    )


    st.write(
        f"👥 Passengers: "
        f"{len(passengers)}"
    )


    st.divider()


    # --------------------------------------------------
    # PRICE CALCULATION
    # --------------------------------------------------

    base_fare = (
        flight["price"] *
        len(passengers)
    )


    gst = base_fare * 0.05


    total = base_fare + gst


    st.write(
        f"Base Fare: "
        f"₹{base_fare:,.2f}"
    )


    st.write(
        f"GST (5%): "
        f"₹{gst:,.2f}"
    )


    st.divider()


    st.subheader(
        f"Total Amount: ₹{total:,.2f}"
    )


    st.divider()


    # --------------------------------------------------
    # PAYMENT METHOD
    # --------------------------------------------------

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


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "← Back to Passenger Details",
            use_container_width=True
        ):

            st.session_state.page = "Passengers"

            st.rerun()


    with col2:

        if st.button(
            "💳 Pay Now",
            use_container_width=True
        ):

            booking_id = (
                "SB" +
                str(
                    random.randint(
                        10000,
                        99999
                    )
                )
            )


            booking = {

                "booking_id":
                    booking_id,

                "airline":
                    flight["airline"],

                "flight_number":
                    flight["flight_number"],

                "from":
                    st.session_state.search_from,

                "to":
                    st.session_state.search_to,

                "date":
                    str(
                        st.session_state.search_date
                    ),

                "time":
                    flight["time"],

                "class":
                    flight["class"],

                "passengers":
                    passengers,

                "base_fare":
                    base_fare,

                "gst":
                    gst,

                "total":
                    total,

                "payment_method":
                    payment_method,

                "payment_status":
                    "Paid"

            }


            st.session_state.current_booking = (
                booking
            )


            st.session_state.bookings.append(
                booking
            )


            st.session_state.page = "Ticket"

            st.rerun()


# ==================================================
# TICKET PAGE
# ==================================================

elif st.session_state.page == "Ticket":

    booking = st.session_state.current_booking


    st.header("🎫 Booking Confirmed!")


    st.success(
        "Your flight has been successfully booked."
    )


    st.subheader(
        f"Booking ID: "
        f"{booking['booking_id']}"
    )


    st.divider()


    # --------------------------------------------------
    # FLIGHT DETAILS
    # --------------------------------------------------

    st.subheader("✈️ Flight Details")


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            f"**Airline:** "
            f"{booking['airline']}"
        )


        st.write(
            f"**Flight:** "
            f"{booking['flight_number']}"
        )


        st.write(
            f"**From:** "
            f"{booking['from']}"
        )


        st.write(
            f"**To:** "
            f"{booking['to']}"
        )


    with col2:

        st.write(
            f"**Date:** "
            f"{booking['date']}"
        )


        st.write(
            f"**Time:** "
            f"{booking['time']}"
        )


        st.write(
            f"**Class:** "
            f"{booking['class']}"
        )


        st.write(
            f"**Payment:** "
            f"{booking['payment_status']}"
        )


    st.divider()


    # --------------------------------------------------
    # PASSENGER DETAILS
    # --------------------------------------------------

    st.subheader("👤 Passenger Details")


    for i, passenger in enumerate(
        booking["passengers"]
    ):

        st.write(
            f"### Passenger {i + 1}"
        )


        st.write(
            f"👤 Name: "
            f"{passenger['name']}"
        )


        st.write(
            f"🧑 Type: "
            f"{passenger['type']}"
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


        st.divider()


    # --------------------------------------------------
    # PAYMENT DETAILS
    # --------------------------------------------------

    st.subheader("💰 Payment Details")


    st.write(
        f"Base Fare: "
        f"₹{booking['base_fare']:,.2f}"
    )


    st.write(
        f"GST: "
        f"₹{booking['gst']:,.2f}"
    )


    st.write(
        f"Total Paid: "
        f"₹{booking['total']:,.2f}"
    )


    st.write(
        f"Payment Method: "
        f"{booking['payment_method']}"
    )


    st.divider()


    # --------------------------------------------------
    # DOWNLOADABLE TICKET
    # --------------------------------------------------

    ticket_text = ""


    ticket_text += (
        "========================================\n"
    )


    ticket_text += (
        "                 SKYBOOK\n"
    )


    ticket_text += (
        "               FLIGHT TICKET\n"
    )


    ticket_text += (
        "========================================\n\n"
    )


    ticket_text += (
        f"Booking ID: "
        f"{booking['booking_id']}\n"
    )


    ticket_text += (
        f"Airline: "
        f"{booking['airline']}\n"
    )


    ticket_text += (
        f"Flight: "
        f"{booking['flight_number']}\n"
    )


    ticket_text += (
        f"From: "
        f"{booking['from']}\n"
    )


    ticket_text += (
        f"To: "
        f"{booking['to']}\n"
    )


    ticket_text += (
        f"Date: "
        f"{booking['date']}\n"
    )


    ticket_text += (
        f"Time: "
        f"{booking['time']}\n"
    )


    ticket_text += (
        f"Class: "
        f"{booking['class']}\n\n"
    )


    ticket_text += (
        "PASSENGER DETAILS\n"
    )


    ticket_text += (
        "----------------------------------------\n"
    )


    for i, passenger in enumerate(
        booking["passengers"]
    ):

        ticket_text += (
            f"\nPassenger {i + 1}\n"
        )


        ticket_text += (
            f"Name: "
            f"{passenger['name']}\n"
        )


        ticket_text += (
            f"Type: "
            f"{passenger['type']}\n"
        )


        ticket_text += (
            f"Age: "
            f"{passenger['age']}\n"
        )


        ticket_text += (
            f"Phone: "
            f"{passenger['phone']}\n"
        )


        ticket_text += (
            f"Email: "
            f"{passenger['email']}\n"
        )


    ticket_text += (
        "\n----------------------------------------\n"
    )


    ticket_text += (
        f"Base Fare: "
        f"₹{booking['base_fare']:,.2f}\n"
    )


    ticket_text += (
        f"GST: "
        f"₹{booking['gst']:,.2f}\n"
    )


    ticket_text += (
        f"Total Paid: "
        f"₹{booking['total']:,.2f}\n"
    )


    ticket_text += (
        f"Payment Method: "
        f"{booking['payment_method']}\n"
    )


    ticket_text += (
        f"Payment Status: "
        f"{booking['payment_status']}\n"
    )


    ticket_text += (
        "\n========================================\n"
    )


    ticket_text += (
        "       Thank you for choosing SkyBook!\n"
    )


    ticket_text += (
        "========================================\n"
    )


    st.download_button(
        "📥 Download Ticket",
        ticket_text,
        file_name=(
            f"SkyBook_"
            f"{booking['booking_id']}.txt"
        ),
        mime="text/plain",
        use_container_width=True
    )


    st.write("")


    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


# ==================================================
# MY BOOKINGS PAGE
# ==================================================

elif st.session_state.page == "Bookings":

    st.header("📚 My Bookings")


    if len(st.session_state.bookings) == 0:

        st.info(
            "You don't have any bookings yet."
        )


        if st.button(
            "🔎 Search Flights",
            use_container_width=True
        ):

            st.session_state.page = "Search"

            st.rerun()


    else:

        for booking in st.session_state.bookings:

            st.subheader(
                f"🎫 Booking ID: "
                f"{booking['booking_id']}"
            )


            st.write(
                f"✈️ {booking['airline']} "
                f"({booking['flight_number']})"
            )


            st.write(
                f"📍 {booking['from']} → "
                f"{booking['to']}"
            )


            st.write(
                f"📅 {booking['date']}"
            )


            st.write(
                f"💰 Total: "
                f"₹{booking['total']:,.2f}"
            )


            st.write(
                f"✅ Status: "
                f"{booking['payment_status']}"
            )


            st.write("👤 Passengers:")


            for i, passenger in enumerate(
                booking["passengers"]
            ):

                st.write(
                    f"{i + 1}. "
                    f"{passenger['name']} - "
                    f"{passenger['type']} "
                    f"(Age: {passenger['age']})"
                )


            st.divider()
