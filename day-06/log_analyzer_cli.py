import json
import argparse
import sys
from pathlib import Path


class LogAnalyzer:
    
    def __init__(self, log_file, level_filter=None):
        self.log_file = log_file
        self.level_filter = level_filter
        self.counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
        self.filtered_lines = []
    
    """Read log file and count log levels"""
    def analyze(self):
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    for level in self.counts:
                        if level in line:
                            self.counts[level] += 1
                            if self.level_filter is None or self.level_filter == level:
                                self.filtered_lines.append(line.strip())
                            break
            return True
        except FileNotFoundError:
            print(f"Error: Log file '{self.log_file}' not found")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    """Print summary to terminal"""
    def print_summary(self):
        print("LOG ANALYSIS SUMMARY")
        
        if self.level_filter:
            print(f"Filter: {self.level_filter}")
            print(f"Matching lines: {len(self.filtered_lines)}")
            for line in self.filtered_lines:
                print(line)
        else:
            for level, count in self.counts.items():
                print(f"{level}: {count}")
        
        print("\n")
    
    """Save summary to output file (auto-detect format)"""
    def save_output(self, output_file):
        if not output_file:
            return
        
        try:
            if output_file.endswith('.json'):
                with open(output_file, 'w') as f:
                    json.dump(self.counts, f, indent=2)
            else:
                with open(output_file, 'w') as f:
                    f.write("LOG ANALYSIS SUMMARY\n")
                    f.write("="*50 + "\n")
                    if self.level_filter:
                        f.write(f"Filter: {self.level_filter}\n")
                        f.write(f"Matching lines: {len(self.filtered_lines)}\n")
                        f.write("\n")
                        for line in self.filtered_lines:
                            f.write(line + "\n")
                    else:
                        for level, count in self.counts.items():
                            f.write(f"{level}: {count}\n")
                    f.write("\n")
            
            print(f"Summary saved to {output_file}")
        except Exception as e:
            print(f"Error saving file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="DevOps Log Analyzer Tool - Analyze log files and extract insights"
    )
    
    parser.add_argument(
        '--file',
        required=True,
        help='Path to log file (required)'
    )
    
    parser.add_argument(
        '--out',
        help='Output file path (optional, defaults to log_summary.txt)'
    )
    
    parser.add_argument(
        '--level',
        choices=['INFO', 'WARNING', 'ERROR'],
        help='Filter logs by level (INFO, WARNING, or ERROR)'
    )
    
    args = parser.parse_args()
    
    # Validate log file exists
    if not Path(args.file).exists():
        print(f"Error: Log file '{args.file}' not found")
        sys.exit(1)
    
    # Create analyzer
    analyzer = LogAnalyzer(args.file, level_filter=args.level)
    
    # Perform analysis
    if analyzer.analyze():
        analyzer.print_summary()
        
        # Determine output file
        output_file = args.out if args.out else "log_summary.txt"
        analyzer.save_output(output_file)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
