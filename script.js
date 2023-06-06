const http = require('http');
const url = require('url');
const fs = require('fs');

const server = http.createServer((req, res) => {
  const path = url.parse(req.url, true).pathname;

  if (path === '/') {
    // Serve the HTML form
    fs.readFile('index.html', (err, data) => {
      if (err) {
        res.writeHead(404, {'Content-Type': 'text/html'});
        return res.end('404 Not Found');
      }

      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(data);
      return res.end();
    });
  } else if (path === '/submit') {
    // Handle the form submission
    let body = '';

    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const formData = new URLSearchParams(body);
      const name = formData.get('name');
      const email = formData.get('email');
      const age = formData.get('age');
      const rating = formData.get('rating');
      const visit = formData.get('visit');
      const comment = formData.get('comment');
      const subscribe = formData.get('subscribe');

      // Display the entered data
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(  
res.write('<p><strong>Name:</strong> ' + name + '</p>'));
res.write('<p><strong>Email:</strong> ' + email + '</p>');
res.write('<p><strong>Age:</strong> ' + age + '</p>');
res.write('<p><strong>Website Rating:</strong> ' + rating + '</p>');
res.write('<p><strong>Last Visit Date:</strong> ' + visit + '</p>');
res.write('<p><strong>Comments:</strong> ' + comment + '</p>');
res.write('<p><strong>Subscribe to Newsletter:</strong> ' + (subscribe ? "Yes" : "No") + '</p>');
      return res.end();
    });
  } else {
    // Serve a 404 page for any other request
    res.writeHead(404, {'Content-Type': 'text/html'});
    res.write('404 Not Found');
    return res.end();
  }
});

server.listen(3000, () => {
  console.log('Server listening on port 3000');
});