shows = []
print("Welcome to Pumapix,Enter your favorite shows.")

x = 0
while x < 6:
        print("Enter a show name.")
        show = raw_input()
        if show == "done" or show == "Done":
                x = 10
        else:
                shows.append(show)

print("This is what you entered  " + str(shows))
print("We've added a couple important ones.")


y = 1

more_shows = ['Breaking Bad', 'The Wire', 'Sons of Anarchy', 'The Office']


total = shows + more_shows

total.sort()


for tv in total:
        print(str(y) + ". " + tv)
        y = y + 1
