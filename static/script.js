/*
* JS
*/

var apiUrl = "http://localhost:8010/"
var audio;
var bufferedUrl = "";
var bufferedId = "";

function searchData(query, callback) {
  $.ajax({
    url: apiUrl + "api/v0/query/" + query,
    type: "GET",
    beforeSend: function() {
      $('#main-container').css({'text-align': 'center'})
      $('#main-container').append("<div id='loader-container'><br/><br/><img id='loader' src='ajax-loader.gif'><br/><br/><div id='message-loader'>Looking for awesome new music ! Can take up to 1min to process ...</div></div>")
    },
    complete: function() {
      $('#loader-container').remove()
      $('#main-container').css({'text-align': 'left'})
    },
    success: function(data){
      callback(data)
    }
  });
}

function submitQuery() {
  var q = $("#search-query").val();
  $("#main-container").html("");
  searchData(q, function(data) {
    $("#main-container").append("<div id='tracks-container'></div>")
    var tracks = data.data

    for(var j=0; j<tracks.length; j++) {
      var track = tracks[j]
      html = "<ul><li>"
      html += "<span class='track track-name' title='" + track.name + "'>&nbsp;" + track.name + "</span>&nbsp;"
      html += "<span class='track track-artists' title='" + track.artists + "'> by " + track.artists + "</span>&nbsp;&nbsp;&nbsp;"
      html += "<img id='track-"+j+"' class='track-play' src='https://www.slatecube.com/images/play-btn.png' onclick=\"playSound('"+track.previewUrl+"','track-"+j+"')\"/><br/>"
      html += "</li></ul>"
      $("#tracks-container").append(html)
    }

  });
}

function playSound(url, id) {
    if (typeof audio != 'undefined') {
      audio.pause();
      audio.currentTime = 0;
      $('#'+id).attr("src", "https://www.slatecube.com/images/play-btn.png");
    }
    if (bufferedUrl !== url) {
      $('#'+bufferedId).attr("src", "https://www.slatecube.com/images/play-btn.png");
      audio = new Audio(url);
      audio.play();
      bufferedUrl = url;
      bufferedId = id;
      $('#'+id).attr("src", "stop.png");
    }
}
