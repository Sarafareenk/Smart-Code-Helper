import os
from cppcheck_runner import run_cppcheck
from clang_formatter import format_code

def main():
    file_path = input("Enter the path to your code file: ").strip()

    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    file_ext = os.path.splitext(file_path)[1]

    if file_ext in ['.c', '.cpp']:
        print("\n--- Running Cppcheck ---")
        cppcheck_result = run_cppcheck(file_path)
        print(cppcheck_result)

        print("\n--- Running Clang-Format ---")
        formatted_code = format_code(file_path)
        print(formatted_code)

    elif file_ext == '.py':
        print("Python support coming from Phase 1 — not included in this script yet.")
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
v
