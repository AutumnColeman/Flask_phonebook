from flask import Flask, render_template
import pg

db = pg.DB(dbname='phonebook_v2')
app = Flask('Phonebook')

@app.route('/')
def list_all():
    query = db.query('select * from phonebook')

    return render_template(
        'layout.html',
        title='Phonebook',
        entry_list=query.namedresult())

if __name__ == '__main__':
    app.run(debug=True)
