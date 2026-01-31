import json


class LogAnalyzer:
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    
    """Read log file and count log levels"""
    def analyze(self):
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    for level in self.counts:
                        if level in line:
                            self.counts[level] += 1
                            break
            return True
        except FileNotFoundError:
            print(f"Error: {self.log_file} not found")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    """Print summary to terminal"""
    def print_summary(self):
        print("LOG ANALYSIS SUMMARY")
        for level, count in self.counts.items():
            print(f"{level}: {count}")
    
    """Save summary to JSON file"""
    def save_to_json(self, output_file):
        try:
            with open(output_file, 'w') as f:
                json.dump(self.counts, f, indent=2)
            print(f"Summary saved to {output_file} (JSON)")
        except Exception as e:
            print(f"Error saving JSON: {e}")
    
    """Save summary to text file"""
    def save_to_txt(self, output_file):
        try:
            with open(output_file, 'w') as f:
                f.write("LOG ANALYSIS SUMMARY\n")
                for level, count in self.counts.items():
                    f.write(f"{level}: {count}\n")
            print(f"Summary saved to {output_file} (TXT)")
        except Exception as e:
            print(f"Error saving TXT: {e}")


# Main execution
if __name__ == "__main__":
    analyzer = LogAnalyzer("app.log")
    
    if analyzer.analyze():
        analyzer.print_summary()
        analyzer.save_to_json("log_summary.json")
        analyzer.save_to_txt("log_summary.txt")
    else:
        print("Analysis failed")


"""# Basic analysis
python log_analyzer_cli.py --file app.log

# Filter ERROR logs only
python log_analyzer_cli.py --file app.log --level ERROR

# Custom output file
python log_analyzer_cli.py --file app.log --out summary.json

# With all options
python log_analyzer_cli.py --file app.log --level WARNING --out log_summary.txt"""