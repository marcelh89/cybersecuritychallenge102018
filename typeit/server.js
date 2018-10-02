var CryptoJS = require("crypto-js");
var Promise = require('promise');

//var k = CryptoJS.SHA256("\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\x##"); // ops...missing last byte!
var fixPasswordFrom = "\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\x00"
var fixPasswordTo = "\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13\xEE"

var encrypted = "PKhuCrfh3RUw4vie3OMa8z4kcww1i7198ly0Q4rpuyA="

var lineReader = require('line-reader');

var decryptionPromise = new Promise(function (resolve, reject) {
    var possiblePasswords = []

    lineReader.eachLine('possiblekeys', function (line, last) {

        var dec = CryptoJS.AES.decrypt(encrypted, line).toString()
        dec = dec.toString().replace(/ /g, "")
        dec !== "" ? possiblePasswords.push(dec) : null
        //console.log(dec !== "" ? dec : "empty")

        // do whatever you want with line...
        if (last) {
            console.log("possiblePasswords", possiblePasswords)
            resolve(possiblePasswords)
        }

    })
})


decryptionPromise.then(possiblePasswords => {

    var encryptions = []
    var filteredEncryptions = []

    lineReader.eachLine('possiblekeys', function (line, last) {

    //console.log("")
    //console.log("--------Encryptions-----for key----" + line.toString())
    //2nd try
    //input params
    var k = CryptoJS.SHA256(line.toString()); // ops...missing last byte!
    var u = "\x68\x34\x63\x6b\x33\x72"

    for (key in possiblePasswords) {
        var p = possiblePasswords[key]
        var enc = CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0, 32)), {iv: CryptoJS.enc.Hex.parse(k.toString().substring(32, 64))});
        encryptions.push(enc.toString())
    }


    // do whatever you want with line...
    if (last) {
        filteredEncryptions = encryptions.filter(element => element.length == encrypted.length)
        //console.log(encryptions)
        console.log(filteredEncryptions)
    }
})

})

/*
now we have possiblepasswords filled
*/










