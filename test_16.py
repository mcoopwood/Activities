import mod3_16 as mod3
print(mod3.s)
print("This is test.py")

if __name__ == "__main__":
    print("test.py run directly")
else:
    print("test.py imported")
    print(__name__)