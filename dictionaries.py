# each key must be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])

# the (get) function can specify a default value with it 
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not valid key"))


