import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'inventory.sqlite')

# Create a connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS parts (
    part_id TEXT PRIMARY KEY,
    part_name TEXT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    unit_price_usd REAL NOT NULL,
    supplier_id TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT NOT NULL,
    contact_email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS purchase_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id TEXT,
    order_quantity INTEGER,
    order_status TEXT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Clear existing data just in case
cursor.execute("DELETE FROM parts")
cursor.execute("DELETE FROM suppliers")
cursor.execute("DELETE FROM purchase_orders")

# Insert Mock Data
suppliers_data = [
    ('SUP-001', 'Hyundai Motors Corp', 'sales@hyundai-parts.com'),
    ('SUP-002', 'Siemens Automation', 'orders@siemens.com'),
    ('SUP-003', 'Local Hardware Co.', 'contact@localhw.com')
]

parts_data = [
    ('P-001', 'servo_motor_10kw', 2, 1500.00, 'SUP-002'),
    ('P-002', 'coolant_fluid_synthetic_20L', 10, 85.50, 'SUP-003'),
    ('P-003', 'tool_gripper_assembly', 0, 420.00, 'SUP-001'), # 0 stock to test auto-ordering!
    ('P-004', 'z_axis_limit_switch', 15, 35.00, 'SUP-002'),
    ('P-005', 'ethernet_cable_10m', 50, 12.00, 'SUP-003'),
    ('P-006', 'main_control_board_v2', 1, 3200.00, 'SUP-002'),
    ('P-007', 'o_ring_seal_type_b', 100, 2.50, 'SUP-003')
]

cursor.executemany("INSERT INTO suppliers VALUES (?, ?, ?)", suppliers_data)
cursor.executemany("INSERT INTO parts VALUES (?, ?, ?, ?, ?)", parts_data)

conn.commit()
conn.close()

print(f"✅ Successfully initialized {db_path} with mock data!")
