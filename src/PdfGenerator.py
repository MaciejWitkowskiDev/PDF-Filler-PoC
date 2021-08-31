from io import BytesIO
from json import load as json_load
from FormFiller import FormFiller
from FieldMapper import FieldMapper

def main():
    
    with open("test.pdf", "rb") as f:
        filestream = BytesIO(f.read())
    
    with open('mapping.json') as json_file:
        mapping = json_load(json_file)['pit-example']
    
    values = {
        'nip' : '1172204485',
        'urzad': 'Urząd skarbowy Łódź Widzew'
    }
    mapper = FieldMapper(values,mapping)
    formfill = FormFiller(filestream)
    formfill.fillForm(mapper)
    new = formfill.getFilestream()
    with open('output.pdf','wb') as f:
        f.write(new.getbuffer())

main()