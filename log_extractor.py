import sqlite3
import csv


def extract_logs_to_csv(db_path, output_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all records
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()

    # Get column headers
    headers = [description[0] for description in cursor.description]

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    conn.close()
    print(f"[ENI] Successfully exported logs to {output_csv}")


if __name__ == "__main__":
    extract_logs_to_csv("redteam_logs.db", "audit_export.csv")