s = "A string from mod3.py"

print("THis is mod3.py")

if __name__ == "__main__":
    print("mod3.py run directly")
else:
    print("mod3.py imported")
    print(__name__)