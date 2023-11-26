const http = require('http')

server = http.createServer((req, res) => {
  res
    .setHeader("Access-Control-Allow-Origin", "*")
    .setHeader("Content-Type", "text/event-stream")
    .setHeader("Connection", "keep-alive")
    .setHeader("Cache-Control", "no-cache")

  const timeId = setInterval(() => {
    if (req.destroyed) {
      clearInterval(timeId);
    }
    res.write('event:something_event\n');
    res.write('data:1\n');
    res.write('data:2\n\n');
  }, 1000)

  // for (let i = 0 ; i < 3 ; ++i) {
  //   res.write('event:something_event\n');
  //   res.write(`data:${i}\n\n`);
  // }
  // res.end()
})

server.listen(8000, () => {
  console.log('server on')
})