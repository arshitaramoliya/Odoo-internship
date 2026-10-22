from pathlib import Path
import xml.etree.ElementTree as ET

xml_path = Path(__file__).with_name("partner_form.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

print("Form:", root.get("string"))

for field in root.findall(".//field"):
    name = field.get("name")
    widget = field.get("widget")

    if field.get("required") == "1":
        required = " (required)"
    else:
        required = ""

    print(f"    {name:<15} {widget}{required}")