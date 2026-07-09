from pathlib import Path
import yaml

# Paths
current_path = Path(__file__).resolve().parent

data_path = current_path / "data.yaml"
table_path = current_path / "table.tex"

with open(data_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)


def make_table(data):
    header = data[0]
    rows = data[1:]

    latex = []
    latex.append(r"\begin{tabular}{|" + "c|" * len(header) + "}")
    latex.append(r"\hline")

    # header
    latex.append(" & ".join(map(str, header)) + r" \\ \hline")

    # rows
    for row in rows:
        latex.append(" & ".join(map(str, row)) + r" \\ \hline")

    latex.append(r"\end{tabular}")

    return "\n".join(latex)

   
low_to_high = ['very_low', 'low', 'medium', 'high', 'very_high']

rows = []

for i in range(len(config)):
    entry = config['cikk_' + str(i)]
    
    NormAcc = ((entry['start_acc'] - entry['fin_acc']) / entry['start_acc'])
    
    cost_score = low_to_high.index(entry['cost']) + 1
    complex_score = low_to_high.index(entry['complex']) + 1
    compute_score = low_to_high.index(entry['compute']) + 1
    
    CEI = NormAcc * 5 / (cost_score * 0.5 + complex_score * 0.35 + compute_score * 0.15)
    
    rows.append([
        entry['id'],
        entry['model'].replace("_", " "),
        entry['optim'].replace("_", " "),
        entry['cost'].replace("_", " ") + " (" + str(cost_score) + ")",
        entry['complex'].replace("_", " ") + " (" + str(complex_score) + ")",
        entry['compute'].replace("_", " ") + " (" + str(compute_score) + ")",
        f"{NormAcc:.5f}",
        f"{CEI:.5f}"
    ])

# Sort rows by CEI value instead of citation number
rows.sort(key=lambda x: float(x[7]), reverse=True)  # Sort by CEI (index 7), in descending order

# add header and format citation as [id]
data = [
    ["Citation", "Modeling", "Optimization", "Estimated cost", "Setup complexity", "Comput. cost", "Norm. acc.", "CEI"]
]

for row in rows:
    row[0] = f"[{row[0]}]"  # format citation
    data.append(row)

# generate LaTeX
table_tex = make_table(data)

with open(table_path, "w", encoding="utf-8") as f:
    f.write(table_tex)

