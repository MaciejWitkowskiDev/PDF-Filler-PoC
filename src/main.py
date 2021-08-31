from io import BytesIO
from FormFiller import FormFiller
from FieldMapper import FieldMapper

def main():
    with open("test.pdf", "rb") as f:
        filestream = BytesIO(f.read())
    values = {
        'nip' : '1172204485',
        'urzad': 'Urząd skarbowy Łódź Widzew'
    }
    mapping = {
        'p_1' : 'nip',
        'p_6' : 'urzad'
    }
    mapper = FieldMapper(values,mapping)
    formfill = FormFiller(filestream)
    formfill.fillForm(mapper)
    new = formfill.getFilestream()
    with open('output.pdf','wb') as f:
        f.write(new.getbuffer())

main()