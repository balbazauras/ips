function waitForSocketConnection(socket) {
  setTimeout(function () {
    if (socket.readyState === 0) {
      document.getElementById("status").textContent = "CONNECTING";
      waitForSocketConnection(socket);
    } else if (socket.readyState === 1) {
      document.getElementById("status").textContent = "OPEN";
      waitForSocketConnection(socket);
    } else if (socket.readyState === 2) {
      document.getElementById("status").textContent = "CLOSING";
      waitForSocketConnection(socket);
    } else if (socket.readyState === 3) {
      document.getElementById("status").textContent = "CLOSED";
      waitForSocketConnection(socket);
    }
  }, checkConInterval);
}
function sendToSensor() {
  if (typeof socket === "undefined") {
    alert("You have to connect to sensor");
  } else if (socket.readyState != 1)
    alert("You have to wait to make a connection");
  else {
    let msg = {
      value_lower: document.getElementById("value_lower").value,
      value_upper: document.getElementById("value_upper").value,
    };
    socket.send(JSON.stringify(msg));
  }
}
var checkConInterval = 100; //time interval between checks for websocket connection
var socket;
function init() {
  socket = new WebSocket("ws://" + "192.168.205.85" + ":81/");
  waitForSocketConnection(socket);
  socket.onmessage = function (event) {
    processCommand(event);
  };
}

function processCommand(event) {
  let obj = JSON.parse(event.data);
  document.getElementById("value").innerHTML = obj.value;
  console.log(obj.value);
}
