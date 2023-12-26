import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from application import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size) # makes the webapp faster and saves space
    i.save(picture_path)
    return picture_fn


def send_reset_email(user): # Currently facing issue with unsolicited marking by Google
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='support@demo.com',  # Use a real email address that recipients can reply to
                  recipients=[user.email])

    # Create the body of the message (a plain-text and an HTML version).
    msg.body = f"""
    Dear {user.username},

    A request has been received to change the password for your account.

    You can reset your password by clicking on the link below:

    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request, please ignore this email and no changes will be made to your account. If you have any questions or concerns, please reply to this email.

    Best regards,
    Oasis Otaku Team
    """

    mail.send(msg)