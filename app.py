import streamlit as st
import random

st.set_page_config(page_title="SkyBook", page_icon="✈️", layout="wide")

# Session variables
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

# Header
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

# HOME PAGE
if st.session_state.page == "Home":

    st.header("Welcome to SkyBook! 👋")
    st.write("Book flights, enter passenger details and get your ticket.")

    x, y, z = st.columns(3)

    with x:
        st.subheader("🔎 Search")
        st.write("Find your flight.")

    with y:
        st.subheader("💳 Pay")
        st.write("Choose a payment method.")

    with z:
        st.subheader("🎫 Ticket")
        st.write("Get your booking ticket.")

    if st.button("🔎 Start Booking", use_container_width=True):
        st.session_state.page = "Search"
        st.rerun()

# SEARCH PAGE
elif st.session_state.page == "Search":

    st.header("🔎 Search Flights")

    x, y = st.columns(2)

    with x:
        from_city = st.text_input("From", placeholder="Example: Kochi")

    with y:
        to_city = st.text_input("To", placeholder="Example: Dubai")

    x, y = st.columns(2)

    with x:
        date = st.date_input("Travel Date")

    with y:
        people = st.number_input(
            "Passengers", min_value=1, max_value=9, value=1
        )

    if st.button("Search Flights", use_container_width=True):

        if from_city == "" or to_city == "":
            st.warning("Please enter both cities.")
        else:
            st.session_state.from_city = from_city
            st.session_state.to_city = to_city
            st.session_state.date = date
            st.session_state.people = people
            st.session_state.page = "Flights"
            st.rerun()

# FLIGHTS PAGE
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

        w.write("Price")
        w.write("₹" + str(f[4]))

        if st.button("Select " + f[0], key="f" + str(i),
                     use_container_width=True):

            st.session_state.flight = {
                "airline": f[0],
                "number": f[1],
                "time": f[2],
                "class": f[3],
                "price": f[4],
                "count": st.session_state.people
            }

            st.session_state.page = "Passengers"
            st.rerun()

        st.divider()

# PASSENGER PAGE
elif st.session_state.page == "Passengers":

    f = st.session_state.flight

    st.header("👤 Passenger Details")
    st.write(
        f"✈️ {f['airline']} | {f['number']} | "
        f"{st.session_state.from_city} → {st.session_state.to_city}"
    )

    data = []

    for i in range(f["count"]):

        st.subheader("Passenger " + str(i + 1))

        name = st.text_input(
            "Full Name", key="name" + str(i)
        )

        x, y = st.columns(2)

        with x:
            ptype = st.radio(
                "Type",
                ["Adult", "Child"],
                horizontal=True,
                key="type" + str(i)
            )

        with y:
            age = st.number_input(
                "Age", 1, 100, 18,
                key="age" + str(i)
            )

        phone = st.text_input(
            "Phone", key="phone" + str(i)
        )

        email = st.text_input(
            "Email", key="email" + str(i)
        )

        data.append({
            "name": name,
            "type": ptype,
            "age": age,
            "phone": phone,
            "email": email
        })

    x, y = st.columns(2)

    with x:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "Flights"
            st.rerun()

    with y:
        if st.button("Continue to Payment →",
                     use_container_width=True):

            ok = True

            for p in data:
                if p["name"] == "" or p["phone"] == "" or p["email"] == "":
                    ok = False

            if ok:
                st.session_state.passengers = data
                st.session_state.page = "Payment"
                st.rerun()
            else:
                st.warning("Please fill all passenger details.")

# PAYMENT PAGE
elif st.session_state.page == "Payment":

    f = st.session_state.flight
    p = st.session_state.passengers

    st.header("💳 Payment")

    base = f["price"] * len(p)
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
    st.write("Passengers:", len(p))

    st.divider()

    st.write(f"Base Fare: ₹{base:,.2f}")
    st.write(f"GST (5%): ₹{gst:,.2f}")
    st.subheader(f"Total: ₹{total:,.2f}")

    method = st.radio(
        "Payment Method",
        ["Credit / Debit Card", "UPI", "Net Banking"]
    )

    if method == "Credit / Debit Card":

        st.text_input("Card Number")
        x, y = st.columns(2)

        with x:
            st.text_input("Expiry Date")

        with y:
            st.text_input("CVV", type="password")

    elif method == "UPI":
        st.text_input("UPI ID")

    else:
        st.selectbox(
            "Bank",
            ["SBI", "HDFC Bank", "ICICI Bank",
             "Axis Bank", "Canara Bank"]
        )

    x, y = st.columns(2)

    with x:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "Passengers"
            st.rerun()

    with y:
        if st.button("💳 Pay Now", use_container_width=True):

            booking = {
                "id": "SB" + str(random.randint(10000, 99999)),
                "airline": f["airline"],
                "flight": f["number"],
                "time": f["time"],
                "class": f["class"],
                "from": st.session_state.from_city,
                "to": st.session_state.to_city,
                "date": str(st.session_state.date),
                "passengers": p,
                "base": base,
                "gst": gst,
                "total": total,
                "method": method
            }

            st.session_state.bookings.append(booking)
            st.session_state.booking = booking
            st.session_state.page = "Ticket"
            st.rerun()

# TICKET PAGE
elif st.session_state.page == "Ticket":

    b = st.session_state.booking

    st.header("🎫 Booking Confirmed!")
    st.success("Your flight has been successfully booked.")

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
        st.write("**Status:** Paid")

    st.divider()

    st.subheader("👤 Passenger Details")

    for i, p in enumerate(b["passengers"]):

        st.write("### Passenger", i + 1)
        st.write("Name:", p["name"])
        st.write("Type:", p["type"])
        st.write("Age:", p["age"])
        st.write("Phone:", p["phone"])
        st.write("Email:", p["email"])

    st.divider()

    st.subheader("💰 Payment")

    st.write(f"Base Fare: ₹{b['base']:,.2f}")
    st.write(f"GST: ₹{b['gst']:,.2f}")
    st.write(f"Total Paid: ₹{b['total']:,.2f}")
    st.write("Payment Method:", b["method"])

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

PASSENGERS
--------------------------------
"""

    for i, p in enumerate(b["passengers"]):
        ticket += f"""
Passenger {i + 1}
Name: {p['name']}
Type: {p['type']}
Age: {p['age']}
Phone: {p['phone']}
Email: {p['email']}
"""

    ticket += f"""
--------------------------------
Base Fare: ₹{b['base']:,.2f}
GST: ₹{b['gst']:,.2f}
Total Paid: ₹{b['total']:,.2f}
Payment: {b['method']}

Thank you for choosing SkyBook!
================================
"""

    st.download_button(
        "📥 Download Ticket",
        ticket,
        file_name="SkyBook_" + b["id"] + ".txt",
        use_container_width=True
    )

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

# MY BOOKINGS PAGE
elif st.session_state.page == "Bookings":

    st.header("📚 My Bookings")

    if len(st.session_state.bookings) == 0:

        st.info("You don't have any bookings yet.")

    else:

        for b in st.session_state.bookings:

            st.subheader("🎫 " + b["id"])

            st.write(
                f"✈️ {b['airline']} ({b['flight']})"
            )

            st.write(
                f"📍 {b['from']} → {b['to']}"
            )

            st.write("📅", b["date"])
            st.write(f"💰 ₹{b['total']:,.2f}")
            st.write("✅ Paid")

            for i, p in enumerate(b["passengers"]):
                st.write(
                    f"{i + 1}. {p['name']} "
                    f"({p['type']}, Age {p['age']})"
                )

            st.divider()
