import streamlit as st
import random
import array

# App title
st.title("Welcome to the password generator")

password_length = st.slider("Select password length", min_value=6, max_value=20, value=8)

# Centered generate button using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("Generate Password")

# Generate password when button is clicked
if generate:
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					         'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~', '>','*']
        
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        # combine the character randomly selected above
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        for x in range(password_length - 4):
               temp_pass = temp_pass + random.choice(COMBINED_LIST)
               temp_pass_list = array.array('u', temp_pass)
               random.shuffle(temp_pass_list)

        newpassword = ""
        for x in temp_pass_list:
             newpassword = newpassword + x[::-1]

        st.success(f"Generated Password: `{newpassword}`")

# Warning note
st.warning("⚠️ This is a mock trial to generate strong passwords, use at your own risk.")
