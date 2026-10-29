from datetime import datetime

print("Hello, World")
print("Is was create at 28 oct 2026")
#--
dt = datetime.now()
print("New day! Today is ", dt.strftime("%d.%m.%Y %H:%M:%S"))