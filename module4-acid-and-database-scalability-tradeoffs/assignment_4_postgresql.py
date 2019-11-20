# How many passengers survived, and how many died? Died=545, Survived=342
'''
SELECT COUNT("Survived") FROM passengers
GROUP BY "Survived"
'''

# How many passengers were in each class?
#1st: 216, 2nd: 487, 3rd: 184
'''
SELECT COUNT("Pclass") FROM passengers
GROUP BY "Pclass"
'''

# How many passengers survived/died within each class?
# Survived: 1st: 136, 2nd: 119, 3rd: 87
'''
SELECT COUNT("Survived") FROM passengers
WHERE "Survived" = 1
GROUP BY "Pclass"
'''
# Died: 1st: 80, 2nd: 368, 3rd: 97
'''
SELECT COUNT("Survived") FROM passengers
WHERE "Survived" = 0
GROUP BY "Pclass"
'''
# What was the average age of survivors vs nonsurvivors?
# Avg survivor age: 28.41
'''
SELECT avg("Age") FROM passengers
WHERE "Survived" = 1
'''
# Avg nonsurvivor age: 30.14
'''
SELECT avg("Age") FROM passengers
WHERE "Survived" = 0
'''

# What was the average age of each passenger class?

'''
SELECT avg("Age") FROM passengers
GROUP BY "Pclass"
'''
# Avg age
# 1st: 38.79, 2nd: 25.19, 3rd: 29.87

# What was the average fare by passenger class? By survival?
# Avg fare:
# 1st: 84.15, 2nd: 13.71, 3rd: 20.66
'''
SELECT avg("Fare") FROM passengers
GROUP BY "Pclass"
'''

# Average fare by survival:
# Died: 22.21, Survived: 48.39
'''
SELECT avg("Fare") FROM passengers
GROUP BY "Survived"
'''

# How many siblings/spouses aboard on average, by passenger class? By survival?
# 1st class S/S A:0.42, 2nd: 0.62, 3rd: 0.40
'''
SELECT avg("Siblings/Spouses Aboard") FROM passengers
GROUP BY "Pclass"
'''

#Avg s/s a of those who died: 0.55, survived: 0.47
'''
SELECT avg("Siblings/Spouses Aboard") FROM passengers
GROUP BY "Survived"
'''

# How many parents/children aboard on average, by passenger class? By survival?
# Avg number of parents/children aboard, by class.
# 1st: 0.36, 2nd: 0.39, 3rd: 0.38
'''
SELECT avg("Parents/Children Aboard")
FROM passengers
GROUP BY "Pclass"
'''

# Avg number of parents/children aboard, by survival.
# Died: 0.33, Survived: 0.46
'''
SELECT avg("Parents/Children Aboard")
FROM passengers
GROUP BY "Survived"
'''

# Do any passengers have the same name? No
'''
SELECT COUNT("Name") FROM "passengers"
GROUP BY "Name"
HAVING COUNT(*) > 1
'''
