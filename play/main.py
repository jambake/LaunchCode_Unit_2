import webapp2
import validdate

form="""
<form method="post">
    What is your birthday?
    <br>
    <label> Month
    <input type="text" name="month" value="%(month)s">
    </label>
    <label> Day
    <input type="text" name="day" value="%(day)s">
    </label>
    <label> Year
    <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form % {'error': error})

    def get(self):
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.write_form("That is not a valid day")
        else:
            self.write_form("Thanks!")

    
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
