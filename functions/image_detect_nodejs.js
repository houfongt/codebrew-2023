import vision from '@google-cloud/vision';

const client = new vision.ImageAnnotatorClient({
  keyFilename: '/Users/macbook/Keys/codebrew-2023-01234ee1946e.json'
});

const imageUrl = 'https://cdn.britannica.com/17/196817-050-6A15DAC3/vegetables.jpg';

async function detectObjects() {
  const [result] = await client.objectLocalization(imageUrl);
  const objects = result.localizedObjectAnnotations;
  
  objects.forEach(object => {
    console.log(object.name);
  });
}

detectObjects();
