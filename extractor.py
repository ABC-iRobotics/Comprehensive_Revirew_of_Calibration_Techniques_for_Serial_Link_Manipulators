# importing required modules
from pypdf import PdfReader
from pybtex.database.input import bibtex
import yaml 
from pathlib import Path

current_path = Path(__file__).resolve().parent
data_path = current_path / "data.yaml"

with open(data_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

pdf_path = current_path / "Paper.pdf"
bib_path = current_path / "bibliography.bib"

reader = PdfReader(pdf_path)

parser = bibtex.Parser()
bib_data = parser.parse_file(str(bib_path))
bib_data.entries.keys()
oldals = [-1,-2,-3,-4,-5]
for t in range(len(config)):
    for q in oldals:
        page = reader.pages[q]
        text = page.extract_text()
        bib_str = config['cikk_'+str(t)]['name']
        a = ""
        author = bib_data.entries[bib_str].persons['author']
        for i in range(len(author)):
            name = str(author[i]).split(",")
            name = name[1][1:] + " " + name[0]
            if len(author)>3:
                a = a + name + " et al."
                break
            if i <len(author)-2:
                a = a + name + ", "
            elif i <len(author)-1:
                a = a + name +  ", and " 
            else:
                a = a + name 
        x = text.find(a)
        if x == -1:
            a = ""
            for i in range(len(author)):
                name = str(author[i]).split(",")
                name = name[1][1:] + " " + name[0]
                if len(author)>3:
                    a = a + name + " et al."
                    break
                
                if i <len(author)-2:
                    a = a + name + ", "
                elif i <len(author)-1:
                    a = a + name +  " and " 
                else:
                    a = a + name 
        x = text.find(a)        
        if x != -1:
            cite_num = text[x-5:x]
            cite_num = cite_num.split('[')[-1]
            cite_num = cite_num.split(']')[0]
            print(cite_num)
            print (a)
            print(bib_data.entries[bib_str].fields['title'])
            new_yaml_data_dict = {
                'id': int(cite_num),
                'title': bib_data.entries[bib_str].fields['title']
            }
            config['cikk_' + str(t) ].update(new_yaml_data_dict)
            with open(data_path, "w", encoding="utf-8") as yamlfile:
                yaml.safe_dump(config, yamlfile, default_flow_style=False)
            break
        if q == -5:
            print("Title:")
            print(bib_data.entries[bib_str].fields['title'])
            my_id = input("Insert id:")
            new_yaml_data_dict = {
                'id': int(my_id),
                'title': bib_data.entries[bib_str].fields['title']
            }
            config['cikk_' + str(t) ].update(new_yaml_data_dict)
            with open(data_path, "w", encoding="utf-8") as yamlfile:
                yaml.safe_dump(config, yamlfile, default_flow_style=False)
