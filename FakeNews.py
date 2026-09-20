import random

subjects=["Sharukh Khan ","A Fish ","Messi ","Balen shah ","A group of monkey ","Isospeed "]
actions=["launch ","cancels ","dance with ", "eats ", "declear war on ","Play Scissor paper rock "]
place_or_things=["a plate of samosa","in traffic","at meet-Galla","Biryani"," at Railway station","at FIFA world cup"]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(place_or_things)

    Headline=f"Breaking News:{subject}{action}{place_or_thing}" 
    print("\n"+ Headline)

    user=input("\nDo you want to genetate another headline?(yes/no): ").strip().lower()
    if user=="no":
        break

print("\nThanks for using Fake News Headline Generator...")
print("goodBye.....")
print("visit again.....")

#make features = store this into a file 