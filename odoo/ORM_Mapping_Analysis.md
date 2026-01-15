# ORM Mapping: Python Odoo vs PostgreSQL

## Model: inventory.product

| Python Odoo | PostgreSQL |
|------------|-----------|
| **Model Name** | **Table Name** |
| `inventory.product` | `inventory_product` |
| | |
| **Fields** | **Columns** |
| `fields.Char` (name) | `VARCHAR` (name) |
| `fields.Float` (price) | `NUMERIC` (price) |
| `fields.Integer` (stock) | `INTEGER` (stock) |

## Detailed Field Mapping

### 1. name Field
```python
# Python (Odoo ORM)
name = fields.Char(string='Product Name', required=True)
```

```sql
-- PostgreSQL
name VARCHAR NOT NULL
```

**Mapping Details:**
- Python Type: `fields.Char`
- PostgreSQL Type: `VARCHAR` (variable-length character string)
- Constraint: `NOT NULL` (because required=True)
- Index: Automatic index may be created

---

### 2. price Field
```python
# Python (Odoo ORM)
price = fields.Float(string='Price')
```

```sql
-- PostgreSQL
price NUMERIC
```

**Mapping Details:**
- Python Type: `fields.Float`
- PostgreSQL Type: `NUMERIC` or `DOUBLE PRECISION`
- Constraint: Nullable (no required=True)
- Precision: Default precision for monetary values

---

### 3. stock Field
```python
# Python (Odoo ORM)
stock = fields.Integer(string='Stock')
```

```sql
-- PostgreSQL
stock INTEGER
```

**Mapping Details:**
- Python Type: `fields.Integer`
- PostgreSQL Type: `INTEGER` (4-byte integer, range: -2147483648 to +2147483647)
- Constraint: Nullable
- Default: NULL if not specified

---

## Additional Auto-Generated Columns

Odoo ORM automatically adds these columns to every table:

| Python Field | PostgreSQL Column | Type | Description |
|-------------|------------------|------|-------------|
| `id` | `id` | `SERIAL PRIMARY KEY` | Auto-incrementing primary key |
| `create_uid` | `create_uid` | `INTEGER` | User who created the record |
| `create_date` | `create_date` | `TIMESTAMP` | Creation timestamp |
| `write_uid` | `write_uid` | `INTEGER` | Last user who modified |
| `write_date` | `write_date` | `TIMESTAMP` | Last modification timestamp |

---

## Complete Table Structure

```sql
CREATE TABLE inventory_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    price NUMERIC,
    stock INTEGER,
    create_uid INTEGER REFERENCES res_users(id),
    create_date TIMESTAMP WITHOUT TIME ZONE,
    write_uid INTEGER REFERENCES res_users(id),
    write_date TIMESTAMP WITHOUT TIME ZONE
);
```

---

## Verification Commands

After upgrading the module in Odoo, verify the table structure:

```bash
# Connect to PostgreSQL container
docker exec -it odoo17_db_container psql -U odoo -d Linhtranne

# Check table exists
\dt inventory_product

# View table structure
\d inventory_product

# View columns
SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'inventory_product';
```

---

## Field Type Reference

| Odoo Field Type | PostgreSQL Type | Notes |
|----------------|-----------------|-------|
| `fields.Char` | `VARCHAR` | Variable-length text |
| `fields.Text` | `TEXT` | Unlimited text |
| `fields.Integer` | `INTEGER` | 4-byte integer |
| `fields.Float` | `NUMERIC` or `DOUBLE PRECISION` | Decimal numbers |
| `fields.Boolean` | `BOOLEAN` | True/False |
| `fields.Date` | `DATE` | Date without time |
| `fields.Datetime` | `TIMESTAMP` | Date with time |
| `fields.Selection` | `VARCHAR` | Stores the key value |
| `fields.Many2one` | `INTEGER` | Foreign key reference |
| `fields.One2many` | - | No column (virtual field) |
| `fields.Many2many` | - | Creates junction table |
| `fields.Binary` | `BYTEA` | Binary data |

---

## Instructions to Complete the Exercise

1. **Upgrade Module in Odoo:**
   - Go to http://localhost:8069
   - Navigate to Apps
   - Search for "Training Course"
   - Click "Upgrade" button

2. **Verify Table Creation:**
   ```powershell
   docker exec odoo17_db_container psql -U odoo -d Linhtranne -c "\d inventory_product"
   ```

3. **Query Table Structure:**
   ```powershell
   docker exec odoo17_db_container psql -U odoo -d Linhtranne -c "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'inventory_product';"
   ```

4. **Insert Test Data (Optional):**
   - In Odoo UI: Training → Products → Create
   - Or via SQL:
   ```sql
   INSERT INTO inventory_product (name, price, stock, create_date, write_date)
   VALUES ('Test Product', 99.99, 100, NOW(), NOW());
   ```

5. **Query Data:**
   ```powershell
   docker exec odoo17_db_container psql -U odoo -d Linhtranne -c "SELECT id, name, price, stock FROM inventory_product;"
   ```
