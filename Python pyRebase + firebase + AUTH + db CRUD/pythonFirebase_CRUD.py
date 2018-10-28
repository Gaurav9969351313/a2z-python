import pyrebase

# https://github.com/thisbejim/Pyrebase

config = {
    "apiKey": "AIzaSyC_ae_4BHUnutpGbEJ9wWI8HVD-Td0jFj0",
    "authDomain": "a2withfirebase.firebaseapp.com",
    "databaseURL": "https://a2withfirebase.firebaseio.com",
    "projectId": "a2withfirebase",
    "storageBucket": "a2withfirebase.appspot.com",
    "messagingSenderId": "891625492141"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# user = auth.sign_in_with_email_and_password("gauravtalele123@gmail.com", "gauravtalele")
# print(user)

data = {
    "name": "Mortimer 'Morty' Smith"
}

# results = db.child("users").push(data, user['idToken'])

# auth.create_user_with_email_and_password("kajal17talele@gmail.com", "kajal17talele")

# user = auth.sign_in_with_email_and_password("kajal17talele@gmail.com", "kajal17talele")

# auth.send_email_verification(user['idToken'])

# auth.send_password_reset_email("kajal17talele@gmail.com")

# print(auth.get_account_info(user['idToken']))

db = firebase.database()
db = db.child("users").child("admin_users")

data = {"name": "gaurav talele"}
# To save data with a unique, auto-generated, timestamp-based key, use the push() method.
db.push(data)

# To create your own keys use the set() method. The key in the example below is "Morty".
# data = {"name": "kajal talele"}
# db.child("users").child("admin_users").set(data)

# db.child("users").child("admin_users").update({"name": "Mortiest Morty"})

# db.child("users").child("admin_users").remove()
users = db.child("dishCategories").get()
print(users.val())

storage = firebase.storage()
storage.child("Doc/python2715.chm")
