
function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

var socket = new WebSocket(
        'ws://' + window.location.host + '/ws/subscribes');

socket.onopen = () => {
    console.log("sending account");
    socket.send(JSON.stringify({"name": "my"}));
}
socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

socket.onmessage = function(event) {
    console.log(event.data);
    var data = JSON.parse(event.data);

    var messages = document.getElementById('messages');

    var message = document.createElement("div");
    message.className = "messages__row";
    message.innerHTML = "\
        <div class=\"messages__row__title\">\
            <div class=\"messages__row__title__timestamp\">"
                + data.timestamp +
            "</div>\
            <div class=\"messages__row__title__account\">"
                + data.account +
            "</div>\
        </div>\
        <div class=\"messages__row__subtitle\">\
            <div class=\"messages__row__subtitle__symbol\">"
                + data.symbol +
            "</div>\
            <div class=\"messages__row__subtitle__price\">"
                + data.price +
            "</div>\
        </div>"

    messages.appendChild(message);
}