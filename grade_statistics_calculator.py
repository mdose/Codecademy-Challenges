grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    print "Each grade in the class:"
    for grade in grades_input:
        print grade

def grades_sum(scores):
    score_sum = 0
    for score in scores:
        score_sum = score_sum + score
    return score_sum

def grades_average(grades_input):
    sum = grades_sum(grades_input)
    return sum / float(len(grades_input))

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    return variance / len(scores)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print_grades(grades)
print ""
print "The sum of the class grades: " + str(grades_sum(grades))
print "The class average: " + str(grades_average(grades))
print "The class variance: " + str(variance)
# Variance is how the grades varied against the class average.
# A very large variance means that the students' grades were all over the place,
# while a small variance (relatively close to the average) means that the majority
# of students did fairly well.
print "The standard deviation of the class: " + str(grades_std_deviation(variance))
# The standard deviation is the square root of the variance.
