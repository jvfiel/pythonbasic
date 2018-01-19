
#LISTS
skills = ['strike','tripple shot']

print "--------------------"

keyword = "tripple shot"
i = 0
for skill in skills:
    print skill, keyword, i
    if keyword == skill:
        print "found! at", i
        # break
    # print i

print "--------------------"

#SHORT VER.
if keyword in skills:
    #print "found!"
    pass
