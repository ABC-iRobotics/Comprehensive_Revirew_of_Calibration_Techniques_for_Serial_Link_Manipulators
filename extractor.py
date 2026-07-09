# importing required modules
from pypdf import PdfReader
from pybtex.database.input import bibtex
import yaml 

## PATH ###
with open(r'C:\Users\karol\Desktop\Munka\cikkek\Images\Images\Cikk\data.yaml') as file:
    config = yaml.safe_load(file)

# creating a pdf reader object
reader = PdfReader(r'C:\Users\karol\Desktop\Munka\cikkek\Images\Images\Cikk\output.pdf')
parser = bibtex.Parser()
bib_data = parser.parse_file(r'C:\Users\karol\Desktop\Munka\cikkek\Images\Images\Cikk\bibliography.bib')
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
            with open('/home/arminkaroly/Munka/Images/Cikk/data.yaml','w') as yamlfile:
                yaml.safe_dump(config, yamlfile, default_flow_style = False)
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
            with open(r'C:\Users\karol\Desktop\Munka\cikkek\Images\Images\Cikk\data.yaml','w') as yamlfile:
                yaml.safe_dump(config, yamlfile, default_flow_style = False)


# Kérdezd meg a chatGPT-t hogy van e benne 2 azonos ID mert ha igen akkor azért lehet mert a szerzők ugyanazok.  
