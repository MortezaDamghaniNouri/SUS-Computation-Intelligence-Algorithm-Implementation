
import random
number_of_entities = int(input("Enter the number of entities you have: "))
i = 1
probabilities = []
while i <= number_of_entities:
    probabilities.append(float(input("Enter the probability of the " + str(i) + "th entity: ")))
    i += 1

first_ruler = [probabilities[0]]
i = 1
while i < len(probabilities):
    first_ruler.append(round(first_ruler[i - 1] + probabilities[i], 2))
    i += 1


number_of_samples = int(input("Enter the number of samples you want to generate: "))
second_ruler = [0]
i = 1
while i <= (number_of_samples - 1):
    second_ruler.append(i / number_of_samples)
    i += 1


random_number = random.uniform(0, 1 / number_of_samples)
new_second_ruler = []
for i in second_ruler:
    new_second_ruler.append(i + random_number)


result = []
i = 0
while i < len(new_second_ruler):
    j = 0
    while j < len(first_ruler):
        if j == 0:
            if 0 <= new_second_ruler[i] < first_ruler[j]:
                result.append(j + 1)
                break
        else:
            if j == (len(first_ruler) - 1):
                if first_ruler[j - 1] <= new_second_ruler[i] <= first_ruler[j]:
                    result.append(j + 1)
                    break

            else:
                if first_ruler[j - 1] <= new_second_ruler[i] < first_ruler[j]:
                    result.append(j + 1)
                    break
        j += 1
    i += 1


print("The generated random number is: " + str(random_number))
print("The selected entities numbers are: " + str(result))





























