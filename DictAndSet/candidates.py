required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills): # Checking superset
    if skills > set(required_skills): # Checking Proper superset will eliminate Bob (He doesn't have extra skills).
                                      # Also, the operator allows only set or object, hence converting; smarter to
                                      # first convert to set before entering the loop.
        interviewees.add(candidate)

print(interviewees)
