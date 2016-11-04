# Formation Assignment

import webapp2
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar2 - Rot13</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h3>
        <a href="/">Text Rotating</a>
    </h3>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

form="""
<form method="post">
    <div>
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="{0}">
    </div>
    <textarea type="text" name="text" style="height: 50px; width: 200px;">{1}</textarea>
    <br>
    <input type="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):

    def get(self):

        #temp = ""
        response = page_header + form.format("", "") + page_footer
        self.response.write(response)

    def post(self):

        text_answer = self.request.get("text")
        rot_answer = self.request.get("rot")
        rotNum = int(rot_answer)
        answer = encrypt(text_answer, rotNum)

        response = page_header + form.format(rotNum, answer) + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
