quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
index = quote.find("you")
quote = quote[:index] + "always takes longer than " + quote[index:]
print(quote)
