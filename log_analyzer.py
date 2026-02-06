from collections import Counter

def analyze_log(file_path):
    errors = []

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line or "WARNING" in line:
                errors.append(line.strip())

    counter = Counter(errors)

    print("Error / Warning Report:")
    for error, count in counter.items():
        print(f"{count} times: {error}")

if __name__ == "__main__":
    analyze_log("sample.log")
