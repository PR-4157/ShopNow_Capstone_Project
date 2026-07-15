import json
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Read weekly summary
with open("reports/weekly-summary.json", "r") as f:
    report = json.load(f)

# Data for PDF table
data = [
    ["Metric", "Count"],
    ["Images Scanned", report["images_scanned"]],
    ["Critical", report["CRITICAL"]],
    ["High", report["HIGH"]],
    ["Medium", report["MEDIUM"]],
    ["Low", report["LOW"]],
]

# Create PDF
pdf = SimpleDocTemplate("reports/security-report.pdf")

table = Table(data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

    ("GRID", (0, 0), (-1, -1), 1, colors.black),

    ("ALIGN", (0, 0), (-1, -1), "CENTER"),

    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
]))

# Build PDF
pdf.build([table])

print("✅ PDF generated successfully.")