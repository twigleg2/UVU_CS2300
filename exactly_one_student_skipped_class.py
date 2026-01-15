# In Python, there are direct mappings of the three basic logical operators:
#   ∧: `and`
#   ∨: `or`
#   ¬: `not`
# In addition, we have an approximation of the universal quantifier and the existential quantifier
# in the form of Python's built-in functions:
#   ∀: `all()` 
#   ∃: `any()` 
# We can use these to solve logical propositions

SKIPPED = True
DID_NOT_SKIP = False

class1 = [SKIPPED, DID_NOT_SKIP, DID_NOT_SKIP, DID_NOT_SKIP]
class2 = [SKIPPED, SKIPPED, DID_NOT_SKIP, DID_NOT_SKIP]

# Original proposition:
#   ∃x(P(x) ∧ ∀y(x≠y → ¬P(y)))
# After De Morgans law: 
#   ∃x(P(x) ∧ ∀y(x=y ∨ ¬P(y)))
def exactly_one_student_skipped(P):
    return any(P[x] and all((x == y) or not P[y] 
                for y in range(len(P)))
            for x in range(len(P)))

print(exactly_one_student_skipped(class1))
print(exactly_one_student_skipped(class2))