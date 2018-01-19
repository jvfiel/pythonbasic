
#LIST OF DICT
skills = [
            {'skill':'strike','dmg':1},
            {'skill':'tripple shot','dmg':3}
        ]
print skills

print "--------------------"

keyword = "strike"
for i,skill in enumerate(skills):
    # print skill, keyword
    # if keyword == skill:
    #     print "found!"
    #     break
    print "Skill Name: {0}, Damage: {1}".format(skill['skill'],skill['dmg'])
