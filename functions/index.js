import functions from "firebase-functions"
import vision from '@google-cloud/vision'
import { defineSecret } from 'firebase-functions/params'
const googleApiKey = defineSecret('codebrew-2023');
// // Create and deploy your first functions
// // https://firebase.google.com/docs/functions/get-started
//
export const orc = functions.runWith({ minInstances: 1, secrets: [googleApiKey] }).https.onCall(async (data, context) => {
    const client = new vision.ImageAnnotatorClient();

    const imageUrl = data.text;

    const [result] = await client.objectLocalization(imageUrl);
    const objects = result.localizedObjectAnnotations;
    let itemsList = []

    objects.forEach(object => {
        itemsList.push(object.name)
    });

    return { items: itemsList }
    
});
