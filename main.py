from http.server import BaseHTTPRequestHandler, HTTPServer


form = '''<!-- HTML code for a customer feedback form -->

<!DOCTYPE html>
<html>
<head>
  <title>Customer Feedback</title>
  <link rel="stylesheet" type="text/css" href="/styles.css"> <!-- Include an external CSS file -->
</head>
<body>
  <h1>Customer Feedback</h1> <!-- Heading for the feedback form -->
  <form id="myForm" method="POST" action="/"> <!-- Form element with the id "myForm" and method "POST" -->
    <label for="name">Name:</label> <!-- Label for the name input field -->
    <input type="text" id="name" name="name" required> <!-- Text input field for the name, required to be filled -->

    
    <label for="email">Email:</label> <!-- Label for the email input field -->
    <input type="email" id="email" name="email" required> <!-- Email input field, required to be filled -->

    <label for="age">Age:</label> <!-- Label for the age input field -->
    <input type="number" id="age" name="age" min="0" max="150" required> <!-- Number input field for the age, required to be filled and with minimum and maximum values -->

    <label for="rating">Website Rating (1-5):</label> <!-- Label for the rating input field -->
    <div class="rating-input"> <!-- Container for the rating radio buttons -->
      <input type="radio" id="rating1" name="rating" value="1" required> <!-- Radio button for rating 1, required to be selected -->
      <label for="rating1">1</label> <!-- Label for the rating 1 radio button -->

      <input type="radio" id="rating2" name="rating" value="2"> <!-- Radio button for rating 2 -->
      <label for="rating2">2</label> <!-- Label for the rating 2 radio button -->

      <input type="radio" id="rating3" name="rating" value="3"> <!-- Radio button for rating 3 -->
      <label for="rating3">3</label> <!-- Label for the rating 3 radio button -->

      <input type="radio" id="rating4" name="rating" value="4"> <!-- Radio button for rating 4 -->
      <label for="rating4">4</label> <!-- Label for the rating 4 radio button -->

      <input type="radio" id="rating5" name="rating" value="5"> <!-- Radio button for rating 5 -->
      <label for="rating5">5</label> <!-- Label for the rating 5 radio button -->
    </div>

    <label for="visit">Last Visit Date:</label> <!-- Label for the visit input field -->
    <input type="date" id="visit" name="visit" required> <!-- Date input field for the visit, required to be filled -->

    <label for="comment">Comments:</label> <!-- Label for the comment textarea -->
    <textarea id="comment" name="comment" rows="4" required></textarea> <!-- Textarea for the comments, required to be filled -->

    <label for="subscribe">Subscribe to Newsletter:</label> <!-- Label for the subscribe checkbox -->
    <input type="checkbox" id="subscribe" name="subscribe"> <!-- Checkbox for subscribing to the newsletter -->


    <input type="submit" value="Submit"> <!-- Submit button for submitting the form -->
  </form>

  <div id="result"></div> <!-- Placeholder for displaying the form submission result -->

  <script src="/script.js"></script> <!-- Include an external JavaScript file -->
</body>
'''


class MessageBoardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/styles.css':  # Serve the CSS file
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('styles.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/script.js':  # Serve the JavaScript file
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            with open('script.js', 'rb') as file:
                self.wfile.write(file.read())
        else:  # Serve the HTML form
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(form.encode())

    def do_POST(self):
        content_length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(content_length).decode()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode())


def main():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, MessageBoardHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
