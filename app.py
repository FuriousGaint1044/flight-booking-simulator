import streamlit as st
import random

st.set_page_config(page_title="SkyBook", page_icon="✈️", layout="wide")

# Initial values
for key, value in {
    "page": "Home", "bookings": [], "flight": None,
    "passengers": [], "booking": None, "seats": {}
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.title("✈️ SkyBook")
st.write("Your Journey, Our Responsibility")

# Navigation
a, b, c = st.columns(3)
for col, label, page in [
    (a, "🏠 Home", "Home"),
    (b, "🔎 Search Flights", "Search"),
    (c, "📚 My Bookings", "Bookings")
]:
    if col.button(label, use_container_width=True, key="nav_" + page):
        st.session_state.page = page
        st.rerun()

st.divider()
page = st.session_state.page

# Home
if page == "Home":
    st.header("Welcome to SkyBook! 👋")
    st.write("Search flights, select seats and get your ticket.")
    x, y, z = st.columns(3)
    x.subheader("🔎 Search")
    y.subheader("💺 Select Seats")
    z.subheader("🎫 Get Ticket")
    if st.button("Start Booking", key="start"):
        st.session_state.page = "Search"
        st.rerun()

# Search
elif page == "Search":
    st.header("🔎 Search Flights")
    x, y = st.columns(2)
    source = x.text_input("From", placeholder="Example: Kochi")
    destination = y.text_input("To", placeholder="Example: Delhi")
    date = st.date_input("Travel Date")
    people = st.number_input("Passengers", 1, 9, 1)

    if st.button("Search Flights", key="submit_search"):
        if not source.strip() or not destination.strip():
            st.warning("Please enter both cities.")
        elif source.strip().lower() == destination.strip().lower():
            st.warning("Departure and destination must differ.")
        else:
            st.session_state.from_city = source.strip()
            st.session_state.to_city = destination.strip()
            st.session_state.date = date
            st.session_state.people = int(people)
            st.session_state.page = "Flights"
            st.rerun()

# Flight selection
elif page == "Flights":
    st.header("✈️ Available Flights")
    st.write(
        f"{st.session_state.from_city} → "
        f"{st.session_state.to_city}"
    )
    st.write("Date:", st.session_state.date)
    st.info("Sample flights and fares for this school project.")

    flights = [
        ["Air India", "AI-101", "08:00 AM - 11:00 AM", "Economy", 4500],
        ["Emirates", "EK-502", "01:30 PM - 04:30 PM", "Business Class", 5200],
        ["IndiGo", "6E-145", "07:00 PM - 10:00 PM", "Economy", 4800]
    ]

    for i, f in enumerate(flights):
        st.subheader("✈️ " + f[0])
        st.write(f"Flight: {f[1]} | Time: {f[2]}")
        st.write(f"Class: {f[3]} | Fare: ₹{f[4]:,} per passenger")
        if st.button("Select " + f[0], key="flight_" + str(i)):
            st.session_state.flight = {
                "airline": f[0], "number": f[1], "time": f[2],
                "class": f[3], "price": f[4]
            }
            st.session_state.passengers = []
            st.session_state.seats = {}
            st.session_state.page = "Passengers"
            st.rerun()
        st.divider()

# Passenger details
elif page == "Passengers":
    st.header("👤 Passenger Details")
    data = []

    for i in range(st.session_state.people):
        st.subheader(f"Passenger {i + 1}")
        name = st.text_input("Full Name", key=f"name_{i}")
        x, y = st.columns(2)
        age = x.number_input("Age", 1, 100, 18, key=f"age_{i}")
        kind = y.selectbox("Type", ["Adult", "Child"], key=f"type_{i}")
        phone = st.text_input("Phone", key=f"phone_{i}")
        email = st.text_input("Email", key=f"email_{i}")
        data.append({
            "name": name.strip(), "age": age, "type": kind,
            "phone": phone.strip(), "email": email.strip()
        })

    if st.button("Continue to Seat Selection"):
        if any(not p["name"] or not p["phone"] or
               "@" not in p["email"] for p in data):
            st.warning("Fill in all details and enter valid emails.")
        else:
            st.session_state.passengers = data
            st.session_state.seats = {}
            st.session_state.page = "Seats"
            st.rerun()

    if st.button("Back to Flights"):
        st.session_state.page = "Flights"
        st.rerun()

# Seat selection
elif page == "Seats":
    st.header("💺 Seat Selection")
    st.write("Choose a different seat for each passenger.")
    st.caption("Rows 1–10, seats A–F.")

    seats = [
        f"{r}{letter}" for r in range(1, 11)
        for letter in ["A", "B", "C", "D", "E", "F"]
    ]
    chosen = {}

    for i, p in enumerate(st.session_state.passengers):
        old_seat = st.session_state.seats.get(str(i), seats[i])
        index = seats.index(old_seat) if old_seat in seats else i
        chosen[str(i)] = st.selectbox(
            f"{p['name']} — Seat",
            seats, index=index, key=f"seat_{i}"
        )

    st.subheader("Seat Summary")
    for i, p in enumerate(st.session_state.passengers):
        st.write(f"{p['name']}: Seat {chosen[str(i)]}")

    if st.button("Continue to Payment"):
        if len(set(chosen.values())) != len(chosen):
            st.error("Two passengers cannot share the same seat.")
        else:
            st.session_state.seats = chosen
            for i, p in enumerate(st.session_state.passengers):
                p["seat"] = chosen[str(i)]
            st.session_state.page = "Payment"
            st.rerun()

    if st.button("Back to Passenger Details"):
        st.session_state.page = "Passengers"
        st.rerun()

# Payment
elif page == "Payment":
    f = st.session_state.flight
    passengers = st.session_state.passengers
    base = f["price"] * len(passengers)
    gst = base * 0.05
    total = base + gst

    st.header("💳 Payment")
    st.write(f"Flight: {f['airline']} ({f['number']})")
    st.write(f"Route: {st.session_state.from_city} → {st.session_state.to_city}")
    st.write("Date:", st.session_state.date)

    for p in passengers:
        st.write(f"{p['name']} — Seat {p['seat']}")

    st.divider()
    st.write(f"Base Fare: ₹{base:,.2f}")
    st.write(f"GST (5%): ₹{gst:,.2f}")
    st.subheader(f"Total: ₹{total:,.2f}")

    method = st.radio("Payment Method", ["Credit / Debit Card", "UPI"])

    if method == "Credit / Debit Card":
        st.text_input("Card Number")
        x, y = st.columns(2)
        x.text_input("Expiry Date")
        y.text_input("CVV", type="password")
    else:
        st.text_input("UPI ID", placeholder="example@upi")

    if st.button("← Back to Seats"):
        st.session_state.page = "Seats"
        st.rerun()

    if st.button("Confirm Payment"):
        booking = {
            "id": "SB" + str(random.randint(10000, 99999)),
            "airline": f["airline"], "flight": f["number"],
            "time": f["time"], "class": f["class"],
            "from": st.session_state.from_city,
            "to": st.session_state.to_city,
            "date": str(st.session_state.date),
            "passengers": [p.copy() for p in passengers],
            "base": base, "gst": gst, "total": total, "method": method
        }
        st.session_state.bookings.append(booking)
        st.session_state.booking = booking
        st.session_state.page = "Ticket"
        st.rerun()

# Ticket
elif page == "Ticket":
    b = st.session_state.booking

    if b is None:
        st.warning("No booking found.")
    else:
        st.header("🎫 Booking Confirmed!")
        st.success("Your simulated booking is confirmed.")
        st.subheader("Booking ID: " + b["id"])
        st.write(f"Airline: {b['airline']} | Flight: {b['flight']}")
        st.write(f"Route: {b['from']} → {b['to']}")
        st.write(f"Date: {b['date']} | Time: {b['time']}")
        st.write("Class:", b["class"])

        st.subheader("👤 Passengers and Seats")
        for i, p in enumerate(b["passengers"]):
            st.write(
                f"{i + 1}. {p['name']} | Age {p['age']} | "
                f"{p['type']} | Seat {p['seat']}"
            )
            st.write(f"Phone: {p['phone']} | Email: {p['email']}")

        st.subheader("💰 Payment Summary")
        st.write(f"Base Fare: ₹{b['base']:,.2f}")
        st.write(f"GST: ₹{b['gst']:,.2f}")
        st.write(f"Total: ₹{b['total']:,.2f}")
        st.write("Payment Method:", b["method"])

        ticket = (
            f"SKYBOOK FLIGHT TICKET\nBooking ID: {b['id']}\n"
            f"Airline: {b['airline']}\nFlight: {b['flight']}\n"
            f"From: {b['from']}\nTo: {b['to']}\nDate: {b['date']}\n"
            f"Time: {b['time']}\nClass: {b['class']}\n\n"
        )
        for i, p in enumerate(b["passengers"]):
            ticket += (
                f"Passenger {i+1}: {p['name']}\n"
                f"Age: {p['age']} | Type: {p['type']}\n"
                f"Seat: {p['seat']}\nPhone: {p['phone']}\n"
                f"Email: {p['email']}\n\n"
            )
        ticket += (
            f"Base Fare: Rs. {b['base']:.2f}\n"
            f"GST: Rs. {b['gst']:.2f}\n"
            f"Total: Rs. {b['total']:.2f}\n"
            f"Payment Method: {b['method']}\n"
            "Simulated school project booking."
        )

        st.download_button(
            "📥 Download Ticket", ticket,
            file_name=f"SkyBook_{b['id']}.txt",
            mime="text/plain"
        )

        if st.button("View My Bookings"):
            st.session_state.page = "Bookings"
            st.rerun()
        if st.button("Back to Home"):
            st.session_state.page = "Home"
            st.rerun()

# My Bookings
elif page == "Bookings":
    st.header("📚 My Bookings")

    if not st.session_state.bookings:
        st.info("You don't have any bookings yet.")
    else:
        for b in reversed(st.session_state.bookings):
            st.subheader("🎫 " + b["id"])
            st.write(f"{b['airline']} ({b['flight']})")
            st.write(f"{b['from']} → {b['to']} | {b['date']}")
            st.write(f"Total: ₹{b['total']:,.2f} | Demo Confirmed")
            for p in b["passengers"]:
                st.write(f"👤 {p['name']} — Seat {p['seat']}")
            st.divider()

    if st.button("✈️ Book Another Flight"):
        st.session_state.page = "Search"
        st.rerun()
