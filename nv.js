const https = require('https');

// const options = {
  // host: 'nvzzz.ru/api/dummy',
  // path: '/getShowcase',
  // method: 'GET'
// };

// let request = https.request(options, (res) => { });

// const https = require('https');



let request = https.get('https://nvspc.biz/api/u4H-5t3hM0eMprf6kowrpw', (res) => {
  if (res.statusCode !== 200) {
    console.error(`Did not get an OK from the server. Code: ${res.statusCode}`);
    res.resume();
    return;
  }

  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('close', () => {
    console.log('Retrieved all data');
    console.log(JSON.parse(data));
  });
});
