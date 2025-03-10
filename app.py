import re
import random
import string
import streamlit as st

# Common Passwords Blacklist
COMMON_PASSWORDS = {"password123", "123456", "qwerty", "admin", "letmein", "welcome", "passw0rd"}

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This is a commonly used password! Choose a stronger one."]

    if len(password) >= 12:
        score += 2  # Higher weight for longer passwords
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*()_+{}:;'<>,.?/~`]", password):
        score += 2  # Higher weight for special characters
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+{}:;'<>,.?/~`"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+{}:;'<>,.?/~`")
    ]
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

st.title("🔒 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)

    if score >= 5:
        st.success("✅ Strong Password! Your password is secure.")
    elif score >= 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
        for msg in feedback:
            st.write(msg)
    else:
        st.error("❌ Weak Password! Please improve it.")
        for msg in feedback:
            st.write(msg)

if st.button("🔑 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"Suggested Strong Password: {strong_password}")
