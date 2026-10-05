import streamlit as st
import random

st.set_page_config(page_title="SkyBook", page_icon="✈️", layout="wide")

if "page" not in st.session_state: st.session_state.page = "Home"
if "bookings" not in st.session_state: st.session_state.bookings = []
if "flight" not in st.session_state: st.session_state.flight = None
if "passengers" not in st.session_state: st.session_state.passengers = []
if "booking" not in st.session_state: st.session_state.booking = None

st.title("✈️ SkyBook")
st.caption("Your Journey, Our Responsibility")

a,b,c = st.columns(3)
if a.button("🏠 Home", use_container_width=True): st.session_state.page="Home"; st.rerun()
if b.button("🔎 Search Flights", use_container_width=True): st.session_state.page="Search"; st.rerun()
if c.button("📚 My Bookings", use_container_width=True): st.session_state.page="Bookings"; st.rerun()
st.divider()

if st.session_state.page=="Home":
    st.header("Welcome to SkyBook! 👋")
    st.write("Book flights, enter passenger details, make payment and get your ticket.")
    a,b,c=st.columns(3)
    a.subheader("🔎 Search"); a.write("Find your flight.")
    b.subheader("💳 Pay"); b.write("Choose a payment method.")
    c.subheader("🎫 Ticket"); c.write("Get your booking ticket.")
    if st.button("🔎 Start Booking",use_container_width=True):
        st.session_state.page="Search"; st.rerun()

elif st.session_state.page=="Search":
    st.header("🔎 Search Flights")
    a,b=st.columns(2)
    fr=a.text_input("From",placeholder="Example: Kochi")
    to=b.text_input("To",placeholder="Example: Dubai")
    a,b=st.columns(2)
    date=a.date_input("Travel Date")
    n=b.number_input("Passengers",1,9,1)
    if st.button("Search Flights",use_container_width=True):
        if not fr or not to: st.warning("Please enter both cities.")
        else:
            st.session_state.update(fr=fr,to=to,date=date,n=n,page="Flights")
            st.rerun()

elif st.session_state.page=="Flights":
    st.header("✈️ Available Flights")
    st.write(f"📍 {st.session_state.fr} → {st.session_state.to} | 📅 {st.session_state.date} | 👥 {st.session_state.n}")

    flights=[
        ("Air India","AI-101","08:00 AM - 11:00 AM","Economy",4500),
        ("Emirates","EK-502","01:30 PM - 04:30 PM","Business Class",5200),
        ("IndiGo","6E-145","07:00 PM - 10:00 PM","Economy",4800)
    ]

    for i,f in enumerate(flights):
        st.subheader("✈️ "+f[0])
        a,b,c,d=st.columns(4)
        a.write("Flight"); a.write(f[1])
        b.write("Time"); b.write(f[2])
        c.write("Class"); c.write(f[3])
        d.write("Price"); d.write(f"₹{f[4]}")

        if st.button("Select "+f[0],key=i,use_container_width=True):
            st.session_state.flight={
                "airline":f[0],"number":f[1],"time":f[2],
                "class":f[3],"price":f[4],"count":st.session_state.n
            }
            st.session_state.page="Passengers"; st.rerun()
        st.divider()

elif st.session_state.page=="Passengers":
    f=st.session_state.flight
    st.header("👤 Passenger Details")
    st.info(f"{f['airline']} | {f['number']} | {st.session_state.fr} → {st.session_state.to}")

    data=[]
    for i in range(f["count"]):
        st.subheader(f"Passenger {i+1}")
        name=st.text_input("Full Name",key=f"name{i}")
        a,b=st.columns(2)
        typ=a.radio("Type",["Adult","Child"],horizontal=True,key=f"type{i}")
        age=b.number_input("Age",1,100,18,key=f"age{i}")
        phone=st.text_input("Phone",key=f"phone{i}")
        email=st.text_input("Email",key=f"email{i}")
        data.append({"name":name,"type":typ,"age":age,"phone":phone,"email":email})

    a,b=st.columns(2)
    if a.button("← Back",use_container_width=True):
        st.session_state.page="Flights"; st.rerun()

    if b.button("Continue to Payment →",use_container_width=True):
        if all(p["name"] and p["phone"] and p["email"] for p in data):
            st.session_state.passengers=data
            st.session_state.page="Payment"; st.rerun()
        else: st.warning("Please fill all passenger details.")

