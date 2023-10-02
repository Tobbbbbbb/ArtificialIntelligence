class Person():

    def __init__(self, email, name, grade, prevCourses, currentCourses, commitment, extracurriculars, yearsLFA, yearsNotLFA, choices, numEvents):
        self.email = email
        self.name = name
        self.grade = grade
        self.prevCourses = prevCourses
        self.currentCourses = currentCourses
        self.commitment = commitment
        self.extracurriculars = extracurriculars
        self.yearsLFA = yearsLFA
        self.yearsNotLFA = yearsNotLFA
        self.choices = choices
        self.numEvents = numEvents
        self.partners = list()
        self.domain = list()
        self.events = list()
        self.superDomain = list()

    def assignPartners(self, partners):
        self.partners = partners
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email

    def toString(self):
        string = ""
        string += self.email + ", " + self.name + " is in grade " + str(self.grade)
        string += ", has previously taken: "
        if len(self.prevCourses) != 0:
            for elem in self.prevCourses:
                string += elem.getName() + ", "
            string = string[:-2]
        else:
            string += "nothing"
        string += " and is currently taking: "
        if len(self.currentCourses) != 0:
            for elem in self.currentCourses:
                string += elem.getName() + ", "
            string = string[:-2]
        else:
            string += "nothing"
        string += " and has done " + str(self.extracurriculars) + " ecs"
        string += ". They have commitment level " + str(self.commitment) + " and have been in scioly for " + str(self.yearsLFA) + " years at LFA and " + str(self.yearsNotLFA) + " years not at LFA"
        string += ". They want to be in " + str(self.numEvents) + " events, and their top choices are: "
        for elem in self.choices:
            string += str(elem) + ", "
        return string[:-2]

class Course():
    
    def __init__(self, name, weight, subjects, id):
        self.name = name
        self.weight = weight
        self.subjects = subjects
        self.id = id

    def getId(self):
        return self.id

    def getName(self):
        return self.name

class ExtraCurricular():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getId(self):
        return self.id

    def getName(self):
        return self.name

class Event():

    def __init__(self, name, numPeople, block, subjects, id):
        self.name = name
        self.numTruePeople = numPeople
        self.block = block
        self.subjects = subjects
        self.id = id
        self.superDomain = list()
        self.domain = list()
        self.people = list()
        self.numPeople = numPeople

    def getId(self):
        return self.id

    def getNumPeople(self):
        return self.numPeople

    def getName(self):
        return self.name

    def getBlock(self):
        return self.block