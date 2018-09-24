var CryptoJS = require("crypto-js");

//var k = CryptoJS.SHA256("\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\x##"); // ops...missing last byte!
var fixPasswordFrom = "\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\x00"
var fixPasswordTo = "\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\xEE"

//TODO loop over all possible last bytes

tmp = []

var lineReader = require('line-reader');

lineReader.eachLine('possiblepasswords', function(line, last) {


   var possiblePassword = line
    console.log(line, typeof line)
    console.log(hex2a(line))
    console.log(hexToString(line))
    encryptAES(possiblePassword);




  // do whatever you want with line...
  if(last){
    // or check if it's the last one
  }
});




function encryptAES(password){


    //encrypt
    var k = CryptoJS.SHA256(password);

    var key = CryptoJS.enc.Hex.parse(k.toString().substring(0, 32))
    var iv = CryptoJS.enc.Hex.parse(k.toString().substring(32, 64))
    var enc = CryptoJS.AES.encrypt(password, key, {iv: iv});

    console.log("")
    console.log("password", password)
    console.log("k - CryptoJS.SHA256(password)", k.toString())
    console.log("key - CryptoJS.enc.Hex.parse(k.toString().substring(0, 32)", key.toString())
    console.log("iv - CryptoJS.enc.Hex.parse(k.toString().substring(32, 64)", iv.toString())
    console.log("enc - CryptoJS.AES.encrypt(password, key, {iv: iv})", enc.toString())


    //decrypt
    /*
    var ciphertext = "PKhuCrfh3RUw4vie3OMa8z4kcww1i7198ly0Q4rpuyA="
    var bytes  = CryptoJS.AES.decrypt(ciphertext, 'secret key 123');
    var originalText = bytes.toString();
    originalText != "" ? tmp.push(originalText) : null ;
    */

}

function hex2a(hexx) {
    var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function hexToString (hex) {
    var string = '';
    for (var i = 0; i < hex.length; i += 2) {
      string += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    }
    return string;
}








