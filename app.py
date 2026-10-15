
import streamlit as st
import random

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="SkyBook",
    page_icon="✈️",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "flight" not in st.session_state:
    st.session_state.flight = None

if "passengers" not in st.session_state:
    st.session_state.passengers = []

if "booking" not in st.session_state:
    st.session_state.booking = None

if "selected_seats" not in st.session_state:
    st.session_state.selected_seats = {}

# ---------------- HEADER ----------------

st.title("✈️ SkyBook")
st.write("Your Journey, Our Responsibility")

a, b, c = st.columns(3)

with a:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with b:
    if st.button("🔎 Search Flights", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()

with c:
    if st.button("📚 My Bookings", use_container_width=True):
        st.session_state.page = "Bookings"
        st.rerun()

st.divider()

# ---------------- HOME PAGE ----------------

if st.session_state.page == "Home":

    st.header("Welcome to SkyBook! 👋")
    st.write(
        "Search flights, select seats, enter passenger "
        "details and get your flight ticket."
    )

    x, y, z = st.columns(3)

    with x:
        st.subheader("🔎 Search")
        st.write("Find your flight.")

    with y:
        st.subheader("💺 Select Seats")
        st.write("Choose seats for your passengers.")

    with z:
        st.subheader("🎫 Ticket")
        st.write("View and download your ticket.")

    if st.button("🔎 Start Booking", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()

# ---------------- SEARCH FLIGHTS ----------------

elif st.session_state.page == "Search":

    st.header("🔎 Search Flights")

    x, y = st.columns(2)

    with x:
        from_city = st.text_input(
            "From",
            placeholder="Example: Kochi"
        )

    with y:
        to_city = st.text_input(
            "To",
            placeholder="Example: Dubai"
        )

    x, y = st.columns(2)

    with x:
        travel_date = st.date_input("Travel Date")

    with y:
        people = st.number_input(
            "Passengers",
            min_value=1,
            max_value=9,
            value=1
        )

    if st.button("🔎 Search Flights", use_container_width=True):

        if not from_city.strip() or not to_city.strip():
            st.warning("Please enter both cities.")

        elif from_city.strip().lower() == to_city.strip().lower():
            st.warning("Departure and destination must be different.")

        else:
            st.session_state.from_city = from_city.strip()
            st.session_state.to_city = to_city.strip()
            st.session_state.date = travel_date
            st.session_state.people = int(people)

            st.session_state.flight = None
            st.session_state.passengers = []
            st.session_state.selected_seats = {}

            st.session_state.page = "Flights"
            st.rerun()

# ---------------- AVAILABLE FLIGHTS ----------------

elif st.session_state.page == "Flights":

    st.header("✈️ Available Flights")

    st.write(
        f"📍 {st.session_state.from_city} → "
        f"{st.session_state.to_city}"
    )

    st.write(f"📅 {st.session_state.date}")
    st.write(f"👥 Passengers: {st.session_state.people}")

    flights = [
        ["Air India", "AI-101", "08:00 AM - 11:00 AM",
         "Economy", 4500],

        ["Emirates", "EK-502", "01:30 PM - 04:30 PM",
         "Business Class", 5200],

        ["IndiGo", "6E-145", "07:00 PM - 10:00 PM",
         "Economy", 4800]
    ]

    st.info("The flights and fares below are sample project data.")

    st.divider()

    for i, f in enumerate(flights):

        st.subheader("✈️ " + f[0])

        x, y, z, w = st.columns(4)

        x.write("Flight")
        x.write(f[1])

        y.write("Time")
        y.write(f[2])

        z.write("Class")
        z.write(f[3])

        w.write("Price per passenger")
        w.write(f"₹{f[4]:,}")

        if st.button(
            "Select " + f[0],
            key="flight_" + str(i),
            use_container_width=True
        ):

            st.session_state.flight = {
                "airline": f[0],
                "number": f[1],
                "time": f[2],
                "class": f[3],
                "price": f[4],
                "count": st.session_state.people
            }

            st.session_state.passengers = []
            st.session_state.selected_seats = {}

            st.session_state.page = "Passengers"
            st.rerun()

        st.divider()

# ---------------- PASSENGER DETAILS ----------------

elif st.session_state.page == "Passengers":

    f = st.session_state.flight

    st.header("👤 Passenger Details")

    st.write(
        f"✈️ {f['airline']} | {f['number']} | "
        f"{st.session_state.from_city} → "
        f"{st.session_state.to_city}"
    )

    data = []

    for i in range(f["count"]):

        st.subheader("Passenger " + str(i + 1))

        name = st.text_input(
            "Full Name",
            key="name_" + str(i)
        )

        x, y = st.columns(2)

        with x:
            ptype = st.radio(
                "Passenger Type",
                ["Adult", "Child"],
                horizontal=True,
                key="type_" + str(i)
            )

        with y:
            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18,
                key="age_" + str(i)
            )

        x, y = st.columns(2)

        with x:
            phone = st.text_input(
                "Phone",
                key="phone_" + str(i)
            )

        with y:
            email = st.text_input(
                "Email",
                key="email_" + str(i)
            )

        data.append({
            "name": name.strip(),
            "type": ptype,
            "age": age,
            "phone": phone.strip(),
            "email": email.strip()
        })

    x, y = st.columns(2)

    with x:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "Flights"
            st.rerun()

    with y:
        if st.button(
            "Continue to Seat Selection →",
            use_container_width=True
        ):

            valid = True

            for p in data:
                if (
                    not p["name"]
                    or not p["phone"]
                    or not p["email"]
                    or "@" not in p["email"]
                ):
                    valid = False
                    break

            if valid:
                st.session_state.passengers = data
                st.session_state.selected_seats = {}
                st.session_state.page = "Seats"
                st.rerun()

            else:
                st.warning(
                    "Enter each passenger's name, phone "
                    "and a valid email address."
                )

# ---------------- SEAT SELECTION ----------------

elif st.session_state.page == "Seats":

    st.header("💺 Seat Selection")

    st.write(
        "Choose one seat for each passenger. "
        "Every passenger must have a different seat."
    )

    st.info(
        "This is a sample aircraft seat layout for your "
        "school project. Seat selection is free."
    )

    passengers = st.session_state.passengers
    seats = [
        f"{row}{letter}"
        for row in range(1, 11)
        for letter in ["A", "B", "C", "D", "E", "F"]
    ]

    selected = st.session_state.selected_seats

    st.subheader("✈️ Aircraft Seat Map")

    st.caption("Front of the aircraft")

    st.markdown("**A     B     C          D     E     F**")

    # Display the seat layout.
    for row in range(1, 11):

        cols = st.columns(6)

        for i, letter in enumerate(["A", "B", "C", "D", "E", "F"]):

            seat = f"{row}{letter}"

            with cols[i]:

                if seat in selected.values():
                    st.success("🟩 " + seat)
                else:
                    st.button(
                        "💺 " + seat,
                        key="map_" + seat,
                        disabled=True,
                        use_container_width=True
                    )

    st.caption(
        "Green seats are currently assigned. "
        "Use the passenger dropdowns below to change seats."
    )

    st.divider()

    st.subheader("Assign Seats to Passengers")

    # Set initial seat choices without duplicates.
    for i in range(len(passengers)):

        key = "seat_choice_" + str(i)

        if key not in st.session_state:
            already_used = list(selected.values())
            available = [
                seat for seat in seats
                if seat not in already_used
            ]

            if available:
                st.session_state[key] = available[0]
                selected[str(i)] = available[0]

    # Assign each passenger a unique seat.
    for i, passenger in enumerate(passengers):

        st.write(f"**Passenger {i + 1}: {passenger['name']}**")

        key = "seat_choice_" + str(i)
        current_seat = st.session_state.get(key)

        other_seats = [
            selected.get(str(j))
            for j in range(len(passengers))
            if j != i
        ]

        options = [
            seat for seat in seats
            if seat not in other_seats
        ]

        if current_seat not in options:
            current_seat = options[0]
            st.session_state[key] = current_seat

        choice = st.selectbox(
            "Choose Seat",
            options,
            index=options.index(current_seat),
            key=key
        )

        selected[str(i)] = choice

    st.session_state.selected_seats = selected

    st.divider()

    st.subheader("Selected Seats")

    for i, passenger in enumerate(passengers):
        st.write(
            f"👤 {passenger['name']} — "
            f"💺 Seat {selected[str(i)]}"
        )

    x, y = st.columns(2)

    with x:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "Passengers"
            st.rerun()

    with y:
        if st.button(
            "Continue to Payment →",
            use_container_width=True
        ):

            # Save the seat numbers with passenger details.
            for i, passenger in enumerate(passengers):
                passenger["seat"] = selected[str(i)]

            st.session_state.passengers = passengers
            st.session_state.page = "Payment"
            st.rerun()

# ---------------- PAYMENT ----------------

elif st.session_state.page == "Payment":

    f = st.session_state.flight
    passengers = st.session_state.passengers

    st.header("💳 Payment")

    base = f["price"] * len(passengers)
    gst = base * 0.05
    total = base + gst

    st.subheader("Booking Summary")

    st.write("Airline:", f["airline"])
    st.write("Flight:", f["number"])

    st.write(
        "Route:",
        st.session_state.from_city,
        "→",
        st.session_state.to_city
    )

    st.write("Date:", st.session_state.date)
    st.write("Passengers:", len(passengers))

    st.subheader("💺 Seat Details")

    for p in passengers:
        st.write(f"{p['name']}: Seat {p['seat']}")

    st.divider()

    st.write(f"Base Fare: ₹{base:,.2f}")
    st.write(f"GST (5%): ₹{gst:,.2f}")

    st.subheader(f"Total: ₹{total:,.2f}")

    st.caption(
        "Payment is simulated for this school project. "
        "No real money will be charged."
    )

    method = st.radio(
        "Payment Method",
        ["Credit / Debit Card", "UPI", "Net Banking"]
    )

    if method == "Credit / Debit Card":

        st.text_input(
            "Demo Card Number",
            placeholder="Enter any sample number"
        )

        x, y = st.columns(2)

        with x:
            st.text_input("Demo Expiry Date")

        with y:
            st.text_input("Demo CVV", type="password")

    elif method == "UPI":

        st.text_input(
            "Demo UPI ID",
            placeholder="example@upi"
        )

    else:

        st.selectbox(
            "Bank",
            [
                "SBI",
                "HDFC Bank",
                "ICICI Bank",
                "Axis Bank",
                "Canara Bank"
            ]
        )

    st.caption(
        "Do not enter real card details or banking credentials. "
        "These payment fields are only for demonstration."
    )

    x, y = st.columns(2)

    with x:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "Seats"
            st.rerun()

    with y:
        if st.button("Confirm Demo Payment", use_container_width=True):

            booking_id = "SB" + str(random.randint(10000, 99999))

            booking = {
                "id": booking_id,
                "airline": f["airline"],
                "flight": f["number"],
                "time": f["time"],
                "class": f["class"],
                "from": st.session_state.from_city,
                "to": st.session_state.to_city,
                "date": str(st.session_state.date),
                "passengers": passengers.copy(),
                "base": base,
                "gst": gst,
                "total": total,
                "method": method
            }

            st.session_state.bookings.append(booking)
            st.session_state.booking = booking
            st.session_state.page = "Ticket"
            st.rerun()

# ---------------- BOOKING CONFIRMATION ----------------

elif st.session_state.page == "Ticket":

    b = st.session_state.booking

    if b is None:
        st.warning("No booking found. Please book a flight first.")

        if st.button("Go to Home"):
            st.session_state.page = "Home"
            st.rerun()

    else:

        st.header("🎫 Booking Confirmed!")

        st.success(
            "Your sample flight booking has been confirmed."
        )

        st.subheader("Booking ID: " + b["id"])

        x, y = st.columns(2)

        with x:
            st.write("**Airline:**", b["airline"])
            st.write("**Flight:**", b["flight"])
            st.write("**From:**", b["from"])
            st.write("**To:**", b["to"])

        with y:
            st.write("**Date:**", b["date"])
            st.write("**Time:**", b["time"])
            st.write("**Class:**", b["class"])
            st.write("**Status:** Demo Confirmed")

        st.divider()

        st.subheader("👤 Passenger Details and Seats")

        for i, p in enumerate(b["passengers"]):

            st.markdown(f"**Passenger {i + 1}**")

            st.write("Name:", p["name"])
            st.write("Type:", p["type"])
            st.write("Age:", p["age"])
            st.write("Seat Number:", p["seat"])
            st.write("Phone:", p["phone"])
            st.write("Email:", p["email"])

        st.divider()

        st.subheader("💰 Payment Summary")

        st.write(f"Base Fare: ₹{b['base']:,.2f}")
        st.write(f"GST: ₹{b['gst']:,.2f}")
        st.write(f"Total: ₹{b['total']:,.2f}")
        st.write("Payment Method:", b["method"])

        # Create a downloadable text ticket.
        ticket = f"""
================================
           SKYBOOK
         FLIGHT TICKET
================================

Booking ID: {b['id']}
Airline: {b['airline']}
Flight: {b['flight']}
From: {b['from']}
To: {b['to']}
Date: {b['date']}
Time: {b['time']}
Class: {b['class']}

PASSENGERS AND SEATS
--------------------------------
"""

        for i, p in enumerate(b["passengers"]):

            ticket += f"""
Passenger {i + 1}
Name: {p['name']}
Type: {p['type']}
Age: {p['age']}
Seat Number: {p['seat']}
Phone: {p['phone']}
Email: {p['email']}
"""

        ticket += f"""
--------------------------------
Base Fare: Rs. {b['base']:.2f}
GST: Rs. {b['gst']:.2f}
Total: Rs. {b['total']:.2f}
Payment Method: {b['method']}

This is a simulated school project booking.
Thank you for choosing SkyBook!
================================
"""

        st.download_button(
            "📥 Download Ticket",
            data=ticket,
            file_name="SkyBook_" + b["id"] + ".txt",
            mime="text/plain",
            use_container_width=True
        )

        if st.button("📚 View My Bookings", use_container_width=True):
            st.session_state.page = "Bookings"
            st.rerun()

        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()

# ---------------- MY BOOKINGS ----------------

elif st.session_state.page == "Bookings":

    st.header("📚 My Bookings")

    if len(st.session_state.bookings) == 0:

        st.info("You don't have any bookings yet.")

        if st.button("✈️ Book a Flight"):
            st.session_state.page = "Search"
            st.rerun()

    else:

        for b in reversed(st.session_state.bookings):

            st.subheader("🎫 Booking ID: " + b["id"])

            st.write(
                f"✈️ {b['airline']} ({b['flight']})"
            )

            st.write(
                f"📍 {b['from']} → {b['to']}"
            )

            st.write("📅 Travel Date:", b["date"])

            st.write(f"💰 Total Fare: ₹{b['total']:,.2f}")

            st.write("Status: Demo Confirmed")

            st.markdown("**👥 Passengers and Seats**")

            for i, p in enumerate(b["passengers"]):

                st.write(
                    f"{i + 1}. {p['name']} "
                    f"({p['type']}, Age {p['age']}) "
                    f"— Seat {p['seat']}"
                )

            st.divider()

    if st.button("✈️ Book Another Flight", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()
