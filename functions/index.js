const functions = require("firebase-functions");
exports.vision = require('@google-cloud/vision')
const { defineSecret } = require('firebase-functions/params');
const googleApiKey = defineSecret('codebrew-2023');
// // Create and deploy your first functions
// // https://firebase.google.com/docs/functions/get-started
//
exports.orc = functions.runWith({ minInstances: 1, secrets: [googleApiKey] }).https.onCall(async (data, context) => {
    const client = new vision.ImageAnnotatorClient({
        keyFilename: googleApiKey.value()
    });

    const imageUrl = data.text;

    const [result] = await client.objectLocalization(imageUrl);
    const objects = result.localizedObjectAnnotations;

    let itemsList = []

    objects.forEach(object => {
        itemsList.push(...object.name)
    });

   return { items: itemsList }
});
