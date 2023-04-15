const { spawn } = require('child_process');

exports.handler = async function (event, context) {
  const python = spawn('python', ['script1.py']);
  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataToSend = data.toString();
  });
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    return {
      statusCode: 200,
      body: JSON.stringify({ dataToSend }),
    };
  });
  
};
