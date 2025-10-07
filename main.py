import xml.etree.ElementTree as ET

def read_subtask_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    tags = root.find('tags').text
    project_days = int(root.find('projectDays').text)
    
    if project_days <= 365:
        raise ValueError("projectDays must be greater than 365")
    
    return tags, project_days

if __name__ == "__main__":
    try:
        tags, days = read_subtask_from_xml('data.xml')
        print(f"Tags: {tags}, Project Days: {days}")
    except Exception as e:
        print(f"Error: {e}")

