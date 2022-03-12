const { TwitterApi } = require('twitter-api-v2');
const dotenv = require('dotenv');
dotenv.config();

const client = new TwitterApi({
    appKey: process.env.API_KEY,
    appSecret: process.env.API_SECRET,
    accessToken: process.env.ACCESS_TOKEN,
    accessSecret: process.env.ACCESS_SECRET
})

let mediaID = client.v1.uploadMedia('./assets/itswednesday.mp4', { type: 'mp4', target: 'tweet'});

client.v1.tweet('thisisavideo', { media_ids: mediaID }).then((val) => {
    console.log(val.data.errors)
    //console.log("success")
}).catch((err) => {
    console.log(err)
})

// client.v1.uploadMedia('./assets/itswednesday.mp4', { type: 'longmp4' }).then((response)=>{
//     console.log(response);
//     console.log("video upload success");
// }).catch((error) => {
//     console.log(error);
// });