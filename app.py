for i in range(flight["passengers"]):

    st.subheader(f"👤 Passenger {i + 1}")

    name = st.text_input(
        f"Full Name - Passenger {i + 1}",
        key=f"name_{i}"
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
