var CryptoJS = require("crypto-js");
var Promise = require('promise');

var target = "PKhuCrfh3RUw4vie3OMa8z4kcww1i7198ly0Q4rpuyA="

var lineReader = require('line-reader');

var decryptionPromise = new Promise(function (resolve, reject) {
    var possiblePasswordsUtf8 = []
    var possiblePasswordsUtf16 = []


    lineReader.eachLine('possiblekeys', function (line, last) {

        var bytes = CryptoJS.AES.decrypt(target, line ).toString()
        var decUtf16 = bytes.toString(CryptoJS.enc.Utf16);

        //usually we should work with utf16 because of chinese chars in input
        decUtf16 = decUtf16.toString().replace(/ /g, "")
        decUtf16 !== "" ? possiblePasswordsUtf16.push(decUtf16) : null
        //console.log(dec !== "" ? dec : "empty")


        // do whatever you want with line...
        if (last) {
            console.log("possiblePasswordsUtf16", possiblePasswordsUtf16)
            resolve(possiblePasswordsUtf16)
        }

    })
})


decryptionPromise.then((possiblePasswordsUtf16) => {

    var encryptions = []
    var sameLengthEncryptions = []

    lineReader.eachLine('possiblekeys', function (line, last) {

        //console.log("")
        //console.log("--------Encryptions-----for key----" + line.toString())
        //2nd try
        //input params
        var k = CryptoJS.SHA256(line.toString()); // ops...missing last byte!
        var u = "\x68\x34\x63\x6b\x33\x72"

        for (key in possiblePasswordsUtf16) {
            var p = possiblePasswordsUtf16[key]
            var enc = CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0, 32)), {iv: CryptoJS.enc.Hex.parse(k.toString().substring(32, 64))});
            encryptions.push(enc.toString())
        }


        // do whatever you want with line...
        if (last) {
            filteredEncryptions = encryptions.filter(element => element.length == target.length)
            realPassword = filteredEncryptions.filter(element => element == target)
            //console.log(encryptions)
            console.log("possibleEncryptionsWithSameLength", filteredEncryptions)
            console.log("realPassword", realPassword)
        }
    })

})

/*
now we have possiblePasswordsUtf16 filled
*/










