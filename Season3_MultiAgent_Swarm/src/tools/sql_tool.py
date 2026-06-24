import sqlite3
import os
from langchain_core.tools import tool

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'inventory.sqlite')

@tool
def check_inventory(part_name: str) -> str:
    """
    Checks the inventory database for a specific part.
    Args:
        part_name (str): The name of the part to search for (e.g., 'servo_motor_10kw').
    Returns:
        A string containing the stock quantity, unit price, and supplier information, or an alert if stock is low.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Query part info
        query = '''
        SELECT p.part_name, p.stock_quantity, p.unit_price_usd, s.supplier_name, s.contact_email
        FROM parts p
        LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
        WHERE p.part_name LIKE ?
        '''
        cursor.execute(query, (f"%{part_name}%",))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            name, stock, price, supplier, email = result
            report = f"Inventory Status for '{name}':\n"
            report += f"- Stock Quantity: {stock} units\n"
            report += f"- Unit Price: ${price}\n"
            report += f"- Supplier: {supplier} ({email})\n"
            
            if stock == 0:
                report += "\n⚠️ CRITICAL: Stock is ZERO. An automated purchase order must be issued immediately!"
            elif stock < 5:
                report += "\n⚠️ WARNING: Stock is low (less than 5). Consider reordering."
                
            return report
        else:
            return f"Part '{part_name}' not found in the inventory database."
            
    except Exception as e:
        return f"Database error: {str(e)}"

@tool
def create_purchase_order(part_name: str, quantity: int) -> str:
    """
    Creates a new purchase order for a part that is out of stock.
    Args:
        part_name (str): The name of the part to order.
        quantity (int): The amount to order.
    Returns:
        A confirmation message that the order was placed.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Find part_id
        cursor.execute("SELECT part_id FROM parts WHERE part_name LIKE ?", (f"%{part_name}%",))
        result = cursor.fetchone()
        
        if not result:
            conn.close()
            return f"Failed to order: Part '{part_name}' does not exist."
            
        part_id = result[0]
        
        # Insert PO
        cursor.execute('''
            INSERT INTO purchase_orders (part_id, order_quantity, order_status)
            VALUES (?, ?, 'PENDING')
        ''', (part_id, quantity))
        
        conn.commit()
        order_id = cursor.lastrowid
        conn.close()
        
        return f"✅ SUCCESS: Purchase Order #{order_id} created for {quantity}x '{part_name}'. Status: PENDING."
        
    except Exception as e:
        return f"Database error while creating order: {str(e)}"

# For testing
if __name__ == "__main__":
    print(check_inventory.invoke({"part_name": "tool_gripper_assembly"}))
