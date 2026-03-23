# ===============================
# 1️⃣ String to Integer Conversion
# ===============================
a = '10'
print("a =", a)
print("Type of a:", type(a))

# Convert string to integer
b = int(a)
print("b =", b)
print("Type of b:", type(b))

print("\n")

# ===============================
# 2️⃣ Single vs Double Quotes
# ===============================
x = 'hello from single quotes'
y = "Hello from double quotes"
print("x:", x)
print("y:", y)

print("\n")

# ===============================
# 3️⃣ Triple Quotes (Multi-line String)
# ===============================
z = """Hello from triple quotes
print the values into multiple lines"""
print("z:", z)

print("\n")

# ===============================
# 4️⃣ Quotes Inside Strings
# ===============================
# Option 1: Using triple quotes
taskGPT1 = """She said: "It's time to deploy" """
print("taskGPT1:", taskGPT1)

# Option 2: Using mixed quotes with escape
taskGPT2 = 'She said: "It\'s time to deploy"'
print("taskGPT2:", taskGPT2)

# Option 3: Using double quotes outside and single inside
taskGPT3 = "She said: \"It's time to deploy\""
print("taskGPT3:", taskGPT3)

print("\n")

# ===============================
# 5️⃣ DevOps Style Examples
# ===============================

# a) Convert user input to integer
port = int(input("Enter the port number to deploy: "))
print("Deploying on port:", port)

# b) File path example
path = "C:\\Users\\Admin\\Projects\\MyApp"
print("Project path:", path)

# c) Simulate a shell command using subprocess
import subprocess

# List current directory files (works on Windows/Linux)
result = subprocess.run(["echo", "Deploy script running..."], capture_output=True, text=True)
print(result.stdout)

# d) Environment variable example
import os
os.environ['ENV'] = 'production'
env = os.getenv('ENV')
print("Current environment:", env)
12