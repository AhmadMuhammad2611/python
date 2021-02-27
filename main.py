import register
import login

choice = input("""
choose 1 or 2
1) register now
2) login now
""")

if choice == "1":
    register.reg()
elif choice == "2":
    login.log()
