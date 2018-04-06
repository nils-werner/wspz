require("./main.js")

var $ = require("jquery");

$.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return decodeURI(results[1]) || 0;
    }
}

$(document).ready(function () {
  if ($.urlParam('month') !== null) {
    $("iframe").attr(
      "src",
      $("iframe").attr("src") + '&dates=' + $.urlParam('month') + '01/' + $.urlParam('month') + '28'
    );
  }
})
