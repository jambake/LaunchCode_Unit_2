import webapp2

form="""
<form method="post">
  <input name="q">
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(form)


app = webapp2.WSGIApplication([('/', MainPage), debug=True)
