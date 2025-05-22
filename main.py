import ast
import subprocess
import tempfile

def detect_python_bugs(code):
    """Use pyflakes to find errors and warnings in Python code."""
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as temp:
        temp.write(code)
        temp.flush()
        result = subprocess.run(["pyflakes", temp.name], capture_output=True, text=True)
    return result.stdout.strip() or "No bugs detected."

def explain_code_logic(code):
    """Explain logic by parsing Python code structure using AST."""
    try:
        tree = ast.parse(code)
        explanation = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                explanation.append(f"Function '{node.name}' defined with {len(node.args.args)} arguments.")
            elif isinstance(node, ast.Assign):
                targets = [ast.unparse(t) for t in node.targets]
                explanation.append(f"Assignment to {', '.join(targets)}.")
            elif isinstance(node, ast.For):
                explanation.append("Loop detected: 'for' loop.")
            elif isinstance(node, ast.While):
                explanation.append("Loop detected: 'while' loop.")
            elif isinstance(node, ast.If):
                explanation.append("Conditional statement: 'if' block.")
        return "\n".join(explanation) or "No major logic structures detected."
    except Exception as e:
        return f"Error while explaining code: {str(e)}"

def suggest_improvements(code):
    """Suggest simple improvements."""
    suggestions = []
    if "==" in code and "if" not in code:
        suggestions.append("Consider checking equality inside an 'if' statement.")
    if "print" in code and "#" not in code:
        suggestions.append("Add comments to explain what each print does.")
    if len(code) < 20:
        suggestions.append("Code is very short – try a more complex example for deeper analysis.")
    return suggestions or ["No improvements found."]

# ---------- Example usage ----------
if __name__ == "__main__":
    print("Enter your Python code (press Enter twice to finish):\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    user_code = "\n".join(lines)

    print("\n🛠️ Bug Report:\n" + "-"*50)
    print(detect_python_bugs(user_code))

    print("\n📖 Code Explanation:\n" + "-"*50)
    print(explain_code_logic(user_code))

    print("\n💡 Suggestions:\n" + "-"*50)
    for suggestion in suggest_improvements(user_code):
        print("- " + suggestion)
