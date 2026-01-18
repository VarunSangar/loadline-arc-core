class MathSolver:
    def solve(self, text):
        t = text.lower()

        if "derivative" in t:
            return "Identify the outer and inner functions, then apply the chain rule."
        if "integral" in t:
            return "Look for a substitution that simplifies the expression."
        if "=" in t:
            return "Collect like terms and isolate the variable step by step."

        return "Math detected, but structure is unclear."
