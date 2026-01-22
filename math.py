def explain_math(problem: str) -> str:
    if "derivative" in problem:
        return "Identify inner and outer functions, then apply the chain rule."
    if "integral" in problem:
        return "Try substitution to simplify before integrating."
    return "Break the equation into solvable steps."
