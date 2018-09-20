//used http://jsnice.org/

'use strict';
/**
 * @param {string} string
 * @return {?}
 */
function strrev(string) {
  if (!string) {
    return "";
  }
  /** @type {string} */
  var paginationStr = "";
  /** @type {number} */
  var i = string.length - 1;
  for (; i >= 0; i--) {
    /** @type {string} */
    paginationStr = paginationStr + string.charAt(i);
  }
  return paginationStr;
}
/**
 * @return {?}
 */
function flag() {
  /** @type {string} */
  var value = "";
  /** @type {string} */
  var a_embed = "7b";
  /** @type {string} */
  a_embed = a_embed + "46";
  /** @type {string} */
  a_embed = a_embed + "4c";
  /** @type {string} */
  a_embed = a_embed + "47";
  /** @type {string} */
  a_embed = a_embed + "3a";
  /** @type {string} */
  a_embed = a_embed + "41";
  /** @type {string} */
  a_embed = a_embed + "6c";
  /** @type {string} */
  a_embed = a_embed + "6c";
  /** @type {string} */
  a_embed = a_embed + "53";
  /** @type {string} */
  a_embed = a_embed + "65";
  /** @type {string} */
  a_embed = a_embed + "74";
  /** @type {string} */
  a_embed = a_embed + "2e";
  /** @type {string} */
  a_embed = a_embed + "4d";
  /** @type {string} */
  a_embed = a_embed + "31";
  /** @type {string} */
  a_embed = a_embed + "73";
  /** @type {string} */
  a_embed = a_embed + "73";
  /** @type {string} */
  a_embed = a_embed + "31";
  /** @type {string} */
  a_embed = a_embed + "4f";
  /** @type {string} */
  a_embed = a_embed + "6e";
  /** @type {string} */
  a_embed = a_embed + "53";
  /** @type {string} */
  a_embed = a_embed + "74";
  /** @type {string} */
  a_embed = a_embed + "61";
  /** @type {string} */
  a_embed = a_embed + "72";
  /** @type {string} */
  a_embed = a_embed + "74";
  /** @type {string} */
  a_embed = a_embed + "33";
  /** @type {string} */
  a_embed = a_embed + "64";
  /** @type {string} */
  a_embed = a_embed + "7d";
  /** @type {number} */
  var i = 0;
  for (; i < a_embed.length; i = i + 2) {
    /** @type {string} */
    value = value + String.fromCharCode(parseInt(a_embed.substr(i, 2), 16));
  }
  return value;
}
/**
 * @return {undefined}
 */
function magic() {
  /** @type {!Array} */
  var a = new Array;
  /** @type {string} */
  a[14] = "x";
  /** @type {string} */
  a[3] = "u";
  /** @type {string} */
  a[11] = "_";
  /** @type {string} */
  a[0] = "0";
  /** @type {string} */
  a[4] = "5";
  /** @type {string} */
  a[15] = "5";
  /** @type {string} */
  a[7] = "7";
  /** @type {string} */
  a[1] = "b";
  /** @type {string} */
  a[13] = "u";
  /** @type {string} */
  a[8] = "1";
  /** @type {string} */
  a[12] = "5";
  /** @type {string} */
  a[2] = "f";
  /** @type {string} */
  a[6] = "4";
  /** @type {string} */
  a[10] = "n";
  /** @type {string} */
  a[5] = "c";
  /** @type {string} */
  a[9] = "0";
  /** @type {string} */

  console.log(a)

  var b = "";
  var href = document.getElementById("pw").value;
  href = strrev(href);
  if (href == a.join("")) {
    /** @type {string} */
    b = "Congratulation! The flag is: " + flag();
  } else {
    /** @type {string} */
    b = "Try again :(";
  }
  /** @type {string} */
  document.getElementById("result").innerHTML = b;
}
;

