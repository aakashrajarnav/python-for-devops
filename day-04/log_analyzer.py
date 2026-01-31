import json

log_file = "app.log"
counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}

try:
    with open(log_file, 'r') as f:
        for line in f:
            for level in counts:
                if level in line:
                    counts[level] += 1
                    break
    
    # Print summary
    print("LOG ANALYSIS SUMMARY")
    print("\n")
    for level, count in counts.items():
        print(f"{level}: {count}")
    print("\n")
    
    with open("log_summary.json", 'w') as f:
        json.dump(counts, f, indent=2)

    print("Summary saved to log_summary.json")

except FileNotFoundError:
    print(f"Error: {log_file} not found")
except Exception as e:
    print(f"Error: {e}")
