import requests
from bs4 import BeautifulSoup

url = "https://www.prequeladventure.com/2011/03/prequel-begin/"

while url:
    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the div with class "entry-container fix"
    entry_fix_div = soup.find("div", class_="entry-container fix")

    # Check if the div was found
    if entry_fix_div:
        # Find all the <p> tags inside the div
        p_tags = entry_fix_div.find_all("p")

        # Open a file in write mode
        with open("p_tag_texts.txt", "a", encoding="utf8") as file:
            # Write the text from each tag to the file
            for tag in p_tags:
                if "class" in tag.attrs and tag["class"] == ["crappy-blue-link"]:
                    continue
                if "wrote:" in tag.text:
                    file.write(tag.text.replace("wrote:", "wrote: ") + "\n")
                else:
                    file.write(tag.text + "\n")

            file.write("\n")
            print("At page: " + url)

    else:
        print("Div with class 'entry-container fix' not found on the page")

    # Find the "next" link
    next_link = soup.find("td", class_="next")

    # Check if the "next" link was found
    if next_link:
        # Update the URL to follow the next link
        temp = next_link.find("a")["href"]
        url = ''.join(("https:", temp))

    else:
        # No more "next" links, set the URL to None to break the loop
        url = None