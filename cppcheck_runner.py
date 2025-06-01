import subprocess

def run_cppcheck(file_path):
    """
    Runs Cppcheck on the given C/C++ file and returns the output.
    """
    try:
        result = subprocess.run(
            ["cppcheck", "--enable=all", "--std=c++11", file_path],
            capture_output=True,
            text=True
        )

        if result.stderr:
            return f"Cppcheck issues:\n{result.stderr}"
        else:
            return "No issues found by Cppcheck."

    except FileNotFoundError:
        return "Error: Cppcheck is not installed on this system."
