from tinydb import TinyDB,Query #import libry
db=TinyDB('database.json', indent=4, separators=(',', ': ')) #create database and sort
fb=Query()
user=db.table('users')
words=db.table('word')

def saveuser(chat_id):
    
    adm = user.get(doc_id=1)
    l=len(adm)
    if chat_id not in adm.values():
        adm[l+1] = chat_id
        user.update(adm)
def word(txtwords):
    dma=words.get(doc_id=1)
    lw=len(dma)
    if txtwords not in dma.values():
        dma[lw+1] = txtwords
        words.update(dma)

    
    
