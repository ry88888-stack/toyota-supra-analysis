import sqlite3

# データベースを作成
conn = sqlite3.connect("data/toyota_supra.db")

cursor = conn.cursor()

# スープラのデータを保存するテーブル
cursor.execute("DROP TABLE IF EXISTS supra_models")
cursor.execute("""

CREATE TABLE IF NOT EXISTS supra_models (
    id INTEGER PRIMARY KEY,
    generation TEXT,
    model_name TEXT,
    engine TEXT,
    horsepower INTEGER,
    release_year INTEGER,
    displacement_cc INTEGER,
    torque_nm INTEGER
)
""")

conn.commit()

print("Toyota Supra Database created!")
# サンプルデータを登録
supra_data = [
    ("A80", "RZ", "2JZ-GTE", 280, 1997, 2997, 451),
    ("A90", "RZ", "B58", 340, 2019, 2998, 500)
]

cursor.executemany("""
INSERT INTO supra_models
(generation, model_name, engine, horsepower, release_year,
 displacement_cc, torque_nm)
VALUES (?, ?, ?, ?, ?, ?, ?)

""", supra_data)

print("Supra data inserted!")
conn.commit()
conn.close()
print("Database connection closed!")