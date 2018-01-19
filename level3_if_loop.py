
#LISTS
skills = ['strike','tripple shot']

print "--------------------"

keyword = "strike"
for i,skill in enumerate(skills):
    print skill, keyword
    if keyword == skill:
        print "found!"
        break

print "--------------------"

#SHORT VER.
if keyword in skills:
    #print "found!"
    pass
