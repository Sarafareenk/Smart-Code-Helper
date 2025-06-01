import subprocess

def format_code(file_path, style="LLVM"):
    """
    Formats a C/C++ file using Clang-Format.
    :param file_path: Path to the source code file.
    :param style: Formatting style (LLVM, Google, Mozilla, etc.)
    :return: Formatted code as a string or error message.
    """
    try:
        result = subprocess.run(
            ["clang-format", f"--style={style}", file_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout  # Formatted code
        else:
            return f"Error formatting file: {result.stderr}"

    except FileNotFoundError:
        return "Error: Clang-Format is not installed on this system."
