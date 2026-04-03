def get_browser_history(commands):
    page = []
    index = -1

    for command in commands:
        if command in ["Back", "Forward"]:
            if command == "Back" and index>0:index -= 1
            if command == "Forward" and index<len(page)-1 :index += 1
        else:
            page = page[:index+1]
            page.append(command)
            index += 1
    result = [page, index]
    return result



print(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "Forward"]))
