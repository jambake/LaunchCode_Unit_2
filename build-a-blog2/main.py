import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class NewPost(db.Model):

    title = db.StringProperty(required = True)
    newpost = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class Blog(Handler):

    def render_front(self, title="", newpost="", error=""):
        newposts = db.GqlQuery("SELECT * FROM NewPost ORDER BY created DESC LIMIT 5")

        self.render("base.html", title=title, newpost=newpost, error=error, newposts=newposts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        newpost = self.request.get("newpost")

        if title and newpost:
            a = NewPost(title = title, newpost = newpost)
            a.put()

            self.redirect("/")

        else:
            error = "We need both a title and blog post!"
            self.render_front(title, newpost, error)


app = webapp2.WSGIApplication([
    ('/', Blog)
], debug=True)
