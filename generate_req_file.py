import subprocess
import sys

def generate_requirements_file(output_file="requirements.txt"):
    try:
        # Use pip freeze to get the list of installed packages and their versions
        result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True, check=True)
        installed_packages = result.stdout.split("\n")

        # Write the Python version as a comment
        with open(output_file, "w") as file:
            file.write(f"# Python {sys.version}\n")

            # Write the packages to the requirements.txt file
            for package in installed_packages:
                file.write(package + "\n")

        print(f"Requirements file '{output_file}' generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while generating requirements file: {e}")

if __name__ == "__main__":
    generate_requirements_file()
