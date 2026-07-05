import sqlite3
import pandas as pd


class LogAnalyzer:
    def __init__(self, db_path="redteam_logs.db"):
        self.db_path = db_path

    def analyze_and_export(self, output_csv="audit_export.csv"):
        """Reads from SQLite, performs basic analysis, and saves to CSV."""
        conn = sqlite3.connect(self.db_path)
        # Load logs into a pandas DataFrame
        df = pd.read_sql_query("SELECT * FROM logs", conn)
        conn.close()

        if df.empty:
            print("[!] No logs found to analyze.")
            return

        # Simple Analysis: Add a status column for readability
        df['status'] = df['detected'].apply(lambda x: 'BLOCKED' if x == 1 else 'PASSED')

        # Calculate summary metrics for your console output
        total = len(df)
        blocked = df['detected'].sum()
        passed = total - blocked

        print(f"--- Analysis Complete ---")
        print(f"Total Logs: {total}")
        print(f"Blocked: {blocked} ({(blocked / total) * 100:.1f}%)")
        print(f"Passed: {passed} ({(passed / total) * 100:.1f}%)")

        # Export the enriched data to CSV
        df.to_csv(output_csv, index=False)
        print(f"[+] Audit report saved to {output_csv}")


# Usage
if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.analyze_and_export()