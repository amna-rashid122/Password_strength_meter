

# import streamlit as st

# def check_password(password):
#     score = 0
#     tips = []

#     if len(password) >= 8:
#         score += 1
#     else:
#         tips.append("🟠Password should be at least 8 characters long.")

#     if any(c.isupper() for c in password):
#         score += 1
#     else:
#         tips.append("🟣Password should contain at least one uppercase letter.")

#     if any(c.islower() for c in password):
#         score += 1
#     else:
#         tips.append("🟡Password should contain at least one lowercase letter.")

#     if any(c.isdigit() for c in password):
#         score += 1
#     else:
#         tips.append("🔵Add a number (0-9).")

#     if any(c in "!@#$%^&*()_+" for c in password):
#         score += 1
#     else:
#         tips.append(" 🟤Use a special character (!@#$%^&*()_+).")

#     return score, tips

# def main():
#     st.title("🔐 Password Strength Meter")

#     password = st.text_input("Enter your password:", type="password")

#     if password:
#         score, tips = check_password(password)

#         if score == 5:
#             st.success("✅Strong password! 🔥")
#         elif score == 3 or score == 4:
#             st.warning("🛑Moderate password. Consider improving it.")

#         else:
#             st.error("🚩Weak password. Please improve it.")       

#             for tip in tips:
#                 st.write(tip)


# if __name__ == "__main__":
#     main()


import streamlit as st

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🟠 Password should be at least 8 characters long.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("🟣 Password should contain at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("🟡 Password should contain at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("🔵 Add a number (0-9).")

    if any(c in "!@#$%^&*()_+" for c in password):
        score += 1
    else:
        tips.append("🟤 Use a special character (!@#$%^&*()_+).")

    return score, tips

def main():
    st.title("🔐 Password Strength Meter")

    password = st.text_input("Enter your password:", type="password")

    if password:
        score, tips = check_password(password)

        st.write(f"Debug: Your password score is {score}")  # Debugging line

        if score == 5:
            st.success("✅ Strong password! 🔥")
        elif score in [3, 4]:
            st.warning("🛑 Moderate password. Consider improving it.")
        else:
            st.error("🚩 Weak password. Please improve it.")

        for tip in tips:
            st.write(tip)
    else:
        st.info("Please enter a password to check its strength.")

if __name__ == "__main__":
    main()
