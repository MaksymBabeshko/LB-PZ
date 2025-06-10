import sqlite3
import datetime

DATABASE_FILE = "security_monitoring.db"

def create_connection():
    return sqlite3.connect(DATABASE_FILE)

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EventSources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            location TEXT,
            category TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EventTypes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            severity_level TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SecurityEvents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_time TEXT,
            source_id INTEGER,
            event_type_id INTEGER,
            description TEXT,
            ip TEXT,
            user TEXT,
            FOREIGN KEY (source_id) REFERENCES EventSources(id),
            FOREIGN KEY (event_type_id) REFERENCES EventTypes(id)
        )
    ''')

    conn.commit()
    conn.close()

def seed_event_sources():
    conn = create_connection()
    cursor = conn.cursor()

    sources = [
        ("Firewall_Main", "10.0.0.1", "Firewall"),
        ("App_Server_1", "10.0.0.2", "Application Server"),
        ("IDS_Node_3", "10.0.0.3", "IDS"),
        ("Proxy_Server", "10.0.0.4", "Proxy"),
        ("Backup_Firewall", "10.0.0.99", "Firewall")
    ]

    for source in sources:
        cursor.execute("INSERT OR IGNORE INTO EventSources (name, location, category) VALUES (?, ?, ?)", source)

    conn.commit()
    conn.close()

def seed_event_types():
    conn = create_connection()
    cursor = conn.cursor()

    event_types = [
        ("Access Granted", "Informational"),
        ("Access Denied", "Warning"),
        ("Suspicious Scan", "Warning"),
        ("Malware Detected", "Critical"),
        ("System Error", "Critical")
    ]

    for etype in event_types:
        cursor.execute("INSERT OR IGNORE INTO EventTypes (name, severity_level) VALUES (?, ?)", etype)

    conn.commit()
    conn.close()

def seed_security_events():
    conn = create_connection()
    cursor = conn.cursor()

    now = datetime.datetime.now()

    
    ip_pool = [
        "10.0.0.10", "10.0.0.11", "10.0.0.12", "10.0.0.13",
        "10.0.0.14", "10.0.0.15", "10.0.0.16", "10.0.0.17",
        "10.0.0.18", "10.0.0.19", "10.0.0.20", "10.0.0.21",
        "10.0.0.22", "10.0.0.23", "10.0.0.24"
    ]

    events = []
    for i in range(15):
        event_time = (now - datetime.timedelta(minutes=i * 15)).isoformat()

        
        if i % 5 == 0:
            events.append((event_time, 1, 2, "User access denied due to invalid credentials", ip_pool[i], "root"))
        elif i % 5 == 1:
            events.append((event_time, 2, 1, "User logged in successfully", ip_pool[i], f"user{i}"))
        elif i % 5 == 2:
            events.append((event_time, 3, 3, "Suspicious scan detected from IP", ip_pool[i], None))
        elif i % 5 == 3:
            events.append((event_time, 1, 4, "Malware detected on device", ip_pool[i], f"user{i}"))
        else:
            events.append((event_time, 5, 5, "System error reported", ip_pool[i], None))

    cursor.executemany('''
        INSERT INTO SecurityEvents (event_time, source_id, event_type_id, description, ip, user)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', events)

    conn.commit()
    conn.close()

def main():
    setup_database()
    seed_event_sources()
    seed_event_types()
    seed_security_events()

    print("== Security Events Sample ==")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT se.event_time, es.name, et.name, se.description, se.ip, se.user
        FROM SecurityEvents se
        JOIN EventSources es ON se.source_id = es.id
        JOIN EventTypes et ON se.event_type_id = et.id
        ORDER BY se.event_time DESC
        LIMIT 15
    ''')

    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
