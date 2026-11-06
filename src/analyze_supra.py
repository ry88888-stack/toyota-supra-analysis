import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 出力フォルダを作成
os.makedirs("output", exist_ok=True)

# データベースに接続
conn = sqlite3.connect("data/toyota_supra.db")

# SQLでデータを取得
df = pd.read_sql_query("""
SELECT
    generation,
    model_name,
    engine,
    horsepower,
    release_year,
    displacement_cc,
    torque_nm
FROM supra_models
""", conn)

conn.close()

# データ表示
print("=== Toyota Supra Analysis ===")
print(df)

# 馬力の増加率を計算
df["Horsepower_Growth"] = df["horsepower"].pct_change() * 100

# ① 馬力比較
plt.figure(figsize=(8, 5))
plt.bar(df["generation"], df["horsepower"])
plt.title("Toyota Supra - Horsepower Comparison")
plt.xlabel("Generation")
plt.ylabel("Horsepower (PS)")
plt.grid(axis="y")
plt.savefig("output/supra_horsepower.png")

# ② トルク比較
plt.figure(figsize=(8, 5))
plt.bar(df["generation"], df["torque_nm"])
plt.title("Toyota Supra - Torque Comparison")
plt.xlabel("Generation")
plt.ylabel("Torque (Nm)")
plt.grid(axis="y")
plt.savefig("output/supra_torque.png")

# ③ 排気量比較
plt.figure(figsize=(8, 5))
plt.bar(df["generation"], df["displacement_cc"])
plt.title("Toyota Supra - Engine Displacement")
plt.xlabel("Generation")
plt.ylabel("Displacement (cc)")
plt.grid(axis="y")
plt.savefig("output/supra_displacement.png")

# 分析結果を表示
print("\n=== Horsepower Growth ===")
print(df[["generation", "horsepower", "Horsepower_Growth"]])

# CSVに保存
df.to_csv("output/supra_analysis.csv", index=False)

print("\nAnalysis saved successfully!")

# 最後にグラフを表示
plt.show()