# Remove o gráfico de linguagens dos cards 3D: ele só enxerga repositórios públicos.
import re
import sys
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
PIE = re.compile(r"translate\(40,\s*[\d.]+\)")

for path in sys.argv[1:]:
    tree = ET.parse(path)
    root = tree.getroot()
    for g in root.findall(f"{{{NS}}}g"):
        if PIE.fullmatch(g.get("transform", "")):
            root.remove(g)
    tree.write(path, encoding="utf-8", xml_declaration=False)
