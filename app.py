"""Import libraries."""
from flask import Flask, render_template

# TODO: import WTForms

# TODO: import needed fields from WTForms

# TODO: import needed validators from WTForms

# TODO: import Flask SQLAlchemy

# TODO: import Flask SocketIO

# TODO: import Flask Uploads

app = Flask(__name__)
# TODO: create a SECRET_KEY config

app.config["UPLOADED_IMAGES_DEST"] = "static/images"

#  TODO: instantiate UploadSet

# TODO: configure uploads

# TODO: initalize SocketIO

# TODO: create a SQLALCHEMY_DATABASE_URI config with a SQLite database

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# TODO: initalize SQLAlchemy



class Candidate(db.Model):
    # TODO: create an id as a primary key
    # TODO: create "name" as an integer
    # TODO: create a "image" as a string

    # OPTIONAL: create a repr function that returns the candidate's name


class Results(db.Model):
    # TODO: create an id as a primary key
    # TODO: create "vote" as an integer


# TODO: create a CandidateForm using WTForms. it should have a name, image,
#  and submit field


# TODO: create a "calculate_results" function. This function should return a
# dictionary of the count of the two results
# HINT: make a query to each "vote", calculate the total count for each
# vote total, and save it in a variable.


# TODO: create a socketio on "vote" event
    # This function will create a new db object and add it to the db.
    # TODO: emit "vote_results" and pass in a dict of each vote result
    # TODO: remember to send this event to all clients


# TODO: create a route that returns index.html
# TODO: pass in CandidateForm
# TODO: on valid form submission save the image
# TODO: on valid form submission add the candidate to the db
# TODO: make sure you also return the form


# TODO: create a route "/results" the route should return the results from
# the calculate_results function


# TODO: create a route "/candidates" the route should get a query of all
# the candidates but return a dict of the last two candidates
# HINT: use if statements to check the length of candidates so that the terminal
# won't throw IndexErrors


if __name__ == "__main__":
    # TODO: create the database
    # TODO: run the app
