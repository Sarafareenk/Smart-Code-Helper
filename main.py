import os
import subprocess
import tempfile
import ast

# -------------------- Python Code Analysis --------------------
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

# -------------------- C/C++ Code Analysis --------------------
def run_cppcheck(file_path):
    """Run cppcheck to find bugs in C/C++ code."""
    result = subprocess.run(["cppcheck", file_path], capture_output=True, text=True)
    return result.stderr.strip() or "No bugs detected."

def format_code(file_path):
    """Use clang-format to format C/C++ code."""
    result = subprocess.run(["clang-format", file_path], capture_output=True, text=True)
    return result.stdout.strip() or "No formatting changes."

# -------------------- Unified Main Logic --------------------
def main():
    file_path = input("Enter the path to your code file: ").strip()

    if not os.path.exists(file_path):
        print("❌ Error: File does not exist.")
        return

    file_ext = os.path.splitext(file_path)[1]

    if file_ext == '.py':
        with open(file_path, 'r') as f:
            code = f.read()

        print("\n🛠️ Bug Report (Python):\n" + "-"*50)
        print(detect_python_bugs(code))

        print("\n📖 Code Explanation:\n" + "-"*50)
        print(explain_code_logic(code))

        print("\n💡 Suggestions:\n" + "-"*50)
        for suggestion in suggest_improvements(code):
            print("- " + suggestion)

    elif file_ext in ['.c', '.cpp']:
        print("\n🛠️ Bug Report (Cppcheck):\n" + "-"*50)
        print(run_cppcheck(file_path))

        print("\n🧹 Formatted Code (Clang-Format):\n" + "-"*50)
        print(format_code(file_path))

    else:
        print("⚠️ Unsupported file type. Please use .py, .c, or .cpp")

if __name__ == "__main__":
    main()

