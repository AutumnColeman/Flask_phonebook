from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook_v2')
app = Flask('Phonebook')

@app.route('/')
def main():
    query = db.query('select * from phonebook')

    return render_template(
        'layout.html',
        title='Welcome',
        entry_list=query.namedresult())
    # redirect('/new_entry')

@app.route('/listing')
def list_all():
    query = db.query('select * from phonebook')

    return render_template(
        'listing.html',
        title='Phonebook Entries',
        entry_list=query.namedresult())

@app.route('/edit_entry')
def edit_entry():
    id = request.args.get('id')
    query = db.query('''
    select * from phonebook
    where id = %s ''' % id)
    return render_template(
        'edit_entry.html',
        title='Update Entry',
        entry = query.namedresult()[0]
        )

@app.route('/submit_edit_entry', methods=['POST'])
def submit_edit():
    id = request.form.get('id')
    name = request.form.get('name')
    cell_phone = request.form.get('cell_phone')
    home_phone = request.form.get('home_phone')
    work_phone = request.form.get('work_phone')
    email = request.form.get('email')
    if action == 'update':
        action = request.form.get('action')
        db.update('phonebook', {
            'id': id,
            'name': name,
            'cell_number': cell_phone,
            'work_number': work_phone,
            'home_number': home_phone,
            'email': email
        })
    elif action == 'delete':
        db.delete('phonebook', { 'id': id })
    else:
        raise Exception("I don't understand %s" % action)
    return redirect('/')

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
