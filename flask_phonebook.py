from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook_v2')
app = Flask('Phonebook')

@app.route('/')
def main():
    return render_template(
        'layout.html',
        title='Phonebook',
    # redirect('/new_entry')

@app.route('/listings')
def list_all():
    query = db.query('select * from phonebook')

    return render_template(
        'listings.html',
        title='Phonebook Listings',
        entry_list=query.namedresult())

@app.route('/new_entry')
def new_entry():

    return render_template(
        'new_entry.html',
        title='New Entry'
    )

@app.route('/submit_new_entry', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    cell_phone = request.form.get('cell_phone')
    home_phone = request.form.get('home_phone')
    work_phone = request.form.get('work_phone')
    email = request.form.get('email')
    db.insert(
        'phonebook',
        name=name,
        cell_number=cell_phone,
        home_number=home_phone,
        work_number=work_phone,
        email=email)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
