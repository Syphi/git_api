from ..app import db


class GitInfo(db.Model):
    """Model what describe db table"""
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(500))
    html_url = db.Column(db.String(500))
    description = db.Column(db.Text)
    stargazers_count = db.Column(db.Integer)
    language = db.Column(db.String(50))

    def __repr__(self):
        return f"<Git_Info({self.id}) {self.full_name}>"