elif st.session_state.page=="Payment":
    f=st.session_state.flight
    p=st.session_state.passengers
    st.header("💳 Payment")

    base=f["price"]*len(p)
    gst=base*0.05
    total=base+gst

    st.write(f"✈️ {f['airline']} | {f['number']} | {st.session_state.fr} → {st.session_state.to}")
    st.write(f"📅 {st.session_state.date} | 👥 {len(p)} passengers")
    st.write(f"Base Fare: ₹{base:,.2f}")
    st.write(f"GST (5%): ₹{gst:,.2f}")
    st.subheader(f"Total: ₹{total:,.2f}")

    method=st.radio("Payment Method",["Credit / Debit Card","UPI","Net Banking"])

    if method=="Credit / Debit Card":
        st.text_input("Card Number")
        a,b=st.columns(2)
        a.text_input("Expiry")
        b.text_input("CVV",type="password")
    elif method=="UPI":
        st.text_input("UPI ID")
    else:
        st.selectbox("Bank",["SBI","HDFC Bank","ICICI Bank","Axis Bank","Canara Bank"])

    a,b=st.columns(2)
    if a.button("← Back",use_container_width=True):
        st.session_state.page="Passengers"; st.rerun()

    if b.button("💳 Pay Now",use_container_width=True):
        book={
            "id":"SB"+str(random.randint(10000,99999)),
            "airline":f["airline"],"flight":f["number"],"time":f["time"],
            "class":f["class"],"fr":st.session_state.fr,"to":st.session_state.to,
            "date":str(st.session_state.date),"passengers":p,
            "base":base,"gst":gst,"total":total,"method":method
        }
        st.session_state.bookings.append(book)
        st.session_state.booking=book
        st.session_state.page="Ticket"
        st.rerun()

elif st.session_state.page=="Ticket":
    b=st.session_state.booking

    st.header("🎫 Booking Confirmed!")
    st.success("Your flight has been successfully booked.")
    st.subheader("Booking ID: "+b["id"])

    a,c=st.columns(2)
    a.write(f"**Airline:** {b['airline']}")
    a.write(f"**Flight:** {b['flight']}")
    a.write(f"**From:** {b['fr']}")
    a.write(f"**To:** {b['to']}")
    c.write(f"**Date:** {b['date']}")
    c.write(f"**Time:** {b['time']}")
    c.write(f"**Class:** {b['class']}")
    c.write("**Status:** Paid")

    st.divider()
    st.subheader("👤 Passengers")

    for i,p in enumerate(b["passengers"]):
        st.write(f"{i+1}. {p['name']} | {p['type']} | Age {p['age']} | {p['phone']} | {p['email']}")

    st.subheader("💰 Payment")
    st.write(f"Base: ₹{b['base']:,.2f} | GST: ₹{b['gst']:,.2f} | Total: ₹{b['total']:,.2f} | {b['method']}")

    ticket=f"""SKYBOOK - FLIGHT TICKET
Booking ID: {b['id']}
Airline: {b['airline']} | Flight: {b['flight']}
Route: {b['fr']} -> {b['to']}
Date: {b['date']} | Time: {b['time']} | Class: {b['class']}

PASSENGERS:
"""

    for i,p in enumerate(b["passengers"]):
        ticket+=f"{i+1}. {p['name']} - {p['type']}, Age {p['age']}, Phone {p['phone']}, Email {p['email']}\n"

    ticket+=f"""
Total Paid: ₹{b['total']:,.2f}
Payment: {b['method']}
Thank you for choosing SkyBook!
"""

    st.download_button(
        "📥 Download Ticket",ticket,
        file_name="SkyBook_"+b["id"]+".txt",
        use_container_width=True
    )

    if st.button("🏠 Back to Home",use_container_width=True):
        st.session_state.page="Home"; st.rerun()

else:
    st.header("📚 My Bookings")

    if not st.session_state.bookings:
        st.info("You don't have any bookings yet.")

    for b in st.session_state.bookings:
        st.subheader("🎫 "+b["id"])
        st.write(f"✈️ {b['airline']} ({b['flight']}) | 📍 {b['fr']} → {b['to']}")
        st.write(f"📅 {b['date']} | 💰 ₹{b['total']:,.2f} | ✅ Paid")

        for i,p in enumerate(b["passengers"]):
            st.write(f"{i+1}. {p['name']} ({p['type']}, Age {p['age']})")

        st.divider()
