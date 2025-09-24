name = "Hritwick" 
platform = "Python"

# # Single substitution 
# print("Welcome to %s!" % platform) 

# # Multiple substitutions 
# print("%s is learning %s." % (name, platform))


# print("Hello {}, welcome to {}!".format(name, platform))

# print("{user} is learning {lang}.".format(user=name, lang=platform))

# print("{lang} is being learned by {user}.".format(user=name,lang=platform ))


# Fstring
# print(f"Hello {name}, welcome to {platform}!")

from string import Template 
greeting = Template("Hello $name, welcome to $platform!")
print(greeting.substitute(name=name, platform=platform))


price_template = Template("The total cost is $$100.") 
print(price_template.substitute())
