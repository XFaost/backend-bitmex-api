var socket = new WebSocket('ws://localhost:8000/ws/subscribes');

socket.onmessage = function(event) {
    var data = JSON.parse(event.data);
    console.log(data);
    
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