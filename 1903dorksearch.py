import requests
from bs4 import BeautifulSoup
import os

print("=========================================")
print("|      Welcome to 1903 Hack Team!       |")
print("|      Searching for the Dark Web...    |")
print("=========================================")

keywords = input("Enter your search keywords: ")

query = keywords.replace(' ', '+')

url = f"https://www.google.com/search?q={query}"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('a')

save_file = input("Do you want to save the search results to a file? (y/n): ").lower()

if save_file == 'y':
    filename = input("Please enter a filename for the saved file: ")
    with open(os.getcwd() + f"/{filename}.txt", "w") as f:
        for link in results:
            try:
                href = link.get('href')
                if "url?q=" in href and not "webcache" in href:
                    url = href.split("?q=")[1].split("&sa=U")[0]
                    f.write(url + "\n")
                    print(f"\t{url}")
            except:
                continue
    f.close()
    print("=========================================")
    print("|           1903 Dork search done!        |")
    print(f"|  Results saved in {filename}.txt.     |")
    print("=========================================")

elif save_file == 'n':
    print("=========================================")
    print("|           1903 Dork search done!        |")
    print("|         Results not saved.            |")
    print("=========================================")

else:
    print("Invalid input. Please enter either y or n to save or not save the search results.")
